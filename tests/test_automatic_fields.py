"""Test that with no fields selected for a stream automatic fields are still
replicated."""
from base import SegmentBaseTest
from tap_tester.base_suite_tests.automatic_fields_test import MinimumSelectionTest


class SegmentAutomaticFields(MinimumSelectionTest, SegmentBaseTest):
    """Test that with no fields selected for a stream automatic fields are
    still replicated."""

    @staticmethod
    def name():
        return "tap_tester_segment_automatic_fields_test"

    def streams_to_test(self):
        # Due to test data not present excluding streams
        streams_to_exclude = {
            "audit_events",
            "destination_delivery_metrics_summary",
            "groups",
            "source_connected_warehouses",
            "usage_api_calls_per_source_daily",
            "usage_mtu_per_source_daily",
            "usage_mtu_workspace_daily",
            "transformations",
            "warehouses"
        }
        return self.expected_stream_names().difference(streams_to_exclude)
