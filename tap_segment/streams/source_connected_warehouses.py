from tap_segment.streams.abstracts import FullTableStream

class SourceConnectedWarehouses(FullTableStream):
    tap_stream_id = "source_connected_warehouses"
    key_properties = ["sourceId"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    data_key = "warehouses"
    path = "sources/{sourceId}/connected-warehouses"
    path = "sources"

