from tap_segment.streams.abstracts import FullTableStream

class DestinationSubscriptions(FullTableStream):
    tap_stream_id = "destination_subscriptions"
    key_properties = ["destinationId"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    data_key = "subscriptions"
    path = "destinations/{destinationId}/subscriptions"
    parent = "destinations"

