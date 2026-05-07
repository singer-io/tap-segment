import json
from typing import Iterator

from tap_segment.streams.abstracts import FullTableStream


class CatalogDestinations(FullTableStream):
    tap_stream_id = "catalog_destinations"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    data_key = "destinationsCatalog"
    path = "catalog/destinations"

    def get_records(self) -> Iterator:
        """Interacts with api client interaction and pagination."""
        has_more_pages = True
        cursor = None

        while has_more_pages:
            self.params["pagination.count"] = self.page_size
            if cursor:
                self.params["pagination.cursor"] = cursor

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
                cursor = next_page
