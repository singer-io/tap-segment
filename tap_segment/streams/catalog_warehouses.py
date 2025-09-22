from tap_segment.streams.abstracts import FullTableStream

class CatalogWarehouses(FullTableStream):
    tap_stream_id = "catalog_warehouses"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    data_key = "warehousesCatalog"
    path = "catalog/warehouses"

