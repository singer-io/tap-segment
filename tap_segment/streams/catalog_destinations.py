from tap_segment.streams.abstracts import FullTableStream

class CatalogDestinations(FullTableStream):
    tap_stream_id = "catalog_destinations"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    data_key = "destinationsCatalog"
    path = "catalog/destinations"

