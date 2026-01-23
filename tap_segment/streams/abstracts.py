from abc import ABC, abstractmethod
import json
import re
from typing import Any, Dict, Tuple, List, Iterator
from datetime import datetime
from dateutil.relativedelta import relativedelta
import dateutil.parser
import dateutil.tz
from singer import (
    Transformer,
    get_bookmark,
    get_logger,
    metrics,
    write_bookmark,
    write_record,
    write_schema,
    metadata
)

LOGGER = get_logger()


class BaseStream(ABC):
    """
    A Base Class providing structure and boilerplate for generic streams
    and required attributes for any kind of stream
    ~~~
    Provides:
     - Basic Attributes (stream_name,replication_method,key_properties)
     - Helper methods for catalog generation
     - `sync` and `get_records` method for performing sync
    """

    url_endpoint = ""
    path = ""
    page_size = 100
    next_page_key = "next"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    children = []
    parent = ""
    data_key = ""
    parent_bookmark_key = ""
    http_method = "GET"
    bookmark_value = None

    def __init__(self, client=None, catalog=None) -> None:
        self.client = client
        self.catalog = catalog
        self.schema = catalog.schema.to_dict()
        self.metadata = metadata.to_map(catalog.metadata)
        self.child_to_sync = []
        self.params = {}
        self.data_payload = {}

    @property
    @abstractmethod
    def tap_stream_id(self) -> str:
        """Unique identifier for the stream.

        This is allowed to be different from the name of the stream, in
        order to allow for sources that have duplicate stream names.
        """

    @property
    @abstractmethod
    def replication_method(self) -> str:
        """Defines the sync mode of a stream."""

    @property
    @abstractmethod
    def replication_keys(self) -> List:
        """Defines the replication key for incremental sync mode of a
        stream."""

    @property
    @abstractmethod
    def key_properties(self) -> Tuple[str, str]:
        """List of key properties for stream."""

    def is_selected(self):
        return metadata.get(self.metadata, (), "selected")

    @abstractmethod
    def sync(
        self,
        state: Dict,
        transformer: Transformer,
        parent_obj: Dict = None,
    ) -> Dict:
        """
        Performs a replication sync for the stream.
        ~~~
        Args:
         - state (dict): represents the state file for the tap.
         - transformer (object): A Object of the singer.transformer class.
         - parent_obj (dict): The parent object for the stream.

        Returns:
         - bool: The return value. True for success, False otherwise.

        Docs:
         - https://github.com/singer-io/getting-started/blob/master/docs/SYNC_MODE.md
        """


    def get_records(self) -> Iterator:
        """Interacts with api client interaction and pagination."""
        current_page = 1
        has_more_pages = True

        while has_more_pages:
            self.params["page"] = current_page

            response = self.client.make_request(
                self.http_method,
                self.url_endpoint,
                self.params,
                self.headers,
                body=json.dumps(self.data_payload),
                path=self.path
            )
            # Extract data from nested response structure
            response_data = response.get("data", {})
            raw_records = response_data.get(self.data_key, [])
            pagination = response_data.get("pagination", {})
            next_page = pagination.get("next") or response_data.get(self.next_page_key)

            yield from raw_records

            # Check if there are more pages to fetch
            if next_page is None or not raw_records:
                has_more_pages = False
            else:
                current_page += 1

    def write_schema(self) -> None:
        """
        Write a schema message.
        """
        try:
            write_schema(self.tap_stream_id, self.schema, self.key_properties)
        except OSError as err:
            LOGGER.error(
                "OS Error while writing schema for: {}".format(self.tap_stream_id)
            )
            raise err

    def update_params(self, **kwargs) -> None:
        """
        Update params for the stream
        """
        self.params.update(kwargs)

    def update_data_payload(self, **kwargs) -> None:
        """
        Update JSON body for the stream
        """
        self.data_payload.update(kwargs)

    def modify_object(self, record: Dict, parent_record: Dict = None) -> Dict:
        """
        Modify the record before writing to the stream
        """
        return record

    def get_url_endpoint(self, parent_obj: Dict = None) -> str:
        """
        Get the URL endpoint for the stream
        """
        return self.url_endpoint or f"{self.client.base_url}/{self.path}"


class IncrementalStream(BaseStream):
    """Base Class for Incremental Stream."""

    # Flag to indicate if stream uses period-based pagination (for usage streams)
    use_period_pagination = False

    def get_bookmark(self, state: dict, stream: str, key: Any = None) -> int:
        """A wrapper for singer.get_bookmark to deal with compatibility for
        bookmark values or start values."""
        return get_bookmark(
            state,
            stream,
            key or self.replication_keys[0],
            self.client.config["start_date"],
        )

    def write_bookmark(self, state: dict, stream: str, key: Any = None, value: Any = None) -> Dict:
        """A wrapper for singer.get_bookmark to deal with compatibility for
        bookmark values or start values."""
        if not (key or self.replication_keys):
            return state

        current_bookmark = get_bookmark(state, stream, key or self.replication_keys[0], self.client.config["start_date"])
        value = max(current_bookmark, value)
        return write_bookmark(
            state, stream, key or self.replication_keys[0], value
        )

    def sync(
        self,
        state: Dict,
        transformer: Transformer,
        parent_obj: Dict = None,
    ) -> Dict:
        """Implementation for `type: Incremental` stream."""
        bookmark_date = self.get_bookmark(state, self.tap_stream_id)
        current_max_bookmark_date = bookmark_date

        self.update_data_payload(parent_obj=parent_obj)
        self.url_endpoint = self.get_url_endpoint(parent_obj)

        # Setup periods for period-based pagination (usage streams) or single iteration for standard
        if self.use_period_pagination:
            # Parse bookmark date and create period list starting from bookmark month
            bookmark_dt = datetime.strptime(bookmark_date.split('T')[0], '%Y-%m-%d')
            today = datetime.utcnow().date()

            # For period-based APIs that fetch monthly data, start from first day of bookmark month
            # But use the actual bookmark date for filtering
            current_period = bookmark_dt.replace(day=1)

            periods = []
            while current_period.date() <= today:
                periods.append(current_period.strftime('%Y-%m-%d'))
                current_period = current_period + relativedelta(months=1)
        else:
            # Standard incremental: single iteration with updated_since
            periods = [None]

        with metrics.record_counter(self.tap_stream_id) as counter:
            for period in periods:
                # Set appropriate parameter based on stream type
                if self.use_period_pagination:
                    LOGGER.info(f"Fetching data for period: {period}")
                    self.update_params(period=period)
                else:
                    self.update_params(updated_since=bookmark_date)

                # Fetch all records for this period/query
                for record in self.get_records():
                    record = self.modify_object(record, parent_obj)
                    transformed_record = transformer.transform(
                        record, self.schema, self.metadata
                    )

                    # Normalize timestamp to remove microseconds - prevents tap-tester parsing bug
                    # where timestamps with microseconds (e.g., .000000Z, .123456Z) are incorrectly
                    # parsed as IST instead of UTC. Removes any 6-digit microsecond component.
                    if self.replication_keys:
                        timestamp_field = self.replication_keys[0]
                        if timestamp_field in transformed_record and transformed_record[timestamp_field]:
                            ts = transformed_record[timestamp_field]
                            if isinstance(ts, str):
                                # Remove microseconds: pattern matches .NNNNNNZ (any 6 digits followed by Z)
                                transformed_record[timestamp_field] = re.sub(r'\.\d{6}Z$', 'Z', ts)

                    record_bookmark = transformed_record[self.replication_keys[0]]
                    # Filter records to only include those >= bookmark_date
                    # Convert both to datetime objects for proper comparison (ensure UTC timezone)
                    try:
                        # Parse dates and ensure they're in UTC for comparison
                        record_dt = dateutil.parser.parse(record_bookmark)
                        if record_dt.tzinfo is None:
                            record_dt = record_dt.replace(tzinfo=dateutil.tz.UTC)

                        bookmark_dt_parsed = dateutil.parser.parse(bookmark_date)
                        if bookmark_dt_parsed.tzinfo is None:
                            bookmark_dt_parsed = bookmark_dt_parsed.replace(tzinfo=dateutil.tz.UTC)

                        should_include = record_dt >= bookmark_dt_parsed
                    except (ValueError, TypeError) as e:
                        # If parsing fails, skip comparison instead of using unreliable string comparison
                        LOGGER.warning(
                            f"Failed to parse date for comparison; skipping record. "
                            f"record_bookmark={record_bookmark!r}, bookmark_date={bookmark_date!r}, error={e}"
                        )
                        should_include = False

                    if should_include:
                        if self.is_selected():
                            write_record(self.tap_stream_id, transformed_record)
                            counter.increment()

                        current_max_bookmark_date = max(
                            current_max_bookmark_date, record_bookmark
                        )

                        for child in self.child_to_sync:
                            child.sync(state=state, transformer=transformer, parent_obj=record)

            state = self.write_bookmark(state, self.tap_stream_id, value=current_max_bookmark_date)
            return counter.value


class FullTableStream(BaseStream):
    """Base Class for Incremental Stream."""

    replication_keys = []

    def sync(
        self,
        state: Dict,
        transformer: Transformer,
        parent_obj: Dict = None,
    ) -> Dict:
        """Abstract implementation for `type: Fulltable` stream."""
        self.url_endpoint = self.get_url_endpoint(parent_obj)
        self.update_data_payload(parent_obj=parent_obj)
        with metrics.record_counter(self.tap_stream_id) as counter:
            for record in self.get_records():
                record = self.modify_object(record, parent_obj)
                transformed_record = transformer.transform(
                    record, self.schema, self.metadata
                )
                if self.is_selected():
                    write_record(self.tap_stream_id, transformed_record)
                    counter.increment()

                for child in self.child_to_sync:
                    child.sync(state=state, transformer=transformer, parent_obj=record)

            return counter.value


class ParentBaseStream(IncrementalStream):
    """Base Class for Parent Stream."""

    def get_bookmark(self, state: Dict, stream: str, key: Any = None) -> int:
        """A wrapper for singer.get_bookmark to deal with compatibility for
        bookmark values or start values."""

        min_parent_bookmark = (
            super().get_bookmark(state, stream) if self.is_selected() else None
        )
        for child in self.child_to_sync:
            bookmark_key = f"{self.tap_stream_id}_{self.replication_keys[0]}"
            child_bookmark = super().get_bookmark(
                state, child.tap_stream_id, key=bookmark_key
            )
            min_parent_bookmark = (
                min(min_parent_bookmark, child_bookmark)
                if min_parent_bookmark
                else child_bookmark
            )

        return min_parent_bookmark

    def write_bookmark(
        self, state: Dict, stream: str, key: Any = None, value: Any = None
    ) -> Dict:
        """A wrapper for singer.get_bookmark to deal with compatibility for
        bookmark values or start values."""
        if self.is_selected():
            super().write_bookmark(state, stream, value=value)

        for child in self.child_to_sync:
            bookmark_key = f"{self.tap_stream_id}_{self.replication_keys[0]}"
            super().write_bookmark(
                state, child.tap_stream_id, key=bookmark_key, value=value
            )

        return state


class ChildBaseStream(IncrementalStream):
    """Base Class for Child Stream."""

    def get_url_endpoint(self, parent_obj=None):
        """Prepare URL endpoint for child streams."""
        return f"{self.client.base_url}/{self.path.format(parent_obj['id'])}"

    def get_bookmark(self, state: Dict, stream: str, key: Any = None) -> int:
        """Singleton bookmark value for child streams."""
        if not self.bookmark_value:
            self.bookmark_value = super().get_bookmark(state, stream)

        return self.bookmark_value


class ChildFullTableStream(FullTableStream):
    """Base Class for FullTable Child Stream."""

    def get_url_endpoint(self, parent_obj=None):
        """Prepare URL endpoint for child streams."""
        return f"{self.client.base_url}/{self.path.format(parent_obj['id'])}"
