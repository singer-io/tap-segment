from tap_segment.streams.sources import Sources
from tap_segment.streams.destinations import Destinations
from tap_segment.streams.warehouses import Warehouses
from tap_segment.streams.source_connected_destinations import SourceConnectedDestinations
from tap_segment.streams.source_connected_warehouses import SourceConnectedWarehouses
from tap_segment.streams.destination_subscriptions import DestinationSubscriptions
from tap_segment.streams.catalog_sources import CatalogSources
from tap_segment.streams.catalog_destinations import CatalogDestinations
from tap_segment.streams.catalog_warehouses import CatalogWarehouses
from tap_segment.streams.usage_api_calls_per_source_daily import UsageApiCallsPerSourceDaily
from tap_segment.streams.usage_api_calls_workspace_daily import UsageApiCallsWorkspaceDaily
from tap_segment.streams.usage_mtu_per_source_daily import UsageMtuPerSourceDaily
from tap_segment.streams.usage_mtu_workspace_daily import UsageMtuWorkspaceDaily
from tap_segment.streams.destination_delivery_metrics_summary import DestinationDeliveryMetricsSummary
from tap_segment.streams.audit_events import AuditEvents
from tap_segment.streams.iam_users import IamUsers
from tap_segment.streams.iam_groups import IamGroups
from tap_segment.streams.transformations import Transformations

STREAMS = {
    "sources": Sources,
    "destinations": Destinations,
    "warehouses": Warehouses,
    "source_connected_destinations": SourceConnectedDestinations,
    "source_connected_warehouses": SourceConnectedWarehouses,
    "destination_subscriptions": DestinationSubscriptions,
    "catalog_sources": CatalogSources,
    "catalog_destinations": CatalogDestinations,
    "catalog_warehouses": CatalogWarehouses,
    "usage_api_calls_per_source_daily": UsageApiCallsPerSourceDaily,
    "usage_api_calls_workspace_daily": UsageApiCallsWorkspaceDaily,
    "usage_mtu_per_source_daily": UsageMtuPerSourceDaily,
    "usage_mtu_workspace_daily": UsageMtuWorkspaceDaily,
    "destination_delivery_metrics_summary": DestinationDeliveryMetricsSummary,
    "audit_events": AuditEvents,
    "iam_users": IamUsers,
    "iam_groups": IamGroups,
    "transformations": Transformations,
}

