from tap_segment.streams.abstracts import FullTableStream

class CatalogSources(FullTableStream):
    tap_stream_id = "catalog_sources"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    data_key = "sourcesCatalog"
    path = "catalog/sources"

