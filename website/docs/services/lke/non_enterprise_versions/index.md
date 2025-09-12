--- 
title: non_enterprise_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - non_enterprise_versions
  - lke
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

Creates, updates, deletes, gets or lists a <code>non_enterprise_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>non_enterprise_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.lke.non_enterprise_versions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_lke_version"
    values={[
        { label: 'get_lke_version', value: 'get_lke_version' },
        { label: 'get_lke_versions', value: 'get_lke_versions' }
    ]}
>
<TabItem value="get_lke_version">

Returns an LKE Kubernetes version object available for deployment to a standard tier Kubernetes cluster.

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
    <td>__Read-only__ A Kubernetes version number available for deployment to a Kubernetes cluster in the format of &lt;major&gt;.&lt;minor&gt;, and the latest supported patch version. (example: 1.31)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_lke_versions">

Returns a list of LKE Kubernetes versions available for deployment to a standard-tier Kubernetes cluster.

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
    <td>__Read-only__ LKE versions for standard tier.</td>
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
    <td><a href="#get_lke_version"><CopyableCode code="get_lke_version" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>View an LKE Kubernetes version available for deployment to a standard tier Kubernetes cluster.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_lke_versions"><CopyableCode code="get_lke_versions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>List LKE Kubernetes versions available for deployment to a standard-tier Kubernetes cluster.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_lke_version"
    values={[
        { label: 'get_lke_version', value: 'get_lke_version' },
        { label: 'get_lke_versions', value: 'get_lke_versions' }
    ]}
>
<TabItem value="get_lke_version">

View an LKE Kubernetes version available for deployment to a standard tier Kubernetes cluster.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id
FROM linode.lke.non_enterprise_versions
;
```
</TabItem>
<TabItem value="get_lke_versions">

List LKE Kubernetes versions available for deployment to a standard-tier Kubernetes cluster.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.lke.non_enterprise_versions
;
```
</TabItem>
</Tabs>
