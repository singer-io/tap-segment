from base import SegmentBaseTest
from tap_tester.base_suite_tests.bookmark_test import BookmarkTest


class SegmentBookMarkTest(BookmarkTest, SegmentBaseTest):
    """Test tap sets a bookmark and respects it for the next sync of a
    stream."""
    bookmark_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    initial_bookmarks = {
        "bookmarks": {
            "usage_api_calls_per_source_daily": { "timestamp" : "2020-01-01T00:00:00Z"},
            "usage_api_calls_workspace_daily": { "timestamp" : "2020-01-01T00:00:00Z"},
            "usage_mtu_per_source_daily": { "timestamp" : "2020-01-01T00:00:00Z"},
            "usage_mtu_workspace_daily": { "timestamp" : "2020-01-01T00:00:00Z"},
            "destination_delivery_metrics_summary": { "timestamp" : "2020-01-01T00:00:00Z"},
            "audit_events": { "timestamp" : "2020-01-01T00:00:00Z"},
        }
    }
    @staticmethod
    def name():
        return "tap_tester_segment_bookmark_test"

    def streams_to_test(self):
        streams_to_exclude = {}
        return self.expected_stream_names().difference(streams_to_exclude)

