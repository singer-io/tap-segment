from tap_segment.streams.abstracts import IncrementalStream


class AuditEvents(IncrementalStream):
    """
    Currently we are skipping this stream, as it requires an Audit trail feature
    enabled for Business Tier account; else we will get a 403 error

    API documentation: https://docs.segmentapis.com/tag/Audit-Trail
    """
    tap_stream_id = "audit_events"
    key_properties = ["id"]
    replication_method = "INCREMENTAL"
    replication_keys = ["timestamp"]
    data_key = "events"
    path = "audit-events"
