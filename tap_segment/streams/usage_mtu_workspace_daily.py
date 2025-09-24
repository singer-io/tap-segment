from tap_segment.streams.abstracts import IncrementalStream

class UsageMtuWorkspaceDaily(IncrementalStream):
    tap_stream_id = "usage_mtu_workspace_daily"
    key_properties = ["timestamp"]
    replication_method = "INCREMENTAL"
    replication_keys = ["timestamp"]
    data_key = "dailyWorkspaceMTUUsage"
    path = "usage/mtu/daily"

