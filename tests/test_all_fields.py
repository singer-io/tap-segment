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
        # Due to test data not present excluding streams
        streams_to_exclude = {
            "audit_events",
            "groups",
            "source_connected_warehouses",
            "usage_api_calls_per_source_daily",
            "usage_mtu_per_source_daily",
            "usage_mtu_workspace_daily",
            "transformations",
            "warehouses"
        }
        return self.expected_stream_names().difference(streams_to_exclude)
