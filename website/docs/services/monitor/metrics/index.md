--- 
title: metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics
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

Creates, updates, deletes, gets or lists a <code>metrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.monitor.metrics" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_monitor_information"
    values={[
        { label: 'get_monitor_information', value: 'get_monitor_information' }
    ]}
>
<TabItem value="get_monitor_information">

Returns a paginated list of metric information.

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
    <td>The current [page](https://techdocs.akamai.com/linode-api/reference/pagination).</td>
</tr>
<tr>
    <td><CopyableCode code="pages" /></td>
    <td><code>integer</code></td>
    <td>The total number of [pages](https://techdocs.akamai.com/linode-api/reference/pagination).</td>
</tr>
<tr>
    <td><CopyableCode code="results" /></td>
    <td><code>integer</code></td>
    <td>The total number of results.</td>
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
    <td><a href="#get_monitor_information"><CopyableCode code="get_monitor_information" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-X-Filter"><code>X-Filter</code></a></td>
    <td>__Beta__ Returns metrics for a specific service type. Include the appropriate `service_type` as a path parameter.<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation is beta. Call it using the `v4beta` path in its URL.<br />&gt;<br />&gt; - Currently, only the Managed Databases (`dbaas`) service type is supported.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_read_metric"><CopyableCode code="post_read_metric" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>__Beta__ Returns metrics information for the individual entities within a specific service type. Include the appropriate `service_type` as a path parameter. Requires an `authorization: Bearer` [token](https://techdocs.akamai.com/linode-api/reference/post-get-token) you've created for this `service_type`.<br /><br />&gt; 📘<br />&gt;<br />&gt; - Currently, only the Managed Databases (`dbaas`) service type is supported.<br />&gt;<br />&gt; - This operation uses a different URL and version from standard Linode API operations. Verify you're using the URL with the `monitor-api.linode.com` hostname and include `v2beta` as the version in the URL.</td>
</tr>
<tr>
    <td><a href="#post_get_token"><CopyableCode code="post_get_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-entity_ids"><code>entity_ids</code></a></td>
    <td></td>
    <td>__Beta__ Returns a token that authenticates requests for the entities within a specific service type. Include the appropriate `service_type` as a path parameter. The token has a lifetime of six hours after you create it. For an example of the token generation process, see [Monitor API operation authentication](https://techdocs.akamai.com/linode-api/docs/get-started#monitor-api-operation-authentication).<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation is beta. Call it using the `v4beta` path in its URL.<br />&gt;<br />&gt; - Currently, only the Managed Databases (`dbaas`) service type is supported.<br />&gt;<br />&gt; - You also need `read_only` access to the [scope](https://techdocs.akamai.com/linode-api/reference/get-started#oauth-reference) for the selected `service_type`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
<tr id="parameter-X-Filter">
    <td><CopyableCode code="X-Filter" /></td>
    <td><code>object</code></td>
    <td>Specifies a JSON object to filter down the results. See [Filtering and sorting](filtering-and-sorting) for details. (example: &#123;&#123;X-Filter&#125;&#125;)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_monitor_information"
    values={[
        { label: 'get_monitor_information', value: 'get_monitor_information' }
    ]}
>
<TabItem value="get_monitor_information">

__Beta__ Returns metrics for a specific service type. Include the appropriate `service_type` as a path parameter.<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation is beta. Call it using the `v4beta` path in its URL.<br />&gt;<br />&gt; - Currently, only the Managed Databases (`dbaas`) service type is supported.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.monitor.metrics
WHERE X-Filter = '{{ X-Filter }}';
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="post_read_metric"
    values={[
        { label: 'post_read_metric', value: 'post_read_metric' },
        { label: 'post_get_token', value: 'post_get_token' }
    ]}
>
<TabItem value="post_read_metric">

__Beta__ Returns metrics information for the individual entities within a specific service type. Include the appropriate `service_type` as a path parameter. Requires an `authorization: Bearer` [token](https://techdocs.akamai.com/linode-api/reference/post-get-token) you've created for this `service_type`.<br /><br />&gt; 📘<br />&gt;<br />&gt; - Currently, only the Managed Databases (`dbaas`) service type is supported.<br />&gt;<br />&gt; - This operation uses a different URL and version from standard Linode API operations. Verify you're using the URL with the `monitor-api.linode.com` hostname and include `v2beta` as the version in the URL.

```sql
EXEC linode.monitor.metrics.post_read_metric 
;
```
</TabItem>
<TabItem value="post_get_token">

__Beta__ Returns a token that authenticates requests for the entities within a specific service type. Include the appropriate `service_type` as a path parameter. The token has a lifetime of six hours after you create it. For an example of the token generation process, see [Monitor API operation authentication](https://techdocs.akamai.com/linode-api/docs/get-started#monitor-api-operation-authentication).<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation is beta. Call it using the `v4beta` path in its URL.<br />&gt;<br />&gt; - Currently, only the Managed Databases (`dbaas`) service type is supported.<br />&gt;<br />&gt; - You also need `read_only` access to the [scope](https://techdocs.akamai.com/linode-api/reference/get-started#oauth-reference) for the selected `service_type`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.monitor.metrics.post_get_token 
@@json=
'{
"entity_ids": "{{ entity_ids }}"
}';
```
</TabItem>
</Tabs>
