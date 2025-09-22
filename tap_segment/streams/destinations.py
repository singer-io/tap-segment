from tap_segment.streams.abstracts import FullTableStream

class Destinations(FullTableStream):
    tap_stream_id = "destinations"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    data_key = "destinations"
    path = "destinations"

