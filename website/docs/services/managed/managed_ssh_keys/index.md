--- 
title: managed_ssh_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_ssh_keys
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

Creates, updates, deletes, gets or lists a <code>managed_ssh_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_ssh_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.managed.managed_ssh_keys" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_managed_ssh_key"
    values={[
        { label: 'get_managed_ssh_key', value: 'get_managed_ssh_key' }
    ]}
>
<TabItem value="get_managed_ssh_key">

The requested Managed SSH public key.

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
    <td><CopyableCode code="ssh_key" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The unique SSH public key assigned to your Linode account's Managed service. (example: ssh-rsa AAAAB...oD2ZQ== managedservices@linode)</td>
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
    <td><a href="#get_managed_ssh_key"><CopyableCode code="get_managed_ssh_key" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns the unique SSH public key assigned to your Linode account's Managed service. If you [add this public key](https://www.linode.com/docs/products/services/managed/get-started/#adding-the-public-key) to a Linode on your account, Linode special forces will be able to log in to the Linode with this key when attempting to resolve issues.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_managed_ssh_key"
    values={[
        { label: 'get_managed_ssh_key', value: 'get_managed_ssh_key' }
    ]}
>
<TabItem value="get_managed_ssh_key">

Returns the unique SSH public key assigned to your Linode account's Managed service. If you [add this public key](https://www.linode.com/docs/products/services/managed/get-started/#adding-the-public-key) to a Linode on your account, Linode special forces will be able to log in to the Linode with this key when attempting to resolve issues.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
ssh_key
FROM linode.managed.managed_ssh_keys
;
```
</TabItem>
</Tabs>
