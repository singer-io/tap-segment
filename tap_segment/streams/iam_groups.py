from tap_segment.streams.abstracts import FullTableStream

class IamGroups(FullTableStream):
    tap_stream_id = "iam_groups"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    data_key = "userGroups"
    path = "groups"

