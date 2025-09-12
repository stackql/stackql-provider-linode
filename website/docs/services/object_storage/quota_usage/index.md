--- 
title: quota_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - quota_usage
  - object_storage
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

Creates, updates, deletes, gets or lists a <code>quota_usage</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>quota_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.object_storage.quota_usage" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_object_storage_quota_usage"
    values={[
        { label: 'get_object_storage_quota_usage', value: 'get_object_storage_quota_usage' }
    ]}
>
<TabItem value="get_object_storage_quota_usage">

Usage data for the specified `object-storage-quotaId`.

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
    <td><CopyableCode code="quota_limit" /></td>
    <td><code>integer</code></td>
    <td>The availability limit for a specific Object Storage resource (`object-storage-quotaId`) for a single endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="usage" /></td>
    <td><code>integer</code></td>
    <td>The quantity of the Object Storage resource currently in use on an endpoint. Displayed as `null` if no resources are in use.</td>
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
    <td><a href="#get_object_storage_quota_usage"><CopyableCode code="get_object_storage_quota_usage" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns usage data for a specific `object-storage-quotaId`. This includes the maximum number of `object-storage-quotaId` resources you can have for a single endpoint and the current usage for that resource.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_object_storage_quota_usage"
    values={[
        { label: 'get_object_storage_quota_usage', value: 'get_object_storage_quota_usage' }
    ]}
>
<TabItem value="get_object_storage_quota_usage">

Returns usage data for a specific `object-storage-quotaId`. This includes the maximum number of `object-storage-quotaId` resources you can have for a single endpoint and the current usage for that resource.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
quota_limit,
usage
FROM linode.object_storage.quota_usage
;
```
</TabItem>
</Tabs>
