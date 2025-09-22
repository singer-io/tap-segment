from tap_segment.streams.abstracts import FullTableStream

class SourceConnectedDestinations(FullTableStream):
    tap_stream_id = "source_connected_destinations"
    key_properties = ["sourceId"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    data_key = "destinations"
    path = "sources/{sourceId}/connected-destinations"
    path = "sources"

