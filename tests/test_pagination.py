from tap_tester.base_suite_tests.pagination_test import PaginationTest
from base import SegmentBaseTest


class SegmentPaginationTest(PaginationTest, SegmentBaseTest):
    """
    Ensure tap can replicate multiple pages of data for streams that use pagination.
    """

    @staticmethod
    def name():
        return "tap_tester_segment_pagination_test"

    def streams_to_test(self):
        # Due to test data not present excluding streams
        streams_to_exclude = {
            "audit_events",
            "groups",
            "source_connected_warehouses",
            "transformations",
            "usage_api_calls_per_source_daily",
            "usage_mtu_per_source_daily",
            "users",
            "warehouses",
            "usage_mtu_workspace_daily"
        }
        return self.expected_stream_names().difference(streams_to_exclude)

    def get_properties(self, original: bool = True):
        """Configuration with reduced page_size to test pagination logic."""
        return {
            "start_date": "2025-09-01T00:00:00Z",
            "page_size": 2
        }

    def expected_page_size(self, stream):
        """
        Return the expected page size for pagination testing.

        Overrides the default API_LIMIT to use the configured page_size.
        This allows pagination testing with smaller datasets by setting
        a lower page limit than the API default (100).
        """
        return 2
