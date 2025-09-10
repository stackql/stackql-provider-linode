--- 
title: network_transfers
hide_title: false
hide_table_of_contents: false
keywords:
  - network_transfers
  - linode
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

Creates, updates, deletes, gets or lists a <code>network_transfers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_transfers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.linode.network_transfers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_linode_transfer"
    values={[
        { label: 'get_linode_transfer', value: 'get_linode_transfer' }
    ]}
>
<TabItem value="get_linode_transfer">

A collection of the specified Linode's network transfer statistics.

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
    <td><CopyableCode code="billable" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The amount of network transfer this Linode has used, in GB, past your monthly quota.</td>
</tr>
<tr>
    <td><CopyableCode code="quota" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The amount of network transfer this Linode adds to your transfer pool, in GB, for the current month's billing cycle.</td>
</tr>
<tr>
    <td><CopyableCode code="used" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The amount of network transfer used by this Linode, in bytes, for the current month's billing cycle.</td>
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
    <td><a href="#get_linode_transfer"><CopyableCode code="get_linode_transfer" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns a Linode's network transfer pool statistics for the current month.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_linode_transfer"
    values={[
        { label: 'get_linode_transfer', value: 'get_linode_transfer' }
    ]}
>
<TabItem value="get_linode_transfer">

Returns a Linode's network transfer pool statistics for the current month.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
billable,
quota,
used
FROM linode.linode.network_transfers;
```
</TabItem>
</Tabs>
