import json
from typing import Dict, Iterator

from singer import get_logger, metrics, Transformer, write_record
from tap_segment.streams.abstracts import ChildFullTableStream

LOGGER = get_logger()


class DestinationDeliveryMetricsSummary(ChildFullTableStream):
    tap_stream_id = "destination_delivery_metrics_summary"
    key_properties = ["sourceId", "destinationId"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    data_key = "deliveryMetricsSummary"
    path = "destinations/{destinationId}/delivery-metrics"
    parent = "destinations"
    bookmark_value = None

    def get_url_endpoint(self, parent_obj=None):
        """Prepare URL endpoint for child stream with destinationId."""
        if parent_obj:
            return f"{self.client.base_url}/{self.path.format(destinationId=parent_obj.get('id'))}"
        return f"{self.client.base_url}/{self.path}"

    def get_records(self) -> Iterator:
        """Override to handle single object response instead of array."""
        response = self.client.make_request(
            self.http_method,
            self.url_endpoint,
            self.params,
            self.headers,
            body=json.dumps(self.data_payload),
            path=self.path
        )
        response_data = response.get("data", {})
        record = response_data.get(self.data_key, {})

        if record:
            yield record

    def modify_object(self, record, parent_record=None):
        """Add destinationId and sourceId from parent to the record."""
        if parent_record:
            record["destinationId"] = parent_record['id']
            if 'sourceId' in parent_record:
                record["sourceId"] = parent_record['sourceId']
        return record

    def sync(
        self,
        state: Dict,
        transformer: Transformer,
        parent_obj: Dict = None,
    ) -> Dict:
        """Override sync to add sourceId as query parameter."""
        self.url_endpoint = self.get_url_endpoint(parent_obj)
        self.update_data_payload(parent_obj=parent_obj)

        # Add sourceId from parent as query parameter
        if parent_obj and 'sourceId' in parent_obj:
            self.update_params(sourceId=parent_obj['sourceId'])
            LOGGER.info(f"Added sourceId query param: {parent_obj['sourceId']}")

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
