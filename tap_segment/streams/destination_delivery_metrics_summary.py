from tap_segment.streams.abstracts import FullTableStream

class DestinationDeliveryMetricsSummary(FullTableStream):
    tap_stream_id = "destination_delivery_metrics_summary"
    key_properties = ["sourceId"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    data_key = "deliveryMetricsSummary"
    path = "destinations/{destinationId}/delivery-metrics"
    parent = "destinations"
    bookmark_value = None

