--- 
title: ip_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_addresses
  - networking
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

Creates, updates, deletes, gets or lists an <code>ip_addresses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.networking.ip_addresses" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_ip"
    values={[
        { label: 'get_ip', value: 'get_ip' },
        { label: 'get_ips', value: 'get_ips' }
    ]}
>
<TabItem value="get_ip">

The requested IP Address.

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
    <td><CopyableCode code="interface_id" /></td>
    <td><code>integer</code></td>
    <td>__Beta__, __Read-only__ The Linode interface ID that this IP address is assigned to. This value is `null` if a Linode interface is not assigned, or if the IP is assigned to a legacy configuration profile interface.</td>
</tr>
<tr>
    <td><CopyableCode code="linode_id" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The ID of the Linode this address currently belongs to. For IPv4 addresses, this is by default the Linode that this address was assigned to on creation, and these addresses may be moved using the [Assign IPv4s to Linodes](https://techdocs.akamai.com/linode-api/reference/post-assign-ipv4s) operation. For SLAAC and link-local addresses, this value can't be changed.</td>
</tr>
<tr>
    <td><CopyableCode code="address" /></td>
    <td><code>string (ip)</code></td>
    <td>__Read-only__ The IP address. (example: 97.107.143.141)</td>
</tr>
<tr>
    <td><CopyableCode code="gateway" /></td>
    <td><code>string (ip)</code></td>
    <td>__Read-only__ The default gateway for this address. (example: 97.107.143.1)</td>
</tr>
<tr>
    <td><CopyableCode code="prefix" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The number of bits set in the subnet mask.</td>
</tr>
<tr>
    <td><CopyableCode code="public" /></td>
    <td><code>boolean</code></td>
    <td>__Read-only__ Whether this is a public or private IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="rdns" /></td>
    <td><code>string</code></td>
    <td>The reverse DNS assigned to this address. For public IPv4 addresses, this will be set to a default value provided by Linode if not explicitly set. (example: test.example.org)</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The Region this IP address resides in. (example: us-east)</td>
</tr>
<tr>
    <td><CopyableCode code="subnet_mask" /></td>
    <td><code>string (ip)</code></td>
    <td>__Read-only__ The mask that separates host bits from network bits for this address. (example: 255.255.255.0)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The type of address this is. (example: ipv4)</td>
</tr>
<tr>
    <td><CopyableCode code="vpc_nat_1_1" /></td>
    <td><code>object</code></td>
    <td>IPv4 address configured as a 1:1 NAT for this Interface. If no address is configured as a 1:1 NAT, `null` is returned.  &gt; 📘 &gt; &gt; Only allowed for `vpc` type interfaces.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_ips">

A paginated list of IP Addresses.

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
    <td><CopyableCode code="interface_id" /></td>
    <td><code>integer</code></td>
    <td>__Beta__, __Read-only__ The Linode interface ID this public IP address is assigned to. This value is `null` if a Linode interface is not assigned, or if the IP is assigned to a legacy configuration profile interface.</td>
</tr>
<tr>
    <td><CopyableCode code="linode_id" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The ID of the Linode this address currently belongs to. For IPv4 addresses, this defaults to the Linode that this address was assigned to on creation. IPv4 addresses may be moved using the [Assign IPv4s to Linodes](https://techdocs.akamai.com/linode-api/reference/post-assign-ipv4s) operation. For SLAAC and link-local addresses, this value may not be changed.</td>
</tr>
<tr>
    <td><CopyableCode code="address" /></td>
    <td><code>string (ip)</code></td>
    <td>__Filterable__, __Read-only__ The IP address. (example: 192.0.2.141)</td>
</tr>
<tr>
    <td><CopyableCode code="gateway" /></td>
    <td><code>string (ip)</code></td>
    <td>__Read-only__ The default gateway for this address. (example: 192.0.2.1)</td>
</tr>
<tr>
    <td><CopyableCode code="prefix" /></td>
    <td><code>integer</code></td>
    <td>__Filterable__, __Read-only__ The number of bits set in the subnet mask.</td>
</tr>
<tr>
    <td><CopyableCode code="public" /></td>
    <td><code>boolean</code></td>
    <td>__Read-only__ Whether this is a public or private IP address.</td>
</tr>
<tr>
    <td><CopyableCode code="rdns" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The reverse DNS assigned to this address. For public IPv4 addresses, this will be set to a default value provided by Linode if not explicitly set. (example: test.example.org)</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>__Filterable__, __Read-only__ The Region this IP address resides in. (example: us-east)</td>
</tr>
<tr>
    <td><CopyableCode code="subnet_mask" /></td>
    <td><code>string (ip)</code></td>
    <td>__Read-only__ The mask that separates host bits from network bits for this address. (example: 255.255.255.0)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>__Filterable__, __Read-only__ The type of address this is. (example: ipv4)</td>
</tr>
<tr>
    <td><CopyableCode code="vpc_nat_1_1" /></td>
    <td><code>object</code></td>
    <td>IPv4 address configured as a 1:1 NAT for this interface. Empty if no address is configured as a 1:1 NAT.  &gt; 📘 &gt; &gt; Only allowed for `vpc` type interfaces.</td>
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
    <td><a href="#get_ip"><CopyableCode code="get_ip" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns information about a single IP Address on your Account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_ips"><CopyableCode code="get_ips" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-skip_ipv6_rdns"><code>skip_ipv6_rdns</code></a></td>
    <td>Returns a paginated list of IP addresses on your account for Linodes or Linode interfaces, excluding private addresses.<br /><br />&gt; 👍<br />&gt;<br />&gt; if your application frequently accesses this operation and doesn't require IPv6 RDNS data, you can use the `skip_ipv6_rdns` query string to improve performance.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_ip"><CopyableCode code="put_ip" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-data__rdns"><code>data__rdns</code></a></td>
    <td></td>
    <td>Sets RDNS on an IP Address. Forward DNS must already be set up for reverse DNS to be applied. If you set the RDNS to `null` for public IPv4 addresses, it will be reset to the default _ip.linodeusercontent.com_ RDNS value.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_allocate_ip"><CopyableCode code="post_allocate_ip" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-type"><code>type</code></a>, <a href="#parameter-public"><code>public</code></a>, <a href="#parameter-linode_id"><code>linode_id</code></a></td>
    <td></td>
    <td>Allocates a new IPv4 Address on your Account. The Linode must be configured to support additional addresses - please [Open a support ticket](https://techdocs.akamai.com/linode-api/reference/post-ticket) requesting additional addresses before attempting allocation.<br /><br />&gt; 📘<br />&gt;<br />&gt; You can run this operation for Linodes with legacy configuration interfaces. You can't use it for Linodes with Linode interfaces. To allocate an IP for a Linode with Linode interfaces, use the [Add a Linode interface](https://techdocs.akamai.com/linode-api/reference/post-linode-interface) operation and set the public IPv4 address to `auto`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_assign_ips"><CopyableCode code="post_assign_ips" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-region"><code>region</code></a>, <a href="#parameter-assignments"><code>assignments</code></a></td>
    <td></td>
    <td>Assign any set of IPv4 addresses and IPv6 ranges to Linodes in one region. This allows swapping, shuffling, or otherwise reorganizing IPs among your Linodes.<br /><br />The following restrictions apply:<br /><br />- All Linodes need to have at least one public IPv4 address assigned.<br />  - For Linode interfaces, the Linode needs to have a public interface, and the address it receives can't be a private IPv4 address.<br />- Linodes may have no more than one assigned private IPv4 address.<br />- Linodes may have no more than one assigned IPv6 range.<br />- Shared IP addresses cannot be swapped between Linodes.<br /><br />[Open a support ticket](https://techdocs.akamai.com/linode-api/reference/post-ticket) to request additional IPv4 addresses or IPv6 ranges beyond standard account limits.<br /><br />&gt; 📘<br />&gt;<br />&gt; Removing an IP address that has been set as a Managed Linode's `ssh.ip` causes the Managed Linode's SSH access settings to reset to their default values.<br /><br />To view and configure Managed Linode SSH settings, use the following operations:<br /><br />- [Get a Linode's managed settings](https://techdocs.akamai.com/linode-api/reference/get-managed-linode-setting)<br />- [Update a Linode's managed settings](https://techdocs.akamai.com/linode-api/reference/put-managed-linode-setting)<br /><br />&gt; 📘<br />&gt;<br />&gt; Addresses with an active 1:1 NAT to a VPC Interface address cannot be assigned to other Linodes.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_share_ips"><CopyableCode code="post_share_ips" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-linode_id"><code>linode_id</code></a>, <a href="#parameter-ips"><code>ips</code></a></td>
    <td></td>
    <td>Configure shared IPs.<br /><br />IP sharing allows IP address reassignment (also referred to as IP failover) from one Linode to another if the primary Linode becomes unresponsive. This means that requests to the primary Linode's IP address can be automatically rerouted to secondary Linodes at the configured shared IP addresses.<br /><br />IP failover requires configuration of a [BGP based failover service](https://techdocs.akamai.com/cloud-computing/docs/configure-failover-on-a-compute-instance) within the internal system of the primary Linode.<br /><br />&gt; 📘<br />&gt;<br />&gt; A public IPv4 address can't be shared if it's configured for a 1:1 NAT on a legacy configuration profile VPC interface or on a Linode VPC interface.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
<tr id="parameter-skip_ipv6_rdns">
    <td><CopyableCode code="skip_ipv6_rdns" /></td>
    <td><code>boolean</code></td>
    <td>When `true`, the `rdns` property for any `ipv6` type addresses always returns `null` regardless of whether RDNS data exists for the address.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_ip"
    values={[
        { label: 'get_ip', value: 'get_ip' },
        { label: 'get_ips', value: 'get_ips' }
    ]}
>
<TabItem value="get_ip">

Returns information about a single IP Address on your Account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
interface_id,
linode_id,
address,
gateway,
prefix,
public,
rdns,
region,
subnet_mask,
type,
vpc_nat_1_1
FROM linode.networking.ip_addresses;
```
</TabItem>
<TabItem value="get_ips">

Returns a paginated list of IP addresses on your account for Linodes or Linode interfaces, excluding private addresses.<br /><br />&gt; 👍<br />&gt;<br />&gt; if your application frequently accesses this operation and doesn't require IPv6 RDNS data, you can use the `skip_ipv6_rdns` query string to improve performance.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
interface_id,
linode_id,
address,
gateway,
prefix,
public,
rdns,
region,
subnet_mask,
type,
vpc_nat_1_1
FROM linode.networking.ip_addresses
WHERE skip_ipv6_rdns = '{{ skip_ipv6_rdns }}';
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_ip"
    values={[
        { label: 'put_ip', value: 'put_ip' }
    ]}
>
<TabItem value="put_ip">

Sets RDNS on an IP Address. Forward DNS must already be set up for reverse DNS to be applied. If you set the RDNS to `null` for public IPv4 addresses, it will be reset to the default _ip.linodeusercontent.com_ RDNS value.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.networking.ip_addresses
SET 
data__rdns = '{{ rdns }}'
WHERE 
data__rdns = '{{ rdns }}' --required
RETURNING
interface_id,
linode_id,
address,
gateway,
prefix,
public,
rdns,
region,
subnet_mask,
type,
vpc_nat_1_1;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="post_allocate_ip"
    values={[
        { label: 'post_allocate_ip', value: 'post_allocate_ip' },
        { label: 'post_assign_ips', value: 'post_assign_ips' },
        { label: 'post_share_ips', value: 'post_share_ips' }
    ]}
>
<TabItem value="post_allocate_ip">

Allocates a new IPv4 Address on your Account. The Linode must be configured to support additional addresses - please [Open a support ticket](https://techdocs.akamai.com/linode-api/reference/post-ticket) requesting additional addresses before attempting allocation.<br /><br />&gt; 📘<br />&gt;<br />&gt; You can run this operation for Linodes with legacy configuration interfaces. You can't use it for Linodes with Linode interfaces. To allocate an IP for a Linode with Linode interfaces, use the [Add a Linode interface](https://techdocs.akamai.com/linode-api/reference/post-linode-interface) operation and set the public IPv4 address to `auto`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.networking.ip_addresses.post_allocate_ip 
@@json=
'{
"linode_id": {{ linode_id }}, 
"public": {{ public }}, 
"type": "{{ type }}"
}';
```
</TabItem>
<TabItem value="post_assign_ips">

Assign any set of IPv4 addresses and IPv6 ranges to Linodes in one region. This allows swapping, shuffling, or otherwise reorganizing IPs among your Linodes.<br /><br />The following restrictions apply:<br /><br />- All Linodes need to have at least one public IPv4 address assigned.<br />  - For Linode interfaces, the Linode needs to have a public interface, and the address it receives can't be a private IPv4 address.<br />- Linodes may have no more than one assigned private IPv4 address.<br />- Linodes may have no more than one assigned IPv6 range.<br />- Shared IP addresses cannot be swapped between Linodes.<br /><br />[Open a support ticket](https://techdocs.akamai.com/linode-api/reference/post-ticket) to request additional IPv4 addresses or IPv6 ranges beyond standard account limits.<br /><br />&gt; 📘<br />&gt;<br />&gt; Removing an IP address that has been set as a Managed Linode's `ssh.ip` causes the Managed Linode's SSH access settings to reset to their default values.<br /><br />To view and configure Managed Linode SSH settings, use the following operations:<br /><br />- [Get a Linode's managed settings](https://techdocs.akamai.com/linode-api/reference/get-managed-linode-setting)<br />- [Update a Linode's managed settings](https://techdocs.akamai.com/linode-api/reference/put-managed-linode-setting)<br /><br />&gt; 📘<br />&gt;<br />&gt; Addresses with an active 1:1 NAT to a VPC Interface address cannot be assigned to other Linodes.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.networking.ip_addresses.post_assign_ips 
@@json=
'{
"assignments": "{{ assignments }}", 
"region": "{{ region }}"
}';
```
</TabItem>
<TabItem value="post_share_ips">

Configure shared IPs.<br /><br />IP sharing allows IP address reassignment (also referred to as IP failover) from one Linode to another if the primary Linode becomes unresponsive. This means that requests to the primary Linode's IP address can be automatically rerouted to secondary Linodes at the configured shared IP addresses.<br /><br />IP failover requires configuration of a [BGP based failover service](https://techdocs.akamai.com/cloud-computing/docs/configure-failover-on-a-compute-instance) within the internal system of the primary Linode.<br /><br />&gt; 📘<br />&gt;<br />&gt; A public IPv4 address can't be shared if it's configured for a 1:1 NAT on a legacy configuration profile VPC interface or on a Linode VPC interface.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.networking.ip_addresses.post_share_ips 
@@json=
'{
"ips": "{{ ips }}", 
"linode_id": {{ linode_id }}
}';
```
</TabItem>
</Tabs>
