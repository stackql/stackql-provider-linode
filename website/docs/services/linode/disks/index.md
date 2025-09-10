--- 
title: disks
hide_title: false
hide_table_of_contents: false
keywords:
  - disks
  - linode
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

Creates, updates, deletes, gets or lists a <code>disks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.linode.disks" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_linode_disk"
    values={[
        { label: 'get_linode_disk', value: 'get_linode_disk' },
        { label: 'get_linode_disks', value: 'get_linode_disks' }
    ]}
>
<TabItem value="get_linode_disk">

Returns a single Disk object.

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
    <td>__Read-only__ This disk's ID. You need this value to run other operations that interact with the disk.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When this disk was created. (example: 2018-01-01T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="disk_encryption" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ Displays if encryption is enabled on this disk. This setting is based on the `disk_encryption` setting of the Linode. (default: enabled, example: disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="filesystem" /></td>
    <td><code>string</code></td>
    <td>The disk's format or file system. A value of `raw` indicates no file system, just a raw binary stream. A value of `swap` indicates a Linux swap area. The values `ext3` or `ext4` represent these Linux journaling file systems. The value `ext2` is the deprecated ext2 Linux file system. Finally, `initrd` indicates the disk is formatted as an uncompressed initial RAM disk.  &gt; 📘 &gt; &gt; The `ext2` file system doesn't properly support timestamps and will be removed from Linux support in the near future. Also, `initrd` is a legacy format that no longer applies to most use cases. As a best practice, use the other supported formats or file systems instead. (example: ext4)</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The name of the disk. This is for display purposes only. (example: Debian 9 Disk)</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>integer</code></td>
    <td>__Filterable__ The size of the disk in MB.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The current state of the disk. (example: ready)</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When this disk was last updated. (example: 2018-01-01T00:01:01)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_linode_disks">

Returns a paginated list of disks associated with this Linode.

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
    <td><a href="#get_linode_disk"><CopyableCode code="get_linode_disk" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>View Disk information for a Disk associated with this Linode.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_linode_disks"><CopyableCode code="get_linode_disks" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>View Disk information for Disks associated with this Linode.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_add_linode_disk"><CopyableCode code="post_add_linode_disk" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__size"><code>data__size</code></a></td>
    <td></td>
    <td>Add a new disk to an existing Linode. You can create an empty disk to manually configure it later. You can also target a stored `image` to build the disk using a pre-configured file system.<br /><br />- A Linode can have up to 50 disks.<br /><br />- When creating an empty disk, you need to provide a `label` for it. If you don't include a `label`, you need to target an `image` instead.<br /><br />- When you create a disk from an `image`, you need to set a `root_pass` for the disk.<br /><br />- The default file system for a new disk is `ext4`. If you're creating one from an `image`, the disk inherits the file system of that `image`, is unless you specify otherwise.<br /><br />- When you deploy a StackScript on a disk:<br /><br />  - You can run [List StackScripts](https://techdocs.akamai.com/linode-api/reference/get-stack-scripts) to review available StackScripts.<br /><br />  - You need to include a compatible `image` when creating the disk. Run [Get a StackScript](https://techdocs.akamai.com/linode-api/reference/get-stack-script) to review compatible images.<br /><br />  - You should supply SSH keys for the disk's root user, using the `authorized_keys` field.<br /><br />  - You can include individual users via the `authorized_users` field. Before you can add a user, it needs an SSH key assigned to its profile. See [Add an SSH key](https://techdocs.akamai.com/linode-api/reference/post-add-ssh-key) for more information.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_disk"><CopyableCode code="put_disk" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Updates a Disk that you have permission to `read_write`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_disk"><CopyableCode code="delete_disk" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes a Disk you have permission to `read_write`.<br /><br />__Deleting a Disk is a destructive action and cannot be undone.__<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_clone_linode_disk"><CopyableCode code="post_clone_linode_disk" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Copies a disk, byte-for-byte, into a new disk on the same Linode. The operation fails if the target doesn't have enough storage space. A Linode can have up to 50 disks.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_reset_disk_password"><CopyableCode code="post_reset_disk_password" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-password"><code>password</code></a></td>
    <td></td>
    <td>Resets the password of a Disk you have permission to `read_write`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_resize_disk"><CopyableCode code="post_resize_disk" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-size"><code>size</code></a></td>
    <td></td>
    <td>Resizes a Disk you have permission to `read_write`.<br /><br />The Disk must not be in use. If the Disk is in use, the request will succeed but the resize will ultimately fail. For a request to succeed, the Linode must be shut down prior to resizing the Disk, or the Disk must not be assigned to the Linode's active Configuration Profile.<br /><br />If you are resizing the Disk to a smaller size, it cannot be made smaller than what is required by the total size of the files current on the Disk.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_linode_disk"
    values={[
        { label: 'get_linode_disk', value: 'get_linode_disk' },
        { label: 'get_linode_disks', value: 'get_linode_disks' }
    ]}
>
<TabItem value="get_linode_disk">

View Disk information for a Disk associated with this Linode.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
created,
disk_encryption,
filesystem,
label,
size,
status,
updated
FROM linode.linode.disks;
```
</TabItem>
<TabItem value="get_linode_disks">

View Disk information for Disks associated with this Linode.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.linode.disks
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}';
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_add_linode_disk"
    values={[
        { label: 'post_add_linode_disk', value: 'post_add_linode_disk' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_add_linode_disk">

Add a new disk to an existing Linode. You can create an empty disk to manually configure it later. You can also target a stored `image` to build the disk using a pre-configured file system.<br /><br />- A Linode can have up to 50 disks.<br /><br />- When creating an empty disk, you need to provide a `label` for it. If you don't include a `label`, you need to target an `image` instead.<br /><br />- When you create a disk from an `image`, you need to set a `root_pass` for the disk.<br /><br />- The default file system for a new disk is `ext4`. If you're creating one from an `image`, the disk inherits the file system of that `image`, is unless you specify otherwise.<br /><br />- When you deploy a StackScript on a disk:<br /><br />  - You can run [List StackScripts](https://techdocs.akamai.com/linode-api/reference/get-stack-scripts) to review available StackScripts.<br /><br />  - You need to include a compatible `image` when creating the disk. Run [Get a StackScript](https://techdocs.akamai.com/linode-api/reference/get-stack-script) to review compatible images.<br /><br />  - You should supply SSH keys for the disk's root user, using the `authorized_keys` field.<br /><br />  - You can include individual users via the `authorized_users` field. Before you can add a user, it needs an SSH key assigned to its profile. See [Add an SSH key](https://techdocs.akamai.com/linode-api/reference/post-add-ssh-key) for more information.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.linode.disks (
data__authorized_keys,
data__authorized_users,
data__filesystem,
data__image,
data__label,
data__root_pass,
data__size,
data__stackscript_data,
data__stackscript_id
)
SELECT 
'{{ authorized_keys }}',
'{{ authorized_users }}',
'{{ filesystem }}',
'{{ image }}',
'{{ label }}',
'{{ root_pass }}',
{{ size }} --required,
'{{ stackscript_data }}',
{{ stackscript_id }}
RETURNING
id,
created,
disk_encryption,
filesystem,
label,
size,
status,
updated
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: disks
  props:
    - name: authorized_keys
      value: array
      description: >
        __Write-only__ A list of public SSH keys that will be automatically appended to the root user's `~/.ssh/authorized_keys` file when deploying from an Image.
        
    - name: authorized_users
      value: array
      description: >
        __Write-only__ A list of usernames. If the usernames have associated SSH keys, the keys will be appended to the root users `~/.ssh/authorized_keys` file automatically when deploying from an Image.
        
    - name: filesystem
      value: string
      description: >
        The disk's format or file system. A value of `raw` indicates no file system, just a raw binary stream. A value of `swap` indicates a Linux swap area. The values `ext3` or `ext4` represent these Linux journaling file systems. The value `ext2` is the deprecated ext2 Linux file system. Finally, `initrd` indicates the disk is formatted as an uncompressed initial RAM disk.

> 📘
>
> The `ext2` file system doesn't properly support timestamps and will be removed from Linux support in the near future. Also, `initrd` is a legacy format that no longer applies to most use cases. As a best practice, use the other supported formats or file systems instead.
        
      valid_values: ['raw', 'swap', 'ext2', 'ext3', 'ext4', 'initrd']
    - name: image
      value: string
      description: >
        An Image ID to deploy the Linode Disk from.

Run the [List images](https://techdocs.akamai.com/linode-api/reference/get-images) operation with authentication to view all available Images. Official Linode Images start with `linode/`, while your Account's Images start with `private/`. Creating a disk from a Private Image requires `read_only` or `read_write` permissions for that Image. Run the [Update a user's grants](https://techdocs.akamai.com/linode-api/reference/put-user-grants) operation to adjust permissions for an Account Image.
        
    - name: label
      value: string
      description: >
        __Filterable__ The name of the disk. This is for display purposes only.
        
    - name: root_pass
      value: string
      description: >
        __Write-only__ This sets the root user's password on a newly created Linode Disk when deploying from an Image.

- __Required__ when creating a Linode Disk from an Image, including when using a StackScript.

- Must meet a password strength score requirement that is calculated internally by the API. If the strength requirement is not met, you will receive a `Password does not meet strength requirement` error.
        
    - name: size
      value: integer
      description: >
        __Filterable__ The size of the Disk in MB.

Images require a minimum size. Run the [Get an image](https://techdocs.akamai.com/linode-api/reference/get-image) operation to view its size.
        
    - name: stackscript_data
      value: object
      description: >
        This field is required only if the StackScript being deployed requires input data from the User for successful completion. See [User Defined Fields (UDFs)](https://www.linode.com/docs/products/tools/stackscripts/guides/write-a-custom-script/#declare-user-defined-fields-udfs) for more details.

This field is required to be valid JSON.

Total length cannot exceed 65,535 characters.
        
    - name: stackscript_id
      value: integer
      description: >
        A StackScript ID that will cause the referenced StackScript to be run during deployment of this Linode. A compatible `image` is required to use a StackScript. To get a list of available StackScript and their permitted Images, run [List StackScripts](https://techdocs.akamai.com/linode-api/reference/get-stack-scripts). This field cannot be used when deploying from a Backup or a Private Image.
        
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_disk"
    values={[
        { label: 'put_disk', value: 'put_disk' }
    ]}
>
<TabItem value="put_disk">

Updates a Disk that you have permission to `read_write`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.linode.disks
SET 
data__label = '{{ label }}'
WHERE 

RETURNING
id,
created,
disk_encryption,
filesystem,
label,
size,
status,
updated;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_disk"
    values={[
        { label: 'delete_disk', value: 'delete_disk' }
    ]}
>
<TabItem value="delete_disk">

Deletes a Disk you have permission to `read_write`.<br /><br />__Deleting a Disk is a destructive action and cannot be undone.__<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.linode.disks;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="post_clone_linode_disk"
    values={[
        { label: 'post_clone_linode_disk', value: 'post_clone_linode_disk' },
        { label: 'post_reset_disk_password', value: 'post_reset_disk_password' },
        { label: 'post_resize_disk', value: 'post_resize_disk' }
    ]}
>
<TabItem value="post_clone_linode_disk">

Copies a disk, byte-for-byte, into a new disk on the same Linode. The operation fails if the target doesn't have enough storage space. A Linode can have up to 50 disks.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.linode.disks.post_clone_linode_disk 
;
```
</TabItem>
<TabItem value="post_reset_disk_password">

Resets the password of a Disk you have permission to `read_write`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.linode.disks.post_reset_disk_password 
@@json=
'{
"password": "{{ password }}"
}';
```
</TabItem>
<TabItem value="post_resize_disk">

Resizes a Disk you have permission to `read_write`.<br /><br />The Disk must not be in use. If the Disk is in use, the request will succeed but the resize will ultimately fail. For a request to succeed, the Linode must be shut down prior to resizing the Disk, or the Disk must not be assigned to the Linode's active Configuration Profile.<br /><br />If you are resizing the Disk to a smaller size, it cannot be made smaller than what is required by the total size of the files current on the Disk.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.linode.disks.post_resize_disk 
@@json=
'{
"size": {{ size }}
}';
```
</TabItem>
</Tabs>
