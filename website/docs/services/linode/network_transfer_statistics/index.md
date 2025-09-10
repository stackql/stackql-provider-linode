--- 
title: network_transfer_statistics
hide_title: false
hide_table_of_contents: false
keywords:
  - network_transfer_statistics
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

Creates, updates, deletes, gets or lists a <code>network_transfer_statistics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_transfer_statistics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.linode.network_transfer_statistics" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_linode_transfer_by_year_month"
    values={[
        { label: 'get_linode_transfer_by_year_month', value: 'get_linode_transfer_by_year_month' }
    ]}
>
<TabItem value="get_linode_transfer_by_year_month">

A collection of the specified Linode's network transfer statistics for the requested month.

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
    <td><CopyableCode code="bytes_in" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The amount of inbound public network traffic received by this Linode, in bytes, for a specific year/month.</td>
</tr>
<tr>
    <td><CopyableCode code="bytes_out" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The amount of outbound public network traffic sent by this Linode, in bytes, for a specific year/month.</td>
</tr>
<tr>
    <td><CopyableCode code="bytes_total" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The total amount of public network traffic sent and received by this Linode, in bytes, for a specific year/month.</td>
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
    <td><a href="#get_linode_transfer_by_year_month"><CopyableCode code="get_linode_transfer_by_year_month" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns a Linode's network transfer statistics for a specific month. The year/month values must be either a date in the past, or the current month. __OAuth scopes__.<br /><br />    ```<br />    linodes:read_only<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_linode_transfer_by_year_month"
    values={[
        { label: 'get_linode_transfer_by_year_month', value: 'get_linode_transfer_by_year_month' }
    ]}
>
<TabItem value="get_linode_transfer_by_year_month">

Returns a Linode's network transfer statistics for a specific month. The year/month values must be either a date in the past, or the current month. __OAuth scopes__.<br /><br />    ```<br />    linodes:read_only<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
bytes_in,
bytes_out,
bytes_total
FROM linode.linode.network_transfer_statistics;
```
</TabItem>
</Tabs>
