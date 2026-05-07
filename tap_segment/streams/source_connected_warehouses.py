from tap_segment.streams.abstracts import ChildFullTableStream


class SourceConnectedWarehouses(ChildFullTableStream):
    tap_stream_id = "source_connected_warehouses"
    key_properties = ["sourceId"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    data_key = "warehouses"
    path = "sources/{sourceId}/connected-warehouses"
    parent = "sources"

    def get_url_endpoint(self, parent_obj=None):
        """Prepare URL endpoint for child stream with sourceId."""
        if parent_obj:
            return f"{self.client.base_url}/{self.path.format(sourceId=parent_obj.get('id'))}"
        return f"{self.client.base_url}/{self.path}"
