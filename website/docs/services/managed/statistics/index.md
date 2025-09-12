--- 
title: statistics
hide_title: false
hide_table_of_contents: false
keywords:
  - statistics
  - managed
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
<tr><td><b>Id</b></td><td><CopyableCode code="linode.managed.statistics" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_managed_stats"
    values={[
        { label: 'get_managed_stats', value: 'get_managed_stats' }
    ]}
>
<TabItem value="get_managed_stats">

A list of Managed Stats from the last 24 hours.

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
    <td><CopyableCode code="0" /></td>
    <td><code>string</code></td>
    <td> (example: Graphs are not yet available.)</td>
</tr>
<tr>
    <td><CopyableCode code="1" /></td>
    <td><code>string</code></td>
    <td> (example: Graphs are not yet available.)</td>
</tr>
<tr>
    <td><CopyableCode code="2" /></td>
    <td><code>string</code></td>
    <td> (example: Graphs are not yet available.)</td>
</tr>
<tr>
    <td><CopyableCode code="cpu" /></td>
    <td><code>array</code></td>
    <td>CPU usage stats from the last 24 hours.</td>
</tr>
<tr>
    <td><CopyableCode code="disk" /></td>
    <td><code>array</code></td>
    <td>Disk usage stats from the last 24 hours.</td>
</tr>
<tr>
    <td><CopyableCode code="net_in" /></td>
    <td><code>array</code></td>
    <td>Inbound network traffic stats from the last 24 hours.</td>
</tr>
<tr>
    <td><CopyableCode code="net_out" /></td>
    <td><code>array</code></td>
    <td>Outbound network traffic stats from the last 24 hours.</td>
</tr>
<tr>
    <td><CopyableCode code="swap" /></td>
    <td><code>array</code></td>
    <td>Swap usage stats from the last 24 hours.</td>
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
    <td><a href="#get_managed_stats"><CopyableCode code="get_managed_stats" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns a list of Managed Stats on your Account in the form of x and y data points. You can use these data points to plot your own graph visualizations. These stats reflect the last 24 hours of combined usage across all managed Linodes on your account giving you a high-level snapshot of data for the following:<br /><br />- cpu<br />- disk<br />- swap<br />- network in<br />- network out<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_managed_stats"
    values={[
        { label: 'get_managed_stats', value: 'get_managed_stats' }
    ]}
>
<TabItem value="get_managed_stats">

Returns a list of Managed Stats on your Account in the form of x and y data points. You can use these data points to plot your own graph visualizations. These stats reflect the last 24 hours of combined usage across all managed Linodes on your account giving you a high-level snapshot of data for the following:<br /><br />- cpu<br />- disk<br />- swap<br />- network in<br />- network out<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
0,
1,
2,
cpu,
disk,
net_in,
net_out,
swap
FROM linode.managed.statistics
;
```
</TabItem>
</Tabs>
