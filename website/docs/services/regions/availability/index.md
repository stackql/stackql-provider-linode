--- 
title: availability
hide_title: false
hide_table_of_contents: false
keywords:
  - availability
  - regions
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

Creates, updates, deletes, gets or lists an <code>availability</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>availability</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.regions.availability" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_region_availability"
    values={[
        { label: 'get_region_availability', value: 'get_region_availability' },
        { label: 'get_regions_availability', value: 'get_regions_availability' }
    ]}
>
<TabItem value="get_region_availability">

The availability data for a single Region.

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
    <td><CopyableCode code="available" /></td>
    <td><code>boolean</code></td>
    <td>__Filterable__ Whether the compute instance type is available in the region.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The compute instance [Type](https://techdocs.akamai.com/linode-api/reference/get-linode-types) ID. (example: gpu-rtx6000-1.1)</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The [Region](https://techdocs.akamai.com/linode-api/reference/get-regions) ID. (example: us-east)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_regions_availability">

Returns a Region Availability object.

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
    <td><CopyableCode code="available" /></td>
    <td><code>boolean</code></td>
    <td>__Filterable__ Whether the compute instance type is available in the region.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The compute instance [Type](https://techdocs.akamai.com/linode-api/reference/get-linode-types) ID. (example: gpu-rtx6000-1.1)</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The [Region](https://techdocs.akamai.com/linode-api/reference/get-regions) ID. (example: us-east)</td>
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
    <td><a href="#get_region_availability"><CopyableCode code="get_region_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns availability data for a single Region.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)</td>
</tr>
<tr>
    <td><a href="#get_regions_availability"><CopyableCode code="get_regions_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns availability data for all regions.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)</td>
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
    defaultValue="get_region_availability"
    values={[
        { label: 'get_region_availability', value: 'get_region_availability' },
        { label: 'get_regions_availability', value: 'get_regions_availability' }
    ]}
>
<TabItem value="get_region_availability">

Returns availability data for a single Region.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)

```sql
SELECT
available,
plan,
region
FROM linode.regions.availability;
```
</TabItem>
<TabItem value="get_regions_availability">

Returns availability data for all regions.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)

```sql
SELECT
available,
plan,
region
FROM linode.regions.availability;
```
</TabItem>
</Tabs>
