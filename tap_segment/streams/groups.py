from tap_segment.streams.abstracts import FullTableStream


class Groups(FullTableStream):
    tap_stream_id = "groups"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    data_key = "userGroups"
    path = "groups"
