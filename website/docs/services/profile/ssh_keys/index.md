--- 
title: ssh_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - ssh_keys
  - profile
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

Creates, updates, deletes, gets or lists a <code>ssh_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ssh_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.profile.ssh_keys" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_ssh_key"
    values={[
        { label: 'get_ssh_key', value: 'get_ssh_key' },
        { label: 'get_ssh_keys', value: 'get_ssh_keys' }
    ]}
>
<TabItem value="get_ssh_key">

An SSH Key object.

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
    <td><code>integer</code></td>
    <td>__Read-only__ The unique identifier of an SSH Key object.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ The date this key was added. (example: 2018-01-01T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>A label for the SSH Key. (example: My SSH Key)</td>
</tr>
<tr>
    <td><CopyableCode code="ssh_key" /></td>
    <td><code>string (ssh-key)</code></td>
    <td>The public SSH Key, which is used to authenticate to the root user of the Linodes you deploy.  Accepted formats:  - ssh-dss - ssh-rsa - ecdsa-sha2-nistp - ssh-ed25519 - sk-ecdsa-sha2-nistp256 (Akamai-specific) (example: ssh-rsa AAAA_valid_public_ssh_key_123456785== user@their-computer)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_ssh_keys">

Returns a paginated list of SSH Key objects.

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
    <td><a href="#get_ssh_key"><CopyableCode code="get_ssh_key" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns a single SSH Key object identified by `id` that you have access to view.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_ssh_keys"><CopyableCode code="get_ssh_keys" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Returns a collection of SSH Keys you've added to your Profile.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_add_ssh_key"><CopyableCode code="post_add_ssh_key" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Adds an SSH Key to your Account profile.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_ssh_key"><CopyableCode code="put_ssh_key" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Updates an SSH Key that you have permission to `read_write`.<br /><br />Only SSH key labels can be updated.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_ssh_key"><CopyableCode code="delete_ssh_key" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes an SSH Key you have access to.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation only deletes a key's association from your profile. It doesn't remove it from any Linode or disk that was deployed with `authorized_keys`. You need to manually delete the key on the Linode or disk.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer</code></td>
    <td>The page of a collection to return.</td>
</tr>
<tr id="parameter-page_size">
    <td><CopyableCode code="page_size" /></td>
    <td><code>integer</code></td>
    <td>The number of items to return per page.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_ssh_key"
    values={[
        { label: 'get_ssh_key', value: 'get_ssh_key' },
        { label: 'get_ssh_keys', value: 'get_ssh_keys' }
    ]}
>
<TabItem value="get_ssh_key">

Returns a single SSH Key object identified by `id` that you have access to view.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
created,
label,
ssh_key
FROM linode.profile.ssh_keys;
```
</TabItem>
<TabItem value="get_ssh_keys">

Returns a collection of SSH Keys you've added to your Profile.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.profile.ssh_keys
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}';
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_add_ssh_key"
    values={[
        { label: 'post_add_ssh_key', value: 'post_add_ssh_key' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_add_ssh_key">

Adds an SSH Key to your Account profile.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.profile.ssh_keys (
data__label,
data__ssh_key
)
SELECT 
'{{ label }}',
'{{ ssh_key }}'
RETURNING
id,
created,
label,
ssh_key
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: ssh_keys
  props:
    - name: label
      value: string
      description: >
        A label for the SSH Key.
        
    - name: ssh_key
      value: string
      description: >
        The public SSH Key, which is used to authenticate to the root user of the Linodes you deploy.

Accepted formats:

- ssh-dss
- ssh-rsa
- ecdsa-sha2-nistp
- ssh-ed25519
- sk-ecdsa-sha2-nistp256 (Akamai-specific)
        
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_ssh_key"
    values={[
        { label: 'put_ssh_key', value: 'put_ssh_key' }
    ]}
>
<TabItem value="put_ssh_key">

Updates an SSH Key that you have permission to `read_write`.<br /><br />Only SSH key labels can be updated.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.profile.ssh_keys
SET 
data__label = '{{ label }}'
WHERE 

RETURNING
id,
created,
label,
ssh_key;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_ssh_key"
    values={[
        { label: 'delete_ssh_key', value: 'delete_ssh_key' }
    ]}
>
<TabItem value="delete_ssh_key">

Deletes an SSH Key you have access to.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation only deletes a key's association from your profile. It doesn't remove it from any Linode or disk that was deployed with `authorized_keys`. You need to manually delete the key on the Linode or disk.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.profile.ssh_keys;
```
</TabItem>
</Tabs>
