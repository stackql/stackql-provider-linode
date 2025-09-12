--- 
title: statistics
hide_title: false
hide_table_of_contents: false
keywords:
  - statistics
  - nodebalancers
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

Creates, updates, deletes, gets or lists a <code>statistics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>statistics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.nodebalancers.statistics" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_node_balancer_stats"
    values={[
        { label: 'get_node_balancer_stats', value: 'get_node_balancer_stats' }
    ]}
>
<TabItem value="get_node_balancer_stats">

The requested stats.

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
    <td><code>object</code></td>
    <td>The data returned about this NodeBalancers.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>The title for the statistics generated in this response. (example: linode.com - balancer12345 (12345) - day (5 min avg))</td>
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
    <td><a href="#get_node_balancer_stats"><CopyableCode code="get_node_balancer_stats" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns detailed statistics about the requested NodeBalancer. __OAuth scopes__.<br /><br />    ```<br />    nodebalancers:read_only<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_node_balancer_stats"
    values={[
        { label: 'get_node_balancer_stats', value: 'get_node_balancer_stats' }
    ]}
>
<TabItem value="get_node_balancer_stats">

Returns detailed statistics about the requested NodeBalancer. __OAuth scopes__.<br /><br />    ```<br />    nodebalancers:read_only<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
title
FROM linode.nodebalancers.statistics
;
```
</TabItem>
</Tabs>
