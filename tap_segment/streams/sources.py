from tap_segment.streams.abstracts import FullTableStream

class Sources(FullTableStream):
    tap_stream_id = "sources"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    data_key = "sources"
    path = "sources"

