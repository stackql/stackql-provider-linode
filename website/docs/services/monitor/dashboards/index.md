--- 
title: dashboards
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboards
  - monitor
  - linode
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage linode resources using SQL
custom_edit_url: null
image: /img/stackql-linode-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>dashboards</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.monitor.dashboards" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_dashboards_by_id"
    values={[
        { label: 'get_dashboards_by_id', value: 'get_dashboards_by_id' },
        { label: 'get_dashboards', value: 'get_dashboards' },
        { label: 'get_dashboards_all', value: 'get_dashboards_all' }
    ]}
>
<TabItem value="get_dashboards_by_id">

Returns a dashboard.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="id" /></td>
    <td><code>integer</code></td>
    <td>The unique identifier for the dashboard.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the dashboard was created. (example: 2024-10-10T05:01:58Z)</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>The name of the dashboard. This is used for display purposes in Akamai Cloud Manager. (example: Resource Usage)</td>
</tr>
<tr>
    <td><CopyableCode code="service_type" /></td>
    <td><code>string</code></td>
    <td>The Akamai Cloud Computing service used by this dashboard. Currently, only the Managed Databases (`dbaas`) service is supported. (example: dbaas)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of dashboard. Currently, this can only be `standard` for a dashboard that uses default formatting. (example: standard)</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the dashboard was last updated. (example: 2024-10-12T08:15:37Z)</td>
</tr>
<tr>
    <td><CopyableCode code="widgets" /></td>
    <td><code>array</code></td>
    <td>The widgets used in the dashboard.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_dashboards">

Returns a paginated list of dashboards.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="data" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The current [page](https://techdocs.akamai.com/linode-api/reference/pagination).</td>
</tr>
<tr>
    <td><CopyableCode code="pages" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The total number of [pages](https://techdocs.akamai.com/linode-api/reference/pagination).</td>
</tr>
<tr>
    <td><CopyableCode code="results" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The total number of results.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_dashboards_all">

Returns a paginated list of dashboards.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="id" /></td>
    <td><code>integer</code></td>
    <td>The unique identifier for the dashboard.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the dashboard was created. (example: 2024-10-10T05:01:58Z)</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>The name of the dashboard. This is used for display purposes in Akamai Cloud Manager. (example: Resource Usage)</td>
</tr>
<tr>
    <td><CopyableCode code="service_type" /></td>
    <td><code>string</code></td>
    <td>The Akamai Cloud Computing service used by this dashboard. Currently, only the Managed Databases (`dbaas`) service is supported. (example: dbaas)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of dashboard. Currently, this can only be `standard` for a dashboard that uses default formatting. (example: standard)</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the dashboard was last updated. (example: 2024-10-12T08:15:37Z)</td>
</tr>
<tr>
    <td><CopyableCode code="widgets" /></td>
    <td><code>array</code></td>
    <td>The widgets used in the dashboard.</td>
</tr>
</tbody>
</table>
</TabItem>
</Tabs>

## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#get_dashboards_by_id"><CopyableCode code="get_dashboards_by_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>__Beta__ Returns a specific dashboard, based on its unique ID. You can run the [List dashboards](https://techdocs.akamai.com/linode-api/reference/get-dashboards-all) operation to see the ID for all dashboards.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation is beta. Call it using the `v4beta` path in its URL.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_dashboards"><CopyableCode code="get_dashboards" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>__Beta__ Returns all available dashboards for a given service type. Include the appropriate `service_type` as a path parameter.<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation is beta. Call it using the `v4beta` path in its URL.<br />&gt;<br />&gt; - Currently, only the Managed Databases (`dbaas`) service type is supported.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_dashboards_all"><CopyableCode code="get_dashboards_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>__Beta__ Returns all available dashboards.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation is beta. Call it using the `v4beta` path in its URL.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_dashboards_by_id"
    values={[
        { label: 'get_dashboards_by_id', value: 'get_dashboards_by_id' },
        { label: 'get_dashboards', value: 'get_dashboards' },
        { label: 'get_dashboards_all', value: 'get_dashboards_all' }
    ]}
>
<TabItem value="get_dashboards_by_id">

__Beta__ Returns a specific dashboard, based on its unique ID. You can run the [List dashboards](https://techdocs.akamai.com/linode-api/reference/get-dashboards-all) operation to see the ID for all dashboards.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation is beta. Call it using the `v4beta` path in its URL.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
created,
label,
service_type,
type,
updated,
widgets
FROM linode.monitor.dashboards
;
```
</TabItem>
<TabItem value="get_dashboards">

__Beta__ Returns all available dashboards for a given service type. Include the appropriate `service_type` as a path parameter.<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation is beta. Call it using the `v4beta` path in its URL.<br />&gt;<br />&gt; - Currently, only the Managed Databases (`dbaas`) service type is supported.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.monitor.dashboards
;
```
</TabItem>
<TabItem value="get_dashboards_all">

__Beta__ Returns all available dashboards.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation is beta. Call it using the `v4beta` path in its URL.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
created,
label,
service_type,
type,
updated,
widgets
FROM linode.monitor.dashboards
;
```
</TabItem>
</Tabs>
