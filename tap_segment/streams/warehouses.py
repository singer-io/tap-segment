from tap_segment.streams.abstracts import FullTableStream

class Warehouses(FullTableStream):
    tap_stream_id = "warehouses"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    data_key = "warehouses"
    path = "warehouses"

