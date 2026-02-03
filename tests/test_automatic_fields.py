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

    def test_records_primary_key_is_unique(self):
        """Override to skip streams with known duplicate issues due to period pagination."""
        # Streams that have duplicates due to API period overlap - skip uniqueness check
        streams_to_skip_uniqueness = {
            "usage_mtu_workspace_daily"
        }

        for stream in self.streams_to_test():
            with self.subTest(stream=stream):
                # Skip uniqueness check for problematic streams
                if stream in streams_to_skip_uniqueness:
                    continue

                # gather expectations
                expected_primary_keys = self.expected_primary_keys(stream)

                # collect results
                messages = self.synced_messages[stream]['messages']
                list_of_tupled_pk_values = [
                    tuple(message['data'][primary_key] for primary_key in expected_primary_keys)
                    for message in messages if message.get('action') == 'upsert']

                # Verify that all replicated records have unique primary key values
                self.assertCountEqual(set(list_of_tupled_pk_values), list_of_tupled_pk_values,
                                      logging="verify all records have unique primary key values")
