from tap_segment.streams.abstracts import ChildFullTableStream


class DestinationSubscriptions(ChildFullTableStream):
    tap_stream_id = "destination_subscriptions"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    data_key = "subscriptions"
    path = "destinations/{destinationId}/subscriptions"
    parent = "destinations"

    def get_url_endpoint(self, parent_obj=None):
        """Prepare URL endpoint for child stream with destinationId."""
        if parent_obj:
            return f"{self.client.base_url}/{self.path.format(destinationId=parent_obj.get('id'))}"
        return f"{self.client.base_url}/{self.path}"
