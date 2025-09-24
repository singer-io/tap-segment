from tap_segment.streams.abstracts import FullTableStream

class Transformations(FullTableStream):
    tap_stream_id = "transformations"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    data_key = "transformations"
    path = "transformations"

