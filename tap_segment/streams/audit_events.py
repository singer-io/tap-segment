from tap_segment.streams.abstracts import IncrementalStream

class AuditEvents(IncrementalStream):
    tap_stream_id = "audit_events"
    key_properties = ["id"]
    replication_method = "INCREMENTAL"
    replication_keys = ["timestamp"]
    data_key = "events"
    path = "audit-events"

