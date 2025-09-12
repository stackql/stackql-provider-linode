--- 
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
  - volumes
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

Creates, updates, deletes, gets or lists a <code>volumes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.volumes.volumes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_volume"
    values={[
        { label: 'get_volume', value: 'get_volume' },
        { label: 'get_volumes', value: 'get_volumes' }
    ]}
>
<TabItem value="get_volume">

Returns a single Volume object.

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
    <td>__Read-only__ The unique identifier for the volume.</td>
</tr>
<tr>
    <td><CopyableCode code="linode_id" /></td>
    <td><code>integer</code></td>
    <td>The unique identifier of the Linode this volume is attached to, if applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When this volume was created. (example: 2018-01-01T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ Whether encryption is enabled on this volume. (example: enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="filesystem_path" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The full file system path for the volume, based on its `label`. The path is `/dev/disk/by-id/scsi-0Linode_Volume_label`. (example: /dev/disk/by-id/scsi-0Linode_Volume_my-volume)</td>
</tr>
<tr>
    <td><CopyableCode code="hardware_type" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The storage type of this volume. This can be either `hdd` to emulate a hard disk drive for the volume, or `nvme` to emulate a non-volatile memory express solid state drive. (example: nvme)</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The name of the volume. A `label` can be up to 32 characters long and contain alphanumeric characters, hyphens, and underscores. This value is also used in the volume's `filesystem_path`. (example: my-volume, pattern: <code>^[a-zA-Z]((?!--|__)[a-zA-Z0-9-_])+$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="linode_label" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The name of the Linode this volume is attached to, if applicable. (example: linode123)</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>The unique ID of this Region. (example: us-east)</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>integer</code></td>
    <td>The Volume's size, in GiB.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The current status of the volume. This can be one of:  - `creating`. The API is creating the volume and it's not ready for use.  - `active`. The volume is online and ready for use.  - `resizing`. The volume's capacity is being upgraded.  - `key_rotating`. The volume's encryption keys are being rotated to new values. Requests to resize, delete, or clone a volume fail during encryption key rotation. (example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>__Filterable__ Any tags applied to this object. Use [tags](https://techdocs.akamai.com/linode-api/reference/post-tag) to label and organize your cloud computing resources.</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When this volume was last updated. (example: 2018-01-01T00:01:01)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_volumes">

Returns an array of all Volumes on your Account.

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
    <td><a href="#get_volume"><CopyableCode code="get_volume" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Get information about a single Volume.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_volumes"><CopyableCode code="get_volumes" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Returns a paginated list of Volumes you have permission to view.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_volume"><CopyableCode code="post_volume" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__label"><code>data__label</code></a></td>
    <td></td>
    <td>Creates a volume on your account. For this to complete, you need the `add_volumes` grant. Creating a new volume accrues additional charges on your account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_volume"><CopyableCode code="put_volume" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Updates a Volume that you have permission to `read_write`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_volume"><CopyableCode code="delete_volume" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes a Volume you have permission to `read_write`.<br /><br />- __Deleting a Volume is a destructive action and cannot be undone.__<br /><br />- Deleting stops billing for the Volume. You will be billed for time used within the billing period the Volume was active.<br /><br />- Volumes that are migrating cannot be deleted until the migration is finished.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_attach_volume"><CopyableCode code="post_attach_volume" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-linode_id"><code>linode_id</code></a></td>
    <td></td>
    <td>Attaches a Volume on your Account to an existing Linode on your Account. In order for this request to complete successfully, your User must have `read_write` permission to the Volume and `read_write` permission to the Linode. Additionally, the Volume and Linode must be located in the same Region.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_clone_volume"><CopyableCode code="post_clone_volume" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-label"><code>label</code></a></td>
    <td></td>
    <td>Creates a Volume on your Account. In order for this request to complete successfully, your User must have the `add_volumes` grant. The new Volume will have the same size and data as the source Volume. Creating a new Volume will incur a charge on your Account.<br /><br />- Only Volumes with a `status` of `active` can be cloned.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_detach_volume"><CopyableCode code="post_detach_volume" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Detaches a Volume on your Account from a Linode on your Account. In order for this request to complete successfully, your User must have `read_write` access to the Volume and `read_write` access to the Linode.<br /><br />Volumes are automatically detached from deleted Linodes.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_resize_volume"><CopyableCode code="post_resize_volume" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-size"><code>size</code></a></td>
    <td></td>
    <td>Resize an existing Volume on your Account. In order for this request to complete successfully, your User must have the `read_write` permissions to the Volume.<br /><br />- Volumes can only be resized up.<br />- Only Volumes with a `status` of "active" can be resized.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_volume"
    values={[
        { label: 'get_volume', value: 'get_volume' },
        { label: 'get_volumes', value: 'get_volumes' }
    ]}
>
<TabItem value="get_volume">

Get information about a single Volume.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
linode_id,
created,
encryption,
filesystem_path,
hardware_type,
label,
linode_label,
region,
size,
status,
tags,
updated
FROM linode.volumes.volumes
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}'
;
```
</TabItem>
<TabItem value="get_volumes">

Returns a paginated list of Volumes you have permission to view.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.volumes.volumes
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_volume"
    values={[
        { label: 'post_volume', value: 'post_volume' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_volume">

Creates a volume on your account. For this to complete, you need the `add_volumes` grant. Creating a new volume accrues additional charges on your account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.volumes.volumes (
data__config_id,
data__encryption,
data__label,
data__linode_id,
data__region,
data__size,
data__tags
)
SELECT 
{{ config_id }},
'{{ encryption }}',
'{{ label }}' /* required */,
{{ linode_id }},
'{{ region }}',
{{ size }},
'{{ tags }}'
RETURNING
id,
linode_id,
created,
encryption,
filesystem_path,
hardware_type,
label,
linode_label,
region,
size,
status,
tags,
updated
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: volumes
  props:
    - name: config_id
      value: integer
      description: >
        When creating a volume attached to a Linode, this is the identifier of the Linode configuration profile (config) where the volume will live. Run the [List configuration profiles](https://techdocs.akamai.com/linode-api/reference/get-linode-configs) operation and store the `id` for the applicable config. The following apply when adding a `config_id`:

- The selected config needs to belong to the Linode referenced by `linode_id` in this request.

- You can't provide a `config_id` if you don't also provide a `linode_id` in the request.

- If you send a `linode_id` without a `config_id` in the request, the API attaches the volume to that Linode's last used config, or to the only config in that Linode. If there isn't a config available for attachment, the API returns an error.
        
    - name: encryption
      value: string
      description: >
        Enables encryption on the volume. Full disk encryption ensures the data stored on a block storage volume drive is secure. It protects against unauthorized access by keeping the data encrypted if the volume drive is removed from the data center, decommissioned, or disposed of.

The platform automatically manages the encryption and decryption process for you. You can use an encrypted volume the same way you use a non-encrypted volume.

> 📘
>
> You can enable or disable disk encryption only when creating new block storage volumes. After a volume is created, the encryption setting can't be changed.
        
      valid_values: ['enabled', 'disabled']
      default: disabled
    - name: label
      value: string
      description: >
        The name of the volume. A `label` can be up to 32 characters long and contain alphanumeric characters, hyphens, and underscores. This value is also used in the volume's `filesystem_path`.
        
    - name: linode_id
      value: integer
      description: >
        The Linode this volume should be attached to after it's created. If not given, the volume will be created without an attachment.
        
    - name: region
      value: string
      description: >
        The region where the API deploys the volume. This is only required if you didn't provide a `linode_id` for the volume.
        
    - name: size
      value: integer
      description: >
        The initial size of this volume, in GB. Volumes can only be resized after the creation completes.
        
      default: 20
    - name: tags
      value: array
      description: >
        __Filterable__ Any tags applied to this object. Use [tags](https://techdocs.akamai.com/linode-api/reference/post-tag) to label and organize your cloud computing resources.
        
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_volume"
    values={[
        { label: 'put_volume', value: 'put_volume' }
    ]}
>
<TabItem value="put_volume">

Updates a Volume that you have permission to `read_write`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.volumes.volumes
SET 
data__label = '{{ label }}',
data__region = '{{ region }}',
data__tags = '{{ tags }}'
RETURNING
id,
linode_id,
created,
encryption,
filesystem_path,
hardware_type,
label,
linode_label,
region,
size,
status,
tags,
updated;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_volume"
    values={[
        { label: 'delete_volume', value: 'delete_volume' }
    ]}
>
<TabItem value="delete_volume">

Deletes a Volume you have permission to `read_write`.<br /><br />- __Deleting a Volume is a destructive action and cannot be undone.__<br /><br />- Deleting stops billing for the Volume. You will be billed for time used within the billing period the Volume was active.<br /><br />- Volumes that are migrating cannot be deleted until the migration is finished.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.volumes.volumes
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="post_attach_volume"
    values={[
        { label: 'post_attach_volume', value: 'post_attach_volume' },
        { label: 'post_clone_volume', value: 'post_clone_volume' },
        { label: 'post_detach_volume', value: 'post_detach_volume' },
        { label: 'post_resize_volume', value: 'post_resize_volume' }
    ]}
>
<TabItem value="post_attach_volume">

Attaches a Volume on your Account to an existing Linode on your Account. In order for this request to complete successfully, your User must have `read_write` permission to the Volume and `read_write` permission to the Linode. Additionally, the Volume and Linode must be located in the same Region.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.volumes.volumes.post_attach_volume 
@@json=
'{
"config_id": {{ config_id }}, 
"linode_id": {{ linode_id }}, 
"persist_across_boots": {{ persist_across_boots }}
}'
;
```
</TabItem>
<TabItem value="post_clone_volume">

Creates a Volume on your Account. In order for this request to complete successfully, your User must have the `add_volumes` grant. The new Volume will have the same size and data as the source Volume. Creating a new Volume will incur a charge on your Account.<br /><br />- Only Volumes with a `status` of `active` can be cloned.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.volumes.volumes.post_clone_volume 
@@json=
'{
"label": "{{ label }}"
}'
;
```
</TabItem>
<TabItem value="post_detach_volume">

Detaches a Volume on your Account from a Linode on your Account. In order for this request to complete successfully, your User must have `read_write` access to the Volume and `read_write` access to the Linode.<br /><br />Volumes are automatically detached from deleted Linodes.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.volumes.volumes.post_detach_volume 

;
```
</TabItem>
<TabItem value="post_resize_volume">

Resize an existing Volume on your Account. In order for this request to complete successfully, your User must have the `read_write` permissions to the Volume.<br /><br />- Volumes can only be resized up.<br />- Only Volumes with a `status` of "active" can be resized.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.volumes.volumes.post_resize_volume 
@@json=
'{
"size": {{ size }}
}'
;
```
</TabItem>
</Tabs>
