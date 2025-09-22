from tap_segment.streams.abstracts import IncrementalStream

class UsageApiCallsPerSourceDaily(IncrementalStream):
    tap_stream_id = "usage_api_calls_per_source_daily"
    key_properties = ["sourceId"]
    replication_method = "INCREMENTAL"
    replication_keys = ["timestamp"]
    data_key = "dailyPerSourceAPICallsUsage"
    path = "usage/api-calls/sources/daily"

