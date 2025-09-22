from tap_segment.streams.abstracts import ChildBaseStream

class DestinationDeliveryMetricsSummary(ChildBaseStream):
    tap_stream_id = "destination_delivery_metrics_summary"
    key_properties = ["destinationId"]
    replication_method = "INCREMENTAL"
    replication_keys = ["timestamp"]
    data_key = "deliveryMetricsSummary"
    path = "destinations/{destinationId}/delivery-metrics"
    parent = "destinations"
    bookmark_value = None

