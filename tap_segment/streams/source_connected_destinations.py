from tap_segment.streams.abstracts import ChildFullTableStream


class SourceConnectedDestinations(ChildFullTableStream):
    tap_stream_id = "source_connected_destinations"
    key_properties = ["sourceId", "id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    data_key = "destinations"
    path = "sources/{sourceId}/connected-destinations"
    parent = "sources"

    def get_url_endpoint(self, parent_obj=None):
        """Prepare URL endpoint for child stream with sourceId."""
        if parent_obj:
            return f"{self.client.base_url}/{self.path.format(sourceId=parent_obj.get('id'))}"
        return f"{self.client.base_url}/{self.path}"
