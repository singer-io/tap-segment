from base import SegmentBaseTest
from tap_tester.base_suite_tests.bookmark_test import BookmarkTest


class SegmentBookMarkTest(BookmarkTest, SegmentBaseTest):
    """Test tap sets a bookmark and respects it for the next sync of a
    stream."""
    bookmark_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    initial_bookmarks = {
        "bookmarks": {
            "usage_api_calls_workspace_daily": { "timestamp" : "2025-09-01T00:00:00Z"},
            "usage_mtu_workspace_daily": { "timestamp" : "2025-09-01T00:00:00Z"}
        }
    }
    @staticmethod
    def name():
        return "tap_tester_segment_bookmark_test"

    def streams_to_test(self):
        # Excluding below streams, as these streams use full table replication
        # Excluding 'audit_events', 'usage_api_calls_per_source_daily' since it has no test data
        streams_to_exclude = {
            "audit_events",
            "catalog_destinations",
            "catalog_sources",
            "catalog_warehouses",
            "destination_delivery_metrics_summary",
            "destination_subscriptions",
            "destinations",
            "groups",
            "source_connected_destinations",
            "source_connected_warehouses",
            "sources",
            "transformations",
            "usage_api_calls_per_source_daily",
            "usage_mtu_per_source_daily",
            "users",
            "warehouses"
        }
        return self.expected_stream_names().difference(streams_to_exclude)
