from base import SegmentBaseTest
from tap_tester.base_suite_tests.all_fields_test import AllFieldsTest


class SegmentAllFields(AllFieldsTest, SegmentBaseTest):
    """Ensure running the tap with all streams and fields selected results in
    the replication of all fields."""
    MISSING_FIELDS = {
        'destination_subscriptions': {'reverseETLSchedule'}
    }

    @staticmethod
    def name():
        return "tap_tester_segment_all_fields_test"

    def streams_to_test(self):
        streams_to_exclude = {
            # No access to this stream
            "audit_events",
            # Insufficient test data available for these streams
            "groups",
            "source_connected_warehouses",
            "transformations",
            "warehouses",
            "usage_api_calls_per_source_daily",
            "usage_mtu_per_source_daily"
        }
        return self.expected_stream_names().difference(streams_to_exclude)
