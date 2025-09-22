# tap-segment

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/docs/SPEC.md).

This tap:

- Pulls raw data from the [Segment API].
- Extracts the following resources:
    - [Sources](https://docs.segmentapis.com/tag/Sources/#operation/listSources)

    - [Destinations](https://docs.segmentapis.com/tag/Destinations/#operation/listDestinations)

    - [Warehouses](https://docs.segmentapis.com/tag/Warehouses/#operation/listWarehouses)

    - [SourceConnectedDestinations](https://docs.segmentapis.com/tag/Sources/#operation/listConnectedDestinationsFromSource)

    - [SourceConnectedWarehouses](https://docs.segmentapis.com/tag/Sources/#operation/listConnectedWarehousesFromSource)

    - [DestinationSubscriptions](https://docs.segmentapis.com/tag/Destinations/#operation/listSubscriptionsFromDestination)

    - [CatalogSources](https://docs.segmentapis.com/tag/Catalog/#operation/getSourcesCatalog)

    - [CatalogDestinations](https://docs.segmentapis.com/tag/Catalog/#operation/getDestinationsCatalog)

    - [CatalogWarehouses](https://docs.segmentapis.com/tag/Catalog/#operation/getWarehousesCatalog)

    - [UsageApiCallsPerSourceDaily](https://docs.segmentapis.com/tag/API-Calls/#operation/getDailyPerSourceAPICallsUsage)

    - [UsageApiCallsWorkspaceDaily](https://docs.segmentapis.com/tag/API-Calls/#operation/getDailyPerWorkspaceAPICallsUsage)

    - [UsageMtuPerSourceDaily](https://docs.segmentapis.com/tag/Monthly-Tracked-Users/#operation/getDailyPerSourceMTUUsage)

    - [UsageMtuWorkspaceDaily](https://docs.segmentapis.com/tag/Monthly-Tracked-Users/#operation/getDailyPerWorkspaceMTUUsage)

    - [DestinationDeliveryMetricsSummary](https://docs.segmentapis.com/tag/Destinations/#operation/listDeliveryMetricsSummaryFromDestination)

    - [AuditEvents](https://docs.segmentapis.com/tag/Audit-Trail/#operation/listAuditEvents)

    - [IamUsers](https://docs.segmentapis.com/tag/IAM-Users/#operation/listUsers)

    - [IamGroups](https://docs.segmentapis.com/tag/IAM-Groups/#operation/listUserGroups)

    - [Transformations](https://docs.segmentapis.com/tag/Transformations/#operation/listTransformations)

- Outputs the schema for each resource
- Incrementally pulls data based on the input state


## Streams


**[sources](https://docs.segmentapis.com/tag/Sources/#operation/listSources)**
- Data Key = sources
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[destinations](https://docs.segmentapis.com/tag/Destinations/#operation/listDestinations)**
- Data Key = destinations
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[warehouses](https://docs.segmentapis.com/tag/Warehouses/#operation/listWarehouses)**
- Data Key = warehouses
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[source_connected_destinations](https://docs.segmentapis.com/tag/Sources/#operation/listConnectedDestinationsFromSource)**
- Data Key = destinations
- Primary keys: ['sourceId']
- Replication strategy: FULL_TABLE

**[source_connected_warehouses](https://docs.segmentapis.com/tag/Sources/#operation/listConnectedWarehousesFromSource)**
- Data Key = warehouses
- Primary keys: ['sourceId']
- Replication strategy: FULL_TABLE

**[destination_subscriptions](https://docs.segmentapis.com/tag/Destinations/#operation/listSubscriptionsFromDestination)**
- Data Key = subscriptions
- Primary keys: ['destinationId']
- Replication strategy: FULL_TABLE

**[catalog_sources](https://docs.segmentapis.com/tag/Catalog/#operation/getSourcesCatalog)**
- Data Key = sourcesCatalog
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[catalog_destinations](https://docs.segmentapis.com/tag/Catalog/#operation/getDestinationsCatalog)**
- Data Key = destinationsCatalog
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[catalog_warehouses](https://docs.segmentapis.com/tag/Catalog/#operation/getWarehousesCatalog)**
- Data Key = warehousesCatalog
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[usage_api_calls_per_source_daily](https://docs.segmentapis.com/tag/API-Calls/#operation/getDailyPerSourceAPICallsUsage)**
- Data Key = dailyPerSourceAPICallsUsage
- Primary keys: ['sourceId']
- Replication strategy: INCREMENTAL

**[usage_api_calls_workspace_daily](https://docs.segmentapis.com/tag/API-Calls/#operation/getDailyPerWorkspaceAPICallsUsage)**
- Data Key = dailyWorkspaceAPICallsUsage
- Primary keys: ['timestamp']
- Replication strategy: INCREMENTAL

**[usage_mtu_per_source_daily](https://docs.segmentapis.com/tag/Monthly-Tracked-Users/#operation/getDailyPerSourceMTUUsage)**
- Data Key = dailyPerSourceMTUUsage
- Primary keys: ['sourceId']
- Replication strategy: INCREMENTAL

**[usage_mtu_workspace_daily](https://docs.segmentapis.com/tag/Monthly-Tracked-Users/#operation/getDailyPerWorkspaceMTUUsage)**
- Data Key = dailyWorkspaceMTUUsage
- Primary keys: ['timestamp']
- Replication strategy: INCREMENTAL

**[destination_delivery_metrics_summary](https://docs.segmentapis.com/tag/Destinations/#operation/listDeliveryMetricsSummaryFromDestination)**
- Data Key = deliveryMetricsSummary
- Primary keys: ['destinationId']
- Replication strategy: INCREMENTAL

**[audit_events](https://docs.segmentapis.com/tag/Audit-Trail/#operation/listAuditEvents)**
- Data Key = events
- Primary keys: ['id']
- Replication strategy: INCREMENTAL

**[iam_users](https://docs.segmentapis.com/tag/IAM-Users/#operation/listUsers)**
- Data Key = users
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[iam_groups](https://docs.segmentapis.com/tag/IAM-Groups/#operation/listUserGroups)**
- Data Key = userGroups
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[transformations](https://docs.segmentapis.com/tag/Transformations/#operation/listTransformations)**
- Data Key = transformations
- Primary keys: ['id']
- Replication strategy: FULL_TABLE



## Authentication

## Quick Start

1. Install

    Clone this repository, and then install using setup.py. We recommend using a virtualenv:

    ```bash
    > virtualenv -p python3 venv
    > source venv/bin/activate
    > python setup.py install
    OR
    > cd .../tap-segment
    > pip install -e .
    ```
2. Dependent libraries. The following dependent libraries were installed.
    ```bash
    > pip install singer-python
    > pip install target-stitch
    > pip install target-json

    ```
    - [singer-tools](https://github.com/singer-io/singer-tools)
    - [target-stitch](https://github.com/singer-io/target-stitch)

3. Create your tap's `config.json` file.  The tap config file for this tap should include these entries:
   - `start_date` - the default value to use if no bookmark exists for an endpoint (rfc3339 date string)
   - `user_agent` (string, optional): Process and email for API logging purposes. Example: `tap-segment <api_user_email@your_company.com>`
   - `request_timeout` (integer, `300`): Max time for which request should wait to get a response. Default request_timeout is 300 seconds.

    ```json
    {
        "start_date": "2019-01-01T00:00:00Z",
        "user_agent": "tap-segment <api_user_email@your_company.com>",
        "request_timeout": 300
    }```

    Optionally, also create a `state.json` file. `currently_syncing` is an optional attribute used for identifying the last object to be synced in case the job is interrupted mid-stream. The next run would begin where the last job left off.

    ```json
    {
        "currently_syncing": "engage",
        "bookmarks": {
            "export": "2019-09-27T22:34:39.000000Z",
            "funnels": "2019-09-28T15:30:26.000000Z",
            "revenue": "2019-09-28T18:23:53Z"
        }
    }
    ```

4. Run the Tap in Discovery Mode
    This creates a catalog.json for selecting objects/fields to integrate:
    ```bash
    tap-segment --config config.json --discover > catalog.json
    ```
   See the Singer docs on discovery mode
   [here](https://github.com/singer-io/getting-started/blob/master/docs/DISCOVERY_MODE.md#discovery-mode).

5. Run the Tap in Sync Mode (with catalog) and [write out to state file](https://github.com/singer-io/getting-started/blob/master/docs/RUNNING_AND_DEVELOPING.md#running-a-singer-tap-with-a-singer-target)

    For Sync mode:
    ```bash
    > tap-segment --config tap_config.json --catalog catalog.json > state.json
    > tail -1 state.json > state.json.tmp && mv state.json.tmp state.json
    ```
    To load to json files to verify outputs:
    ```bash
    > tap-segment --config tap_config.json --catalog catalog.json | target-json > state.json
    > tail -1 state.json > state.json.tmp && mv state.json.tmp state.json
    ```
    To pseudo-load to [Stitch Import API](https://github.com/singer-io/target-stitch) with dry run:
    ```bash
    > tap-segment --config tap_config.json --catalog catalog.json | target-stitch --config target_config.json --dry-run > state.json
    > tail -1 state.json > state.json.tmp && mv state.json.tmp state.json
    ```

6. Test the Tap
    While developing the segment tap, the following utilities were run in accordance with Singer.io best practices:
    Pylint to improve [code quality](https://github.com/singer-io/getting-started/blob/master/docs/BEST_PRACTICES.md#code-quality):
    ```bash
    > pylint tap_segment -d missing-docstring -d logging-format-interpolation -d too-many-locals -d too-many-arguments
    ```
    Pylint test resulted in the following score:
    ```bash
    Your code has been rated at 9.67/10
    ```

    To [check the tap](https://github.com/singer-io/singer-tools#singer-check-tap) and verify working:
    ```bash
    > tap_segment --config tap_config.json --catalog catalog.json | singer-check-tap > state.json
    > tail -1 state.json > state.json.tmp && mv state.json.tmp state.json
    ```

    #### Unit Tests

    Unit tests may be run with the following.

    ```
    python -m pytest --verbose
    ```

    Note, you may need to install test dependencies.

    ```
    pip install -e .'[dev]'
    ```
---

Copyright &copy; 2019 Stitch
