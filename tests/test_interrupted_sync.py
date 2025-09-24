
from base import SegmentBaseTest
from tap_tester.base_suite_tests.interrupted_sync_test import InterruptedSyncTest


class SegmentInterruptedSyncTest(InterruptedSyncTest, SegmentBaseTest):
    """Test tap sets a bookmark and respects it for the next sync of a
    stream."""

    @staticmethod
    def name():
        return "tap_tester_segment_interrupted_sync_test"

    def streams_to_test(self):
        return self.expected_stream_names()


    def manipulate_state(self):
        return {
            "currently_syncing": "prospects",
            "bookmarks": {
                "usage_api_calls_per_source_daily": { "timestamp" : "2020-01-01T00:00:00Z"},
                "usage_api_calls_workspace_daily": { "timestamp" : "2020-01-01T00:00:00Z"},
                "usage_mtu_per_source_daily": { "timestamp" : "2020-01-01T00:00:00Z"},
                "usage_mtu_workspace_daily": { "timestamp" : "2020-01-01T00:00:00Z"},
                "destination_delivery_metrics_summary": { "timestamp" : "2020-01-01T00:00:00Z"},
                "audit_events": { "timestamp" : "2020-01-01T00:00:00Z"},
        }
    }

