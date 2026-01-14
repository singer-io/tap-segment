from typing import Dict

from singer import (
    Transformer,
    metrics,
    write_record
)

from tap_segment.streams.abstracts import IncrementalStream


class UsageMtuWorkspaceDaily(IncrementalStream):
    tap_stream_id = "usage_mtu_workspace_daily"
    key_properties = ["timestamp"]
    replication_method = "INCREMENTAL"
    replication_keys = ["timestamp"]
    data_key = "dailyWorkspaceMTUUsage"
    path = "usage/mtu/daily"

    def sync(
        self,
        state: Dict,
        transformer: Transformer,
        parent_obj: Dict = None,
    ) -> Dict:
        """ Require 'period' parameter instead of 'updated_since' for usage streams."""
        bookmark_date = self.get_bookmark(state, self.tap_stream_id)
        current_max_bookmark_date = bookmark_date

        # Extract just date part to use as the period parameter
        period_param = bookmark_date.split('T')[0] if 'T' in bookmark_date else bookmark_date
        self.update_params(period=period_param)
        self.update_data_payload(parent_obj=parent_obj)
        self.url_endpoint = self.get_url_endpoint(parent_obj)

        with metrics.record_counter(self.tap_stream_id) as counter:
            for record in self.get_records():
                record = self.modify_object(record, parent_obj)
                transformed_record = transformer.transform(
                    record, self.schema, self.metadata
                )

                record_bookmark = transformed_record[self.replication_keys[0]]
                if record_bookmark >= bookmark_date:
                    if self.is_selected():
                        write_record(self.tap_stream_id, transformed_record)
                        counter.increment()

                    current_max_bookmark_date = max(
                        current_max_bookmark_date, record_bookmark
                    )

            state = self.write_bookmark(state, self.tap_stream_id, value=current_max_bookmark_date)
            return counter.value
