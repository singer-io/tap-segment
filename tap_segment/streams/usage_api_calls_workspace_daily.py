from tap_segment.streams.abstracts import IncrementalStream

class UsageApiCallsWorkspaceDaily(IncrementalStream):
    tap_stream_id = "usage_api_calls_workspace_daily"
    key_properties = ["timestamp"]
    replication_method = "INCREMENTAL"
    replication_keys = ["timestamp"]
    data_key = "dailyWorkspaceAPICallsUsage"
    path = "usage/api-calls/daily"

