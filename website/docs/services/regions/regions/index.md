--- 
title: regions
hide_title: false
hide_table_of_contents: false
keywords:
  - regions
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

Creates, updates, deletes, gets or lists a <code>regions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>regions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.regions.regions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_region"
    values={[
        { label: 'get_region', value: 'get_region' },
        { label: 'get_regions', value: 'get_regions' }
    ]}
>
<TabItem value="get_region">

A single Region object.

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
    <td><code>string</code></td>
    <td>The unique ID of this Region. (example: us-east)</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>array</code></td>
    <td>A list of capabilities of this region.</td>
</tr>
<tr>
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The country where this region resides. (example: us)</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>Detailed location information for this region, including city, state or region, and country. (example: Newark, NJ, USA)</td>
</tr>
<tr>
    <td><CopyableCode code="monitors" /></td>
    <td><code>object</code></td>
    <td>__Beta__ Lists the services in this region that support metrics and alerts use with Akamai Cloud Pulse (ACLP).  &gt; 📘 &gt; &gt; The ACLP service is currently beta. This object is only returned in a response if you're participating in the ACLP beta. Contact your account team for more information.</td>
</tr>
<tr>
    <td><CopyableCode code="placement_group_limits" /></td>
    <td><code>object</code></td>
    <td>The limits for [placement groups](https://www.linode.com/docs/products/compute/compute-instances/guides/placement-groups/) in this region.</td>
</tr>
<tr>
    <td><CopyableCode code="resolvers" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="site_type" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ This region's site type. A `core` region indicates a traditional cloud computing [region](https://www.linode.com/docs/products/platform/get-started/guides/choose-a-data-center/#product-availability) that offers all compute services. A `distributed` region indicates sites that are globally dispersed to be closer to end users and workloads. These regions offer limited services. (example: core)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>This region's current operational status. (example: ok)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_regions">

Returns an array of regions.

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
    <td><a href="#get_region"><CopyableCode code="get_region" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns a single Region.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)</td>
</tr>
<tr>
    <td><a href="#get_regions"><CopyableCode code="get_regions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Lists the regions available for Linode services. Not all services are guaranteed to be available in all regions.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)</td>
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
    defaultValue="get_region"
    values={[
        { label: 'get_region', value: 'get_region' },
        { label: 'get_regions', value: 'get_regions' }
    ]}
>
<TabItem value="get_region">

Returns a single Region.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)

```sql
SELECT
id,
capabilities,
country,
label,
monitors,
placement_group_limits,
resolvers,
site_type,
status
FROM linode.regions.regions;
```
</TabItem>
<TabItem value="get_regions">

Lists the regions available for Linode services. Not all services are guaranteed to be available in all regions.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)

```sql
SELECT
data,
page,
pages,
results
FROM linode.regions.regions;
```
</TabItem>
</Tabs>
