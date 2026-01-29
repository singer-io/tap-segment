
from base import SegmentBaseTest
from tap_tester.base_suite_tests.interrupted_sync_test import InterruptedSyncTest


class SegmentInterruptedSyncTest(InterruptedSyncTest, SegmentBaseTest):
    """Test tap sets a bookmark and respects it for the next sync of a
    stream."""

    @staticmethod
    def name():
        return "tap_tester_segment_interrupted_sync_test"

    def streams_to_test(self):
        streams_to_exclude = {
            # No access to this stream
            "audit_events",
            # Full table replication streams (no bookmark/interruption support)
            "catalog_destinations",
            "catalog_sources",
            "catalog_warehouses",
            "destination_subscriptions",
            "destinations",
            "source_connected_destinations",
            "sources",
            "users",
            # Insufficient test data available for these streams
            "destination_delivery_metrics_summary",
            "groups",
            "source_connected_warehouses",
            "transformations",
            "usage_api_calls_per_source_daily",
            "usage_mtu_per_source_daily",
            "warehouses"
        }
        return self.expected_stream_names().difference(streams_to_exclude)

    def manipulate_state(self):
        return {
            "currently_syncing": "usage_api_calls_workspace_daily",
            "bookmarks": {
                "usage_api_calls_workspace_daily": {"timestamp": "2025-07-01T00:00:00Z"},
                "usage_mtu_workspace_daily": {"timestamp": "2025-07-01T00:00:00Z"}
            }
        }

