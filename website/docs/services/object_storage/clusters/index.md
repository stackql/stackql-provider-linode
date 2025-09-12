--- 
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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

Creates, updates, deletes, gets or lists a <code>clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.object_storage.clusters" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_object_storage_cluster"
    values={[
        { label: 'get_object_storage_cluster', value: 'get_object_storage_cluster' },
        { label: 'get_object_storage_clusters', value: 'get_object_storage_clusters' }
    ]}
>
<TabItem value="get_object_storage_cluster">

The requested Cluster.

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
    <td>The unique ID for this cluster. (example: us-east-1)</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>The base URL for this cluster, used for connecting with third-party clients. (example: us-east-1.linodeobjects.com)</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>The region where this cluster is located. (example: us-east)</td>
</tr>
<tr>
    <td><CopyableCode code="static_site_domain" /></td>
    <td><code>string</code></td>
    <td>The base URL for this cluster used when hosting static sites. (example: website-us-east-1.linodeobjects.com)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>This cluster's status. (example: available)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_object_storage_clusters">

A paginated list of available clusters.

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
    <td><a href="#get_object_storage_cluster"><CopyableCode code="get_object_storage_cluster" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>__Deprecated__ Returns a single Object Storage cluster.<br /><br />&gt; 📘<br />&gt;<br />&gt; This displays deprecated `clusterId` values that represent regions used with older versions of the API. It's maintained for backward compatibility. Run [Get a region](https://techdocs.akamai.com/linode-api/reference/get-region) instead.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)</td>
</tr>
<tr>
    <td><a href="#get_object_storage_clusters"><CopyableCode code="get_object_storage_clusters" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>__Deprecated__ Returns a paginated list of available Object Storage legacy clusters.<br /><br />&gt; 📘<br />&gt;<br />&gt; This displays deprecated `clusterId` values that represent regions used with older versions of the API. It's maintained for backward compatibility. Run [Get a region](https://techdocs.akamai.com/linode-api/reference/get-region) instead.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)</td>
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
    defaultValue="get_object_storage_cluster"
    values={[
        { label: 'get_object_storage_cluster', value: 'get_object_storage_cluster' },
        { label: 'get_object_storage_clusters', value: 'get_object_storage_clusters' }
    ]}
>
<TabItem value="get_object_storage_cluster">

__Deprecated__ Returns a single Object Storage cluster.<br /><br />&gt; 📘<br />&gt;<br />&gt; This displays deprecated `clusterId` values that represent regions used with older versions of the API. It's maintained for backward compatibility. Run [Get a region](https://techdocs.akamai.com/linode-api/reference/get-region) instead.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)

```sql
SELECT
id,
domain,
region,
static_site_domain,
status
FROM linode.object_storage.clusters
;
```
</TabItem>
<TabItem value="get_object_storage_clusters">

__Deprecated__ Returns a paginated list of available Object Storage legacy clusters.<br /><br />&gt; 📘<br />&gt;<br />&gt; This displays deprecated `clusterId` values that represent regions used with older versions of the API. It's maintained for backward compatibility. Run [Get a region](https://techdocs.akamai.com/linode-api/reference/get-region) instead.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)

```sql
SELECT
data,
page,
pages,
results
FROM linode.object_storage.clusters
;
```
</TabItem>
</Tabs>
