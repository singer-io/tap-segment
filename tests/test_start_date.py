from base import SegmentBaseTest
from tap_tester.base_suite_tests.start_date_test import StartDateTest



class SegmentStartDateTest(StartDateTest, SegmentBaseTest):
    """Instantiate start date according to the desired data set and run the
    test."""

    @staticmethod
    def name():
        return "tap_tester_segment_start_date_test"

    def streams_to_test(self):
        # Due to test data not present excluding streams
        streams_to_exclude = {
            "audit_events",
            "warehouses",
            "source_connected_warehouses",
            "usage_api_calls_per_source_daily",
            "usage_mtu_per_source_daily",
            "groups",
            "transformations",
            #  full table streams
            "catalog_destinations",
            "users",
            # "usage_api_calls_workspace_daily",
            "catalog_sources",
            "sources",
            "destination_delivery_metrics_summary",
            "destination_subscriptions",
            "usage_mtu_workspace_daily",
            "source_connected_destinations",
            "catalog_warehouses",
            "destinations",
        }
        return self.expected_stream_names().difference(streams_to_exclude)

    @property
    def start_date_1(self):
        return "2025-11-01T00:00:00Z"
    @property
    def start_date_2(self):
        return "2026-01-01T00:00:00Z"
