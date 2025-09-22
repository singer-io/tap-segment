from tap_segment.streams.abstracts import IncrementalStream

class UsageMtuPerSourceDaily(IncrementalStream):
    tap_stream_id = "usage_mtu_per_source_daily"
    key_properties = ["sourceId"]
    replication_method = "INCREMENTAL"
    replication_keys = ["timestamp"]
    data_key = "dailyPerSourceMTUUsage"
    path = "usage/mtu/sources/daily"

