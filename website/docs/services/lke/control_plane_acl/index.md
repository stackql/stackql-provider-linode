--- 
title: control_plane_acl
hide_title: false
hide_table_of_contents: false
keywords:
  - control_plane_acl
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

Creates, updates, deletes, gets or lists a <code>control_plane_acl</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>control_plane_acl</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.lke.control_plane_acl" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_lke_cluster_acl"
    values={[
        { label: 'get_lke_cluster_acl', value: 'get_lke_cluster_acl' }
    ]}
>
<TabItem value="get_lke_cluster_acl">

Returns a single cluster's control plane access control list. The optional field `revision-id` provided will be reflected on GET response when (and only after) the ACL stanza is verified as enforced.

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
    <td><CopyableCode code="addresses" /></td>
    <td><code>object</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="revision-id" /></td>
    <td><code></code></td>
    <td></td>
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
    <td><a href="#get_lke_cluster_acl"><CopyableCode code="get_lke_cluster_acl" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a specific cluster's control plane access control List.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_lke_cluster_acl"><CopyableCode code="put_lke_cluster_acl" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Updates a specific cluster's control plane access control list.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_lke_cluster_acl"><CopyableCode code="delete_lke_cluster_acl" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Disable control plane access controls and deletes all rules. This has the same effect as calling `PUT` with an acl json map value of `&#123;“enabled” : false&#125;`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_lke_cluster_acl"
    values={[
        { label: 'get_lke_cluster_acl', value: 'get_lke_cluster_acl' }
    ]}
>
<TabItem value="get_lke_cluster_acl">

Get a specific cluster's control plane access control List.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
addresses,
revision-id
FROM linode.lke.control_plane_acl
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_lke_cluster_acl"
    values={[
        { label: 'put_lke_cluster_acl', value: 'put_lke_cluster_acl' }
    ]}
>
<TabItem value="put_lke_cluster_acl">

Updates a specific cluster's control plane access control list.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.lke.control_plane_acl
SET 
data__acl = '{{ acl }}'
RETURNING
acl;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_lke_cluster_acl"
    values={[
        { label: 'delete_lke_cluster_acl', value: 'delete_lke_cluster_acl' }
    ]}
>
<TabItem value="delete_lke_cluster_acl">

Disable control plane access controls and deletes all rules. This has the same effect as calling `PUT` with an acl json map value of `&#123;“enabled” : false&#125;`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.lke.control_plane_acl
;
```
</TabItem>
</Tabs>
