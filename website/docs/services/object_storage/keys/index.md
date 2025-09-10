--- 
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
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

Creates, updates, deletes, gets or lists a <code>keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.object_storage.keys" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_object_storage_key"
    values={[
        { label: 'get_object_storage_key', value: 'get_object_storage_key' },
        { label: 'get_object_storage_keys', value: 'get_object_storage_keys' }
    ]}
>
<TabItem value="get_object_storage_key">

The key pair.

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
    <td>This Object Storage key's unique ID.</td>
</tr>
<tr>
    <td><CopyableCode code="access_key" /></td>
    <td><code>string</code></td>
    <td>A unique string chosen by the API to identify this key. Used as a username to identify this key when making requests to an S3 API, such as the Amazon S3 API or Ceph Object Gateway S3 API. (example: ABCDEFGHI1JKL2MNOP34)</td>
</tr>
<tr>
    <td><CopyableCode code="bucket_access" /></td>
    <td><code>array</code></td>
    <td>Settings that limit access to specific buckets, each with a specific permission level. See [Create a limited access key](https://techdocs.akamai.com/linode-api/reference/post-object-storage-keys) for more information.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>The label given to this key. For display purposes only. (example: my-key)</td>
</tr>
<tr>
    <td><CopyableCode code="limited" /></td>
    <td><code>boolean</code></td>
    <td>Whether this Object Storage key limits access to specific buckets and permissions. Returns `false` if this key grants full access. Specific limitations are set in `bucket_access`.</td>
</tr>
<tr>
    <td><CopyableCode code="regions" /></td>
    <td><code>array</code></td>
    <td>The key can be used in these regions to manage buckets.</td>
</tr>
<tr>
    <td><CopyableCode code="secret_key" /></td>
    <td><code>string</code></td>
    <td>This Object Storage key's secret key. Used as a password to validate this key when making requests to an S3 API, such as the Amazon S3 API or Ceph Object Gateway S3 API.  &gt; 📘 &gt; &gt; This value is listed as `[REDACTED]` for this operation, to protect it. It's only revealed in a response after [creating](https://techdocs.akamai.com/linode-api/reference/post-object-storage-keys) a key.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_object_storage_keys">

A paginated list of Object Storage Keys.

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
    <td><a href="#get_object_storage_key"><CopyableCode code="get_object_storage_key" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns a single Object Storage key provisioned for your account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_object_storage_keys"><CopyableCode code="get_object_storage_keys" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns a paginated list of Object Storage keys for authentication.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_object_storage_keys"><CopyableCode code="post_object_storage_keys" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Provisions a new Object Storage key for authentication. A successful request triggers an `obj_access_key_create` [event](https://techdocs.akamai.com/linode-api/reference/get-events).<br /><br />&gt; 📘<br />&gt;<br />&gt; Accounts with negative balances can't access this operation.<br /><br />**Create an unlimited access key**<br /><br />This type of key grants full access to all of your buckets in each region you name, using the `regions` array. Run the [List regions](https://techdocs.akamai.com/linode-api/reference/get-regions) operation, verify that each desired region includes `"Object Storage"` among its `capabilities`, and store the `id` value for each. Leave the `bucket_access` array out to create an unlimited access key.<br /><br />Check out this [example workflow](https://techdocs.akamai.com/linode-api/reference/create-an-unlimited-access-key) for an unlimited access key.<br /><br />**Create a limited access key**<br /><br />This type of key lets you name specific buckets where you need to manage content. In the `bucket_access` array, include individual objects for each bucket, comprised of the target `bucket_name`, the `permissions` level for access to the bucket, and the `region` where the bucket lives. Run the [List Object Storage buckets](https://techdocs.akamai.com/linode-api/reference/get-object-storage-buckets) operation and store the `label`, to use as the `bucket_name`, and the `region` for each. With a limited access key, the parent-level `regions` array isn't required.<br /><br />Check out this [example workflow](https://techdocs.akamai.com/linode-api/reference/create-a-limited-access-key) for a limited access key.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_object_storage_key"><CopyableCode code="put_object_storage_key" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Updates an Object Storage key on your account. A successful request triggers an `obj_access_key_update` [event](https://techdocs.akamai.com/linode-api/reference/get-events).<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_object_storage_key"><CopyableCode code="delete_object_storage_key" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Revokes an Object Storage Key. This key pair will no longer be usable by third-party clients. A successful request triggers an `obj_access_key_delete` [event](https://techdocs.akamai.com/linode-api/reference/get-events).<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_object_storage_key"
    values={[
        { label: 'get_object_storage_key', value: 'get_object_storage_key' },
        { label: 'get_object_storage_keys', value: 'get_object_storage_keys' }
    ]}
>
<TabItem value="get_object_storage_key">

Returns a single Object Storage key provisioned for your account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
access_key,
bucket_access,
label,
limited,
regions,
secret_key
FROM linode.object_storage.keys;
```
</TabItem>
<TabItem value="get_object_storage_keys">

Returns a paginated list of Object Storage keys for authentication.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.object_storage.keys;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_object_storage_keys"
    values={[
        { label: 'post_object_storage_keys', value: 'post_object_storage_keys' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_object_storage_keys">

Provisions a new Object Storage key for authentication. A successful request triggers an `obj_access_key_create` [event](https://techdocs.akamai.com/linode-api/reference/get-events).<br /><br />&gt; 📘<br />&gt;<br />&gt; Accounts with negative balances can't access this operation.<br /><br />**Create an unlimited access key**<br /><br />This type of key grants full access to all of your buckets in each region you name, using the `regions` array. Run the [List regions](https://techdocs.akamai.com/linode-api/reference/get-regions) operation, verify that each desired region includes `"Object Storage"` among its `capabilities`, and store the `id` value for each. Leave the `bucket_access` array out to create an unlimited access key.<br /><br />Check out this [example workflow](https://techdocs.akamai.com/linode-api/reference/create-an-unlimited-access-key) for an unlimited access key.<br /><br />**Create a limited access key**<br /><br />This type of key lets you name specific buckets where you need to manage content. In the `bucket_access` array, include individual objects for each bucket, comprised of the target `bucket_name`, the `permissions` level for access to the bucket, and the `region` where the bucket lives. Run the [List Object Storage buckets](https://techdocs.akamai.com/linode-api/reference/get-object-storage-buckets) operation and store the `label`, to use as the `bucket_name`, and the `region` for each. With a limited access key, the parent-level `regions` array isn't required.<br /><br />Check out this [example workflow](https://techdocs.akamai.com/linode-api/reference/create-a-limited-access-key) for a limited access key.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.object_storage.keys (

)
SELECT 

RETURNING
id,
access_key,
bucket_access,
label,
limited,
regions,
secret_key
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: keys
  props:
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_object_storage_key"
    values={[
        { label: 'put_object_storage_key', value: 'put_object_storage_key' }
    ]}
>
<TabItem value="put_object_storage_key">

Updates an Object Storage key on your account. A successful request triggers an `obj_access_key_update` [event](https://techdocs.akamai.com/linode-api/reference/get-events).<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.object_storage.keys
SET 
data__label = '{{ label }}',
data__regions = '{{ regions }}'
WHERE 

RETURNING
id,
access_key,
label,
limited,
regions,
secret_key;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_object_storage_key"
    values={[
        { label: 'delete_object_storage_key', value: 'delete_object_storage_key' }
    ]}
>
<TabItem value="delete_object_storage_key">

Revokes an Object Storage Key. This key pair will no longer be usable by third-party clients. A successful request triggers an `obj_access_key_delete` [event](https://techdocs.akamai.com/linode-api/reference/get-events).<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.object_storage.keys;
```
</TabItem>
</Tabs>
