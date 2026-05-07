from tap_segment.streams.abstracts import FullTableStream


class Users(FullTableStream):
    tap_stream_id = "users"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    data_key = "users"
    path = "users"
