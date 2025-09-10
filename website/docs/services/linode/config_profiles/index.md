--- 
title: config_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - config_profiles
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

Creates, updates, deletes, gets or lists a <code>config_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>config_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.linode.config_profiles" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_linode_config"
    values={[
        { label: 'get_linode_config', value: 'get_linode_config' },
        { label: 'get_linode_configs', value: 'get_linode_configs' }
    ]}
>
<TabItem value="get_linode_config">

A configuration profile object.

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
    <td>__Read-only__ The ID of this Config.</td>
</tr>
<tr>
    <td><CopyableCode code="comments" /></td>
    <td><code>string</code></td>
    <td>Optional field for arbitrary user comments on this configuration. (example: This is my main Config)</td>
</tr>
<tr>
    <td><CopyableCode code="devices" /></td>
    <td><code>object</code></td>
    <td>A dictionary of device disks to use as a device map in a Linode's configuration profile.  - An empty device disk dictionary or a dictionary with empty values for device slots is allowed. - If no devices are specified, booting from this configuration will hold until a device exists that allows the boot process to start.</td>
</tr>
<tr>
    <td><CopyableCode code="helpers" /></td>
    <td><code>object</code></td>
    <td>Helpers enabled when booting to this Linode configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="interfaces" /></td>
    <td><code>array</code></td>
    <td>`interfaces` is applicable only to legacy configuration profiles and does not apply to [Linode interfaces](https://techdocs.akamai.com/linode-api/reference/post-linode-interface).  From one to three network interfaces to add to this Linode's configuration profile. The position in the array determines which of the Linode's network interfaces is configured:  - First [0]:  `eth0` - Second [1]: `eth1` - Third [2]:  `eth2`  When updating a Linode's legacy interfaces, _each interface must be redefined_. An empty `interfaces` array results in a default `public` type interface configuration only.  If no public Interface is configured, public IP addresses are still assigned to the Linode but will not be usable without manual configuration.  &gt; 📘 &gt; &gt; Changes to Linode Interface configurations can be enabled by rebooting the Linode.  `vpc` details  See the [VPC documentation](https://www.linode.com/docs/products/networking/vpc/#technical-specifications) guide for its specifications and limitations.  `vlan` details  - Only Next Generation Network (NGN) data centers support VLANs. Run the [List regions](https://techdocs.akamai.com/linode-api/reference/get-regions) operation to view the capabilities of data center regions. If a VLAN is attached to your Linode and you attempt to migrate or clone it to a non-NGN data center, the migration or cloning will not initiate. If a Linode cannot be migrated or cloned because of an incompatibility, you will be prompted to select a different data center or contact support. - See the [VLANs Overview](https://www.linode.com/docs/products/networking/vlans/#technical-specifications) guide to view additional specifications and limitations.</td>
</tr>
<tr>
    <td><CopyableCode code="kernel" /></td>
    <td><code>string</code></td>
    <td>The ID of the kernel used to boot a Linode. Run the [List kernels](https://techdocs.akamai.com/linode-api/reference/get-kernels) operation to see all available kernels. Here are some commonly used kernels:  - `linode/latest-64bit`. This is the default, our latest kernel at the time of an instance boot or reboot.  - `linode/grub2`. The upstream distribution-supplied kernel that's installed on the primary disk, or a custom kernel if installed.  - `linode/direct-disk`. The master boot record (MBR) of the primary disk or root device. Use this in place of a Linux kernel. (default: linode/latest-64bit, example: linode/latest-64bit)</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The name of the configuration for display in Akamai Cloud Manager. (example: My Config)</td>
</tr>
<tr>
    <td><CopyableCode code="memory_limit" /></td>
    <td><code>integer</code></td>
    <td>Defaults to the total RAM of the Linode.</td>
</tr>
<tr>
    <td><CopyableCode code="root_device" /></td>
    <td><code>string</code></td>
    <td>The root device to boot.  &gt; 📘  - If you leave this empty or set an invalid value, the root device defaults to `/dev/sda`.  - If you specify a device at the root device location and it's not mounted, the Linode won't boot until a device is mounted. (example: /dev/sda, pattern: <code>a-z, A-Z, 0-9, /, _, -</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="run_level" /></td>
    <td><code>string</code></td>
    <td>Defines the state of your Linode after booting. Defaults to `default`. (example: default)</td>
</tr>
<tr>
    <td><CopyableCode code="virt_mode" /></td>
    <td><code>string</code></td>
    <td>Controls the virtualization mode. Defaults to `paravirt`.  - `paravirt` is suitable for most cases. Linodes running in `paravirt` mode share some qualities with the host, ultimately making it run faster since there is less transition between it and the host.  - `fullvirt` affords more customization, but is slower because 100% of the VM is virtualized. (example: paravirt)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_linode_configs">

Returns the configuration profiles associated with this Linode.

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
    <td><a href="#get_linode_config"><CopyableCode code="get_linode_config" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns information about a specific configuration profile.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_linode_configs"><CopyableCode code="get_linode_configs" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Lists configuration profiles associated with a Linode.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_add_linode_config"><CopyableCode code="post_add_linode_config" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__label"><code>data__label</code></a>, <a href="#parameter-data__devices"><code>data__devices</code></a></td>
    <td></td>
    <td>Adds a new configuration profile to a Linode.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation is for legacy configuration profiles only, and not [Linode interfaces](https://techdocs.akamai.com/linode-api/reference/post-linode-interface).<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_linode_config"><CopyableCode code="put_linode_config" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Updates a configuration profile.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_linode_config"><CopyableCode code="delete_linode_config" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes the specified configuration profile from the specified Linode.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_linode_config"
    values={[
        { label: 'get_linode_config', value: 'get_linode_config' },
        { label: 'get_linode_configs', value: 'get_linode_configs' }
    ]}
>
<TabItem value="get_linode_config">

Returns information about a specific configuration profile.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
comments,
devices,
helpers,
interfaces,
kernel,
label,
memory_limit,
root_device,
run_level,
virt_mode
FROM linode.linode.config_profiles;
```
</TabItem>
<TabItem value="get_linode_configs">

Lists configuration profiles associated with a Linode.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.linode.config_profiles
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}';
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_add_linode_config"
    values={[
        { label: 'post_add_linode_config', value: 'post_add_linode_config' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_add_linode_config">

Adds a new configuration profile to a Linode.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation is for legacy configuration profiles only, and not [Linode interfaces](https://techdocs.akamai.com/linode-api/reference/post-linode-interface).<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.linode.config_profiles (
data__comments,
data__devices,
data__helpers,
data__interfaces,
data__kernel,
data__label,
data__memory_limit,
data__root_device,
data__run_level,
data__virt_mode
)
SELECT 
'{{ comments }}',
'{{ devices }}' --required,
'{{ helpers }}',
'{{ interfaces }}',
'{{ kernel }}',
'{{ label }}' --required,
{{ memory_limit }},
'{{ root_device }}',
'{{ run_level }}',
'{{ virt_mode }}'
RETURNING
id,
comments,
devices,
helpers,
interfaces,
kernel,
label,
memory_limit,
root_device,
run_level,
virt_mode
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: config_profiles
  props:
    - name: comments
      value: string
      description: >
        Optional field for arbitrary user comments on this configuration.
        
    - name: devices
      value: object
      description: >
        A dictionary of device disks to use as a device map in a Linode's configuration profile.

- An empty device disk dictionary or a dictionary with empty values for device slots is allowed.
- If no devices are specified, booting from this configuration will hold until a device exists that allows the boot process to start.
        
    - name: helpers
      value: object
      description: >
        Helpers enabled when booting to this Linode configuration.
        
    - name: interfaces
      value: array
      description: >
        `interfaces` is applicable only to legacy configuration profiles and does not apply to [Linode interfaces](https://techdocs.akamai.com/linode-api/reference/post-linode-interface).

From one to three network interfaces to add to this Linode's configuration profile. The position in the array determines which of the Linode's network interfaces is configured:

- First [0]:  `eth0`
- Second [1]: `eth1`
- Third [2]:  `eth2`

When updating a Linode's legacy interfaces, _each interface must be redefined_. An empty `interfaces` array results in a default `public` type interface configuration only.

If no public Interface is configured, public IP addresses are still assigned to the Linode but will not be usable without manual configuration.

> 📘
>
> Changes to Linode Interface configurations can be enabled by rebooting the Linode.

`vpc` details

See the [VPC documentation](https://www.linode.com/docs/products/networking/vpc/#technical-specifications) guide for its specifications and limitations.

`vlan` details

- Only Next Generation Network (NGN) data centers support VLANs. Run the [List regions](https://techdocs.akamai.com/linode-api/reference/get-regions) operation to view the capabilities of data center regions. If a VLAN is attached to your Linode and you attempt to migrate or clone it to a non-NGN data center, the migration or cloning will not initiate. If a Linode cannot be migrated or cloned because of an incompatibility, you will be prompted to select a different data center or contact support.
- See the [VLANs Overview](https://www.linode.com/docs/products/networking/vlans/#technical-specifications) guide to view additional specifications and limitations.
        
    - name: kernel
      value: string
      description: >
        The ID of the kernel used to boot a Linode. Run the [List kernels](https://techdocs.akamai.com/linode-api/reference/get-kernels) operation to see all available kernels. Here are some commonly used kernels:

- `linode/latest-64bit`. This is the default, our latest kernel at the time of an instance boot or reboot.

- `linode/grub2`. The upstream distribution-supplied kernel that's installed on the primary disk, or a custom kernel if installed.

- `linode/direct-disk`. The master boot record (MBR) of the primary disk or root device. Use this in place of a Linux kernel.
        
      default: linode/latest-64bit
    - name: label
      value: string
      description: >
        __Filterable__ The name of the configuration for display in Akamai Cloud Manager.
        
    - name: memory_limit
      value: integer
      description: >
        Defaults to the total RAM of the Linode.
        
    - name: root_device
      value: string
      description: >
        The root device to boot.

> 📘

- If you leave this empty or set an invalid value, the root device defaults to `/dev/sda`.

- If you specify a device at the root device location and it's not mounted, the Linode won't boot until a device is mounted.
        
    - name: run_level
      value: string
      description: >
        Defines the state of your Linode after booting. Defaults to `default`.
        
      valid_values: ['default', 'single', 'binbash']
    - name: virt_mode
      value: string
      description: >
        Controls the virtualization mode. Defaults to `paravirt`.

- `paravirt` is suitable for most cases. Linodes running in `paravirt` mode share some qualities with the host, ultimately making it run faster since there is less transition between it and the host.

- `fullvirt` affords more customization, but is slower because 100% of the VM is virtualized.
        
      valid_values: ['paravirt', 'fullvirt']
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_linode_config"
    values={[
        { label: 'put_linode_config', value: 'put_linode_config' }
    ]}
>
<TabItem value="put_linode_config">

Updates a configuration profile.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.linode.config_profiles
SET 
data__comments = '{{ comments }}',
data__devices = '{{ devices }}',
data__helpers = '{{ helpers }}',
data__interfaces = '{{ interfaces }}',
data__kernel = '{{ kernel }}',
data__label = '{{ label }}',
data__memory_limit = {{ memory_limit }},
data__root_device = '{{ root_device }}',
data__run_level = '{{ run_level }}',
data__virt_mode = '{{ virt_mode }}'
WHERE 

RETURNING
id,
comments,
devices,
helpers,
interfaces,
kernel,
label,
memory_limit,
root_device,
run_level,
virt_mode;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_linode_config"
    values={[
        { label: 'delete_linode_config', value: 'delete_linode_config' }
    ]}
>
<TabItem value="delete_linode_config">

Deletes the specified configuration profile from the specified Linode.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.linode.config_profiles;
```
</TabItem>
</Tabs>
