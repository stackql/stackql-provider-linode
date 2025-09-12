--- 
title: config_profile_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - config_profile_interfaces
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

Creates, updates, deletes, gets or lists a <code>config_profile_interfaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>config_profile_interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.linode.config_profile_interfaces" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_linode_config_interface"
    values={[
        { label: 'get_linode_config_interface', value: 'get_linode_config_interface' },
        { label: 'get_linode_config_interfaces', value: 'get_linode_config_interfaces' }
    ]}
>
<TabItem value="get_linode_config_interface">

A configuration interface object.

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
    <td>__Read-only__ The unique ID representing this interface.</td>
</tr>
<tr>
    <td><CopyableCode code="subnet_id" /></td>
    <td><code>integer</code></td>
    <td>The `id` of the VPC subnet for this interface. Use this value in a request to assign a Linode to a VPC subnet.  - Required for `vpc` type interfaces.  - Returned as `null` for non-`vpc` type interfaces.  - Once you've assigned a VPC subnet to an interface, you can't update it.  - You need to reboot a Linode using the interface's configuration profile to assign the Linode to a VPC subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="vpc_id" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The `id` of the VPC configured for this interface. Returned as `null` for non-`vpc` type interfaces.</td>
</tr>
<tr>
    <td><CopyableCode code="active" /></td>
    <td><code>boolean</code></td>
    <td>__Read-only__ Returns `true` if the interface is in use, meaning that the Linode has been booted using the configuration profile to which the interface belongs.</td>
</tr>
<tr>
    <td><CopyableCode code="ip_ranges" /></td>
    <td><code>array</code></td>
    <td>IPv4 CIDR VPC subnet ranges that are routed to this interface.  When included in a request:  - A range can't include any addresses that are assigned to an active Linode or another VPC subnet.  - When updating, you need to include any existing ranges to maintain them. If a range is left out, it will be removed.  - Submit this as an empty array removes all existing values.  - Omit this object to leave existing values as is.  &lt;&lt;LB&gt;&gt;  &gt; 📘 &gt; &gt; This is only supported for interfaces with a `purpose` of `vpc`.</td>
</tr>
<tr>
    <td><CopyableCode code="ipam_address" /></td>
    <td><code>string (ip/netmask)</code></td>
    <td>This interface's private IP address in classless inter-domain routing (CIDR) notation.  For interfaces with a `purpose` of `public`:  - If you include this in a request, set it to an empty string (`""`) or `null`.  - Returned as `null` in a response.  For interfaces with a `purpose` of `vlan`:  - To avoid conflicting addresses, make sure this value is unique for each `vlan` interface.  - This should be unique among devices attached to the VLAN to avoid conflict.  - If Network Helper is enabled, the Linode's interface will be automatically configured to use this address after the Linode is rebooted. If Network Helper is disabled, enable the address using [manual static IP configuration](https://www.linode.com/docs/guides/manual-network-configuration/).  For interfaces with a `purpose` of `vpc`:  - If you include this in a request, set it to an empty string (`""`) or `null`.  - Returned as `null` in a response. (example: 10.0.0.1/24)</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4" /></td>
    <td><code>object</code></td>
    <td>IPv4 addresses configured for this interface. This only applies to interfaces with a `purpose` of `vpc`. Returned as `null` if no `vpc` interface is assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The name of this interface.  For interfaces with a `purpose` of `vlan`:  - Required.  - This needs to be unique among a Linode's interfaces. A Linode can't be attached to the same VLAN multiple times.  - This can only contain ASCII letters, numbers, and dashes (`-`). You can't use two consecutive dashes (`--`).  - If the VLAN label is new, a VLAN is created. Up to 10 VLANs can be created in each data center `region`. To view your active VLANs, run the [List VLANs](https://techdocs.akamai.com/linode-api/reference/get-vlans) operation.  For interfaces with a `purpose` of `public`:  - If you include this in a request, set it to an empty string (`""`) or `null`.  - Returned as `null` in a response.  For interfaces with a `purpose` of `vpc`:  - If you include this in a request, set it to an empty string (`""`) or `null`.  - Returned as `null` in a response. (example: example-interface, pattern: <code>[a-zA-Z0-9-]+</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="primary" /></td>
    <td><code>boolean</code></td>
    <td>The default route to the Linode. Each Linode can have one interface set as its `primary`. If you haven't specifically set a `primary`, the first non-`vlan` type interface is automatically treated as the primary.  &gt; 📘 &gt; &gt; This needs to be set to `false` for any interface that uses `vlan` as its `purpose`.</td>
</tr>
<tr>
    <td><CopyableCode code="purpose" /></td>
    <td><code>string</code></td>
    <td>The type of interface. This can be `public`, `vlan`, or `vpc`.  For interfaces with a `purpose` of `public`:  - You can only define one `public` interface per Linode.  - The Linode's default public IPv4 address is assigned to the `public` interface.  - A Linode needs a `public` interface in the first or `eth0` position to be reachable via the public internet, after it boots. If no `public` interface is configured, you can only access the Linode through [LISH](https://www.linode.com/docs/products/compute/compute-instances/guides/lish/), or through another Linode that's connected to the same VLAN or VPC.  For interfaces with a `purpose` of `vlan`:  - Configuring this `purpose` of interface attaches a Linode to the VLAN with the specified `label`.  - If an `ipam_address` is configured, the Linode uses this address.  For interfaces with a `purpose` of `vpc`:  - Configuring this `purpose` of interface attaches a Linode to an existing VPC subnet with the specified `subnet_id`.  - When the interface is activated, the Linode is configured to use an IP address from the range in the assigned VPC subnet. See `ipv4.vpc` for more information. (example: vlan)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_linode_config_interfaces">

An ordered array of configuration profile interface objects.

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
    <td>__Read-only__ The unique ID representing this interface.</td>
</tr>
<tr>
    <td><CopyableCode code="subnet_id" /></td>
    <td><code>integer</code></td>
    <td>The `id` of the VPC subnet for this interface. Use this value in a request to assign a Linode to a VPC subnet.  - Required for `vpc` type interfaces.  - Returned as `null` for non-`vpc` type interfaces.  - Once you've assigned a VPC subnet to an interface, you can't update it.  - You need to reboot a Linode using the interface's configuration profile to assign the Linode to a VPC subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="vpc_id" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The `id` of the VPC configured for this interface. Returned as `null` for non-`vpc` type interfaces.</td>
</tr>
<tr>
    <td><CopyableCode code="active" /></td>
    <td><code>boolean</code></td>
    <td>__Read-only__ Returns `true` if the interface is in use, meaning that the Linode has been booted using the configuration profile to which the interface belongs.</td>
</tr>
<tr>
    <td><CopyableCode code="ip_ranges" /></td>
    <td><code>array</code></td>
    <td>IPv4 CIDR VPC subnet ranges that are routed to this interface.  When included in a request:  - A range can't include any addresses that are assigned to an active Linode or another VPC subnet.  - When updating, you need to include any existing ranges to maintain them. If a range is left out, it will be removed.  - Submit this as an empty array removes all existing values.  - Omit this object to leave existing values as is.  &lt;&lt;LB&gt;&gt;  &gt; 📘 &gt; &gt; This is only supported for interfaces with a `purpose` of `vpc`.</td>
</tr>
<tr>
    <td><CopyableCode code="ipam_address" /></td>
    <td><code>string (ip/netmask)</code></td>
    <td>This interface's private IP address in classless inter-domain routing (CIDR) notation.  For interfaces with a `purpose` of `public`:  - If you include this in a request, set it to an empty string (`""`) or `null`.  - Returned as `null` in a response.  For interfaces with a `purpose` of `vlan`:  - To avoid conflicting addresses, make sure this value is unique for each `vlan` interface.  - This should be unique among devices attached to the VLAN to avoid conflict.  - If Network Helper is enabled, the Linode's interface will be automatically configured to use this address after the Linode is rebooted. If Network Helper is disabled, enable the address using [manual static IP configuration](https://www.linode.com/docs/guides/manual-network-configuration/).  For interfaces with a `purpose` of `vpc`:  - If you include this in a request, set it to an empty string (`""`) or `null`.  - Returned as `null` in a response. (example: 10.0.0.1/24)</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4" /></td>
    <td><code>object</code></td>
    <td>IPv4 addresses configured for this interface. This only applies to interfaces with a `purpose` of `vpc`. Returned as `null` if no `vpc` interface is assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The name of this interface.  For interfaces with a `purpose` of `vlan`:  - Required.  - This needs to be unique among a Linode's interfaces. A Linode can't be attached to the same VLAN multiple times.  - This can only contain ASCII letters, numbers, and dashes (`-`). You can't use two consecutive dashes (`--`).  - If the VLAN label is new, a VLAN is created. Up to 10 VLANs can be created in each data center `region`. To view your active VLANs, run the [List VLANs](https://techdocs.akamai.com/linode-api/reference/get-vlans) operation.  For interfaces with a `purpose` of `public`:  - If you include this in a request, set it to an empty string (`""`) or `null`.  - Returned as `null` in a response.  For interfaces with a `purpose` of `vpc`:  - If you include this in a request, set it to an empty string (`""`) or `null`.  - Returned as `null` in a response. (example: example-interface, pattern: <code>[a-zA-Z0-9-]+</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="primary" /></td>
    <td><code>boolean</code></td>
    <td>The default route to the Linode. Each Linode can have one interface set as its `primary`. If you haven't specifically set a `primary`, the first non-`vlan` type interface is automatically treated as the primary.  &gt; 📘 &gt; &gt; This needs to be set to `false` for any interface that uses `vlan` as its `purpose`.</td>
</tr>
<tr>
    <td><CopyableCode code="purpose" /></td>
    <td><code>string</code></td>
    <td>The type of interface. This can be `public`, `vlan`, or `vpc`.  For interfaces with a `purpose` of `public`:  - You can only define one `public` interface per Linode.  - The Linode's default public IPv4 address is assigned to the `public` interface.  - A Linode needs a `public` interface in the first or `eth0` position to be reachable via the public internet, after it boots. If no `public` interface is configured, you can only access the Linode through [LISH](https://www.linode.com/docs/products/compute/compute-instances/guides/lish/), or through another Linode that's connected to the same VLAN or VPC.  For interfaces with a `purpose` of `vlan`:  - Configuring this `purpose` of interface attaches a Linode to the VLAN with the specified `label`.  - If an `ipam_address` is configured, the Linode uses this address.  For interfaces with a `purpose` of `vpc`:  - Configuring this `purpose` of interface attaches a Linode to an existing VPC subnet with the specified `subnet_id`.  - When the interface is activated, the Linode is configured to use an IP address from the range in the assigned VPC subnet. See `ipv4.vpc` for more information. (example: vlan)</td>
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
    <td><a href="#get_linode_config_interface"><CopyableCode code="get_linode_config_interface" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns a single configuration profile interface. To access this operation, your user needs at least the `read_only` [grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) for the Linode.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_linode_config_interfaces"><CopyableCode code="get_linode_config_interfaces" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns all configuration profile interfaces assigned to a specific configuration profile, on a specific Linode. To access this operation, your user needs the `read_write` [grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) for the Linode.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_linode_config_interface"><CopyableCode code="post_linode_config_interface" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__purpose"><code>data__purpose</code></a></td>
    <td></td>
    <td>Creates and appends a single interface to the end of the `interfaces` array for an existing configuration profile. After you add the interface, you need to reboot the target Linode.<br /><br />- To access this operation, your user needs the `read_write` [grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) for the Linode.<br /><br />- A successful request triggers a `linode_config_update` [event](https://techdocs.akamai.com/linode-api/reference/get-events).<br /><br />- Only one interface can be set as `primary`. Setting `primary` to `true` for an interface sets all other interfaces to `false`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_linode_config_interface"><CopyableCode code="put_linode_config_interface" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Update a `vpc` or `public` configuration profile interface for a specific configuration profile, on a specific Linode.<br /><br />- To access this operation, your user needs the `read_write` [grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) for the Linode.<br /><br />- A successful request triggers a `linode_config_update` [event](https://techdocs.akamai.com/linode-api/reference/get-events).<br /><br />- Only certain attributes can be updated for a configuration profile interface. You need to [add](https://techdocs.akamai.com/linode-api/reference/post-linode-config-interface) a new configuration profile interface on your Linode if you need new values for any other attribute. Here are the supported objects, based on the interface's `purpose`:<br /><br />  - `public`. The `primary` attribute.<br /><br />  - `vpc`. The `ip_ranges`, `ipv4`, or `primary` attributes.<br /><br />- You can't update a configuration profile with a `purpose` of `vlan`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_linode_config_interface"><CopyableCode code="delete_linode_config_interface" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes a configuration profile interface from a specific configuration profile, on a specific Linode.<br /><br />- To access this operation, your user needs the `read_write` [grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) for the Linode.<br /><br />- A successful request triggers a `linode_config_update` [event](https://techdocs.akamai.com/linode-api/reference/get-events).<br /><br />- You can't delete an active configuration profile interface. First, you need to shut down the associated Linode or restart it using another configuration profile.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_linode_config_interfaces"><CopyableCode code="post_linode_config_interfaces" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-ids"><code>ids</code></a></td>
    <td></td>
    <td>Reorders the existing Interfaces of a Configuration Profile.<br /><br />- The User accessing this operation must have `read_write` grants to the Linode.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_linode_config_interface"
    values={[
        { label: 'get_linode_config_interface', value: 'get_linode_config_interface' },
        { label: 'get_linode_config_interfaces', value: 'get_linode_config_interfaces' }
    ]}
>
<TabItem value="get_linode_config_interface">

Returns a single configuration profile interface. To access this operation, your user needs at least the `read_only` [grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) for the Linode.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
subnet_id,
vpc_id,
active,
ip_ranges,
ipam_address,
ipv4,
label,
primary,
purpose
FROM linode.linode.config_profile_interfaces
;
```
</TabItem>
<TabItem value="get_linode_config_interfaces">

Returns all configuration profile interfaces assigned to a specific configuration profile, on a specific Linode. To access this operation, your user needs the `read_write` [grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) for the Linode.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
subnet_id,
vpc_id,
active,
ip_ranges,
ipam_address,
ipv4,
label,
primary,
purpose
FROM linode.linode.config_profile_interfaces
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_linode_config_interface"
    values={[
        { label: 'post_linode_config_interface', value: 'post_linode_config_interface' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_linode_config_interface">

Creates and appends a single interface to the end of the `interfaces` array for an existing configuration profile. After you add the interface, you need to reboot the target Linode.<br /><br />- To access this operation, your user needs the `read_write` [grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) for the Linode.<br /><br />- A successful request triggers a `linode_config_update` [event](https://techdocs.akamai.com/linode-api/reference/get-events).<br /><br />- Only one interface can be set as `primary`. Setting `primary` to `true` for an interface sets all other interfaces to `false`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.linode.config_profile_interfaces (
data__ip_ranges,
data__ipam_address,
data__ipv4,
data__label,
data__primary,
data__purpose,
data__subnet_id
)
SELECT 
'{{ ip_ranges }}',
'{{ ipam_address }}',
'{{ ipv4 }}',
'{{ label }}',
{{ primary }},
'{{ purpose }}' /* required */,
{{ subnet_id }}
RETURNING
id,
subnet_id,
vpc_id,
active,
ip_ranges,
ipam_address,
ipv4,
label,
primary,
purpose
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: config_profile_interfaces
  props:
    - name: ip_ranges
      value: array
      description: >
        IPv4 CIDR VPC subnet ranges that are routed to this interface.

When included in a request:

- A range can't include any addresses that are assigned to an active Linode or another VPC subnet.

- When updating, you need to include any existing ranges to maintain them. If a range is left out, it will be removed.

- Submit this as an empty array removes all existing values.

- Omit this object to leave existing values as is.

<<LB>>

> 📘
>
> This is only supported for interfaces with a `purpose` of `vpc`.
        
    - name: ipam_address
      value: string
      description: >
        This interface's private IP address in classless inter-domain routing (CIDR) notation.

For interfaces with a `purpose` of `public`:

- If you include this in a request, set it to an empty string (`""`) or `null`.

- Returned as `null` in a response.

For interfaces with a `purpose` of `vlan`:

- To avoid conflicting addresses, make sure this value is unique for each `vlan` interface.

- This should be unique among devices attached to the VLAN to avoid conflict.

- If Network Helper is enabled, the Linode's interface will be automatically configured to use this address after the Linode is rebooted. If Network Helper is disabled, enable the address using [manual static IP configuration](https://www.linode.com/docs/guides/manual-network-configuration/).

For interfaces with a `purpose` of `vpc`:

- If you include this in a request, set it to an empty string (`""`) or `null`.

- Returned as `null` in a response.
        
    - name: ipv4
      value: object
      description: >
        IPv4 addresses configured for this interface. This only applies to interfaces with a `purpose` of `vpc`. Returned as `null` if no `vpc` interface is assigned.
        
    - name: label
      value: string
      description: >
        __Filterable__ The name of this interface.

For interfaces with a `purpose` of `vlan`:

- Required.

- This needs to be unique among a Linode's interfaces. A Linode can't be attached to the same VLAN multiple times.

- This can only contain ASCII letters, numbers, and dashes (`-`). You can't use two consecutive dashes (`--`).

- If the VLAN label is new, a VLAN is created. Up to 10 VLANs can be created in each data center `region`. To view your active VLANs, run the [List VLANs](https://techdocs.akamai.com/linode-api/reference/get-vlans) operation.

For interfaces with a `purpose` of `public`:

- If you include this in a request, set it to an empty string (`""`) or `null`.

- Returned as `null` in a response.

For interfaces with a `purpose` of `vpc`:

- If you include this in a request, set it to an empty string (`""`) or `null`.

- Returned as `null` in a response.
        
    - name: primary
      value: boolean
      description: >
        The default route to the Linode. Each Linode can have one interface set as its `primary`. If you haven't specifically set a `primary`, the first non-`vlan` type interface is automatically treated as the primary.

> 📘
>
> This needs to be set to `false` for any interface that uses `vlan` as its `purpose`.
        
    - name: purpose
      value: string
      description: >
        The type of interface. This can be `public`, `vlan`, or `vpc`.

For interfaces with a `purpose` of `public`:

- You can only define one `public` interface per Linode.

- The Linode's default public IPv4 address is assigned to the `public` interface.

- A Linode needs a `public` interface in the first or `eth0` position to be reachable via the public internet, after it boots. If no `public` interface is configured, you can only access the Linode through [LISH](https://www.linode.com/docs/products/compute/compute-instances/guides/lish/), or through another Linode that's connected to the same VLAN or VPC.

For interfaces with a `purpose` of `vlan`:

- Configuring this `purpose` of interface attaches a Linode to the VLAN with the specified `label`.

- If an `ipam_address` is configured, the Linode uses this address.

For interfaces with a `purpose` of `vpc`:

- Configuring this `purpose` of interface attaches a Linode to an existing VPC subnet with the specified `subnet_id`.

- When the interface is activated, the Linode is configured to use an IP address from the range in the assigned VPC subnet. See `ipv4.vpc` for more information.
        
      valid_values: ['public', 'vlan', 'vpc']
    - name: subnet_id
      value: integer
      description: >
        The `id` of the VPC subnet for this interface. Use this value in a request to assign a Linode to a VPC subnet.

- Required for `vpc` type interfaces.

- Returned as `null` for non-`vpc` type interfaces.

- Once you've assigned a VPC subnet to an interface, you can't update it.

- You need to reboot a Linode using the interface's configuration profile to assign the Linode to a VPC subnet.
        
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_linode_config_interface"
    values={[
        { label: 'put_linode_config_interface', value: 'put_linode_config_interface' }
    ]}
>
<TabItem value="put_linode_config_interface">

Update a `vpc` or `public` configuration profile interface for a specific configuration profile, on a specific Linode.<br /><br />- To access this operation, your user needs the `read_write` [grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) for the Linode.<br /><br />- A successful request triggers a `linode_config_update` [event](https://techdocs.akamai.com/linode-api/reference/get-events).<br /><br />- Only certain attributes can be updated for a configuration profile interface. You need to [add](https://techdocs.akamai.com/linode-api/reference/post-linode-config-interface) a new configuration profile interface on your Linode if you need new values for any other attribute. Here are the supported objects, based on the interface's `purpose`:<br /><br />  - `public`. The `primary` attribute.<br /><br />  - `vpc`. The `ip_ranges`, `ipv4`, or `primary` attributes.<br /><br />- You can't update a configuration profile with a `purpose` of `vlan`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.linode.config_profile_interfaces
SET 
data__ip_ranges = '{{ ip_ranges }}',
data__ipv4 = '{{ ipv4 }}',
data__primary = {{ primary }}
RETURNING
id,
subnet_id,
vpc_id,
active,
ip_ranges,
ipam_address,
ipv4,
label,
primary,
purpose;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_linode_config_interface"
    values={[
        { label: 'delete_linode_config_interface', value: 'delete_linode_config_interface' }
    ]}
>
<TabItem value="delete_linode_config_interface">

Deletes a configuration profile interface from a specific configuration profile, on a specific Linode.<br /><br />- To access this operation, your user needs the `read_write` [grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) for the Linode.<br /><br />- A successful request triggers a `linode_config_update` [event](https://techdocs.akamai.com/linode-api/reference/get-events).<br /><br />- You can't delete an active configuration profile interface. First, you need to shut down the associated Linode or restart it using another configuration profile.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.linode.config_profile_interfaces
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="post_linode_config_interfaces"
    values={[
        { label: 'post_linode_config_interfaces', value: 'post_linode_config_interfaces' }
    ]}
>
<TabItem value="post_linode_config_interfaces">

Reorders the existing Interfaces of a Configuration Profile.<br /><br />- The User accessing this operation must have `read_write` grants to the Linode.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.linode.config_profile_interfaces.post_linode_config_interfaces 
@@json=
'{
"ids": "{{ ids }}"
}'
;
```
</TabItem>
</Tabs>
