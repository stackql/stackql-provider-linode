--- 
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
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

Creates, updates, deletes, gets or lists a <code>backups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.linode.backups" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_backup"
    values={[
        { label: 'get_backup', value: 'get_backup' },
        { label: 'get_backups', value: 'get_backups' }
    ]}
>
<TabItem value="get_backup">

A single Backup.

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
    <td>__Read-only__ The unique ID of this Backup.</td>
</tr>
<tr>
    <td><CopyableCode code="available" /></td>
    <td><code>boolean</code></td>
    <td>__Read-only__ Whether this Backup is available for restoration.  Backups undergoing maintenance are not available for restoration.</td>
</tr>
<tr>
    <td><CopyableCode code="configs" /></td>
    <td><code>array</code></td>
    <td>__Read-only__ A list of the labels of the Configuration profiles that are part of the Backup.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ The date the Backup was taken. (example: 2018-01-15T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="disks" /></td>
    <td><code>array</code></td>
    <td>__Read-only__ A list of the disks that are part of the Backup.</td>
</tr>
<tr>
    <td><CopyableCode code="finished" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ The date the Backup completed. (example: 2018-01-15T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>A label for Backups that are of type `snapshot`. (example: Webserver-Backup-2018)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The current state of a specific Backup. (example: successful)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ This indicates whether the Backup is an automatic Backup or manual snapshot taken by the User at a specific point in time. (example: snapshot)</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ The date the Backup was most recently updated. (example: 2018-01-15T00:01:01)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_backups">

A collection of the specified Linode's available backups.

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
    <td><CopyableCode code="automatic" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="snapshot" /></td>
    <td><code>object</code></td>
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
    <td><a href="#get_backup"><CopyableCode code="get_backup" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns information about a Backup.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_backups"><CopyableCode code="get_backups" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns information about this Linode's available backups.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_snapshot"><CopyableCode code="post_snapshot" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__label"><code>data__label</code></a></td>
    <td></td>
    <td>Creates a snapshot backup of a Linode.<br /><br />&gt; 📘<br />&gt;<br />&gt; - Backups aren't encrypted even when they're taken from an encrypted disk. When a backup is restored, and if encryption is enabled, the data stored on the disk is encrypted again.<br />&gt;<br />&gt; - If you already have a snapshot of this Linode, the previous snapshot will be deleted.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_cancel_backups"><CopyableCode code="post_cancel_backups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Cancels the Backup service on the given Linode. Deletes all of this Linode's existing backups forever.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_enable_backups"><CopyableCode code="post_enable_backups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Enables backups for the specified Linode.<br /><br />&gt; 📘<br />&gt;<br />&gt; Backups aren't encrypted even when they're taken from an encrypted disk. When a backup is restored, and if encryption is enabled, the data stored on the disk is encrypted again.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_restore_backup"><CopyableCode code="post_restore_backup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-linode_id"><code>linode_id</code></a></td>
    <td></td>
    <td>Restores a Linode's backup to the specified Linode.<br /><br />- Backups may not be restored across regions.<br />- Only successfully completed backups that are not undergoing maintenance can be restored.<br />- The Linode that the backup is being restored to can't be the target of a current backup.<br /><br />When you restore a backup, the restored disk is assigned the same [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) as the original disk. In most cases, this is acceptable and doesn't cause issues. However, if you try to mount both the original disk and the corresponding restore disk at the same time (by assigning them both to devices in your Configuration Profile's __Block Device Assignment__), you'll encounter a UUID "collision".<br /><br />When this happens, the system selects, and mounts, only one of the disks at random. This is because both disks are sharing the same UUID. Your instance _may fail to boot_ because the API can't tell which disk is root. If your system boots in this scenario, you won't see an immediate indication if you're booted into the restored disk or the original disk, and you'll be unable to access both disks at the same time.<br /><br />To avoid this, only restore a backup to the same Linode if you don't intend to mount them at the same time, or you're comfortable modifying UUIDs. If you need access to files on both the original disk and the restored disk simultaneously -- for example, if you need to copy files between them -- you should restore the backup to a separate Linode or [create](https://techdocs.akamai.com/linode-api/reference/post-linode-instance) a new Linode using the desired `backup_id`.<br /><br />To learn more about block device assignments and viewing your disks' UUIDs, see our guide on [Configuration Profiles](https://www.linode.com/docs/products/compute/compute-instances/guides/configuration-profiles/#block-device-assignment).<br /><br />&gt; 📘<br />&gt;<br />&gt; Backups aren't encrypted even when they're taken from an encrypted disk. When a backup is restored, and if encryption is enabled, the data stored on the disk is encrypted again.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_backup"
    values={[
        { label: 'get_backup', value: 'get_backup' },
        { label: 'get_backups', value: 'get_backups' }
    ]}
>
<TabItem value="get_backup">

Returns information about a Backup.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
available,
configs,
created,
disks,
finished,
label,
status,
type,
updated
FROM linode.linode.backups;
```
</TabItem>
<TabItem value="get_backups">

Returns information about this Linode's available backups.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
automatic,
snapshot
FROM linode.linode.backups;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_snapshot"
    values={[
        { label: 'post_snapshot', value: 'post_snapshot' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_snapshot">

Creates a snapshot backup of a Linode.<br /><br />&gt; 📘<br />&gt;<br />&gt; - Backups aren't encrypted even when they're taken from an encrypted disk. When a backup is restored, and if encryption is enabled, the data stored on the disk is encrypted again.<br />&gt;<br />&gt; - If you already have a snapshot of this Linode, the previous snapshot will be deleted.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.linode.backups (
data__label
)
SELECT 
'{{ label }}' --required
RETURNING
id,
available,
configs,
created,
disks,
finished,
label,
status,
type,
updated
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: backups
  props:
    - name: label
      value: string
      description: >
        The label for the new snapshot.
        
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="post_cancel_backups"
    values={[
        { label: 'post_cancel_backups', value: 'post_cancel_backups' },
        { label: 'post_enable_backups', value: 'post_enable_backups' },
        { label: 'post_restore_backup', value: 'post_restore_backup' }
    ]}
>
<TabItem value="post_cancel_backups">

Cancels the Backup service on the given Linode. Deletes all of this Linode's existing backups forever.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.linode.backups.post_cancel_backups 
;
```
</TabItem>
<TabItem value="post_enable_backups">

Enables backups for the specified Linode.<br /><br />&gt; 📘<br />&gt;<br />&gt; Backups aren't encrypted even when they're taken from an encrypted disk. When a backup is restored, and if encryption is enabled, the data stored on the disk is encrypted again.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.linode.backups.post_enable_backups 
;
```
</TabItem>
<TabItem value="post_restore_backup">

Restores a Linode's backup to the specified Linode.<br /><br />- Backups may not be restored across regions.<br />- Only successfully completed backups that are not undergoing maintenance can be restored.<br />- The Linode that the backup is being restored to can't be the target of a current backup.<br /><br />When you restore a backup, the restored disk is assigned the same [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) as the original disk. In most cases, this is acceptable and doesn't cause issues. However, if you try to mount both the original disk and the corresponding restore disk at the same time (by assigning them both to devices in your Configuration Profile's __Block Device Assignment__), you'll encounter a UUID "collision".<br /><br />When this happens, the system selects, and mounts, only one of the disks at random. This is because both disks are sharing the same UUID. Your instance _may fail to boot_ because the API can't tell which disk is root. If your system boots in this scenario, you won't see an immediate indication if you're booted into the restored disk or the original disk, and you'll be unable to access both disks at the same time.<br /><br />To avoid this, only restore a backup to the same Linode if you don't intend to mount them at the same time, or you're comfortable modifying UUIDs. If you need access to files on both the original disk and the restored disk simultaneously -- for example, if you need to copy files between them -- you should restore the backup to a separate Linode or [create](https://techdocs.akamai.com/linode-api/reference/post-linode-instance) a new Linode using the desired `backup_id`.<br /><br />To learn more about block device assignments and viewing your disks' UUIDs, see our guide on [Configuration Profiles](https://www.linode.com/docs/products/compute/compute-instances/guides/configuration-profiles/#block-device-assignment).<br /><br />&gt; 📘<br />&gt;<br />&gt; Backups aren't encrypted even when they're taken from an encrypted disk. When a backup is restored, and if encryption is enabled, the data stored on the disk is encrypted again.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.linode.backups.post_restore_backup 
@@json=
'{
"linode_id": {{ linode_id }}, 
"overwrite": {{ overwrite }}
}';
```
</TabItem>
</Tabs>
