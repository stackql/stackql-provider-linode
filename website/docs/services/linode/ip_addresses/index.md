--- 
title: ip_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_addresses
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

Creates, updates, deletes, gets or lists an <code>ip_addresses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.linode.ip_addresses" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_linode_ip"
    values={[
        { label: 'get_linode_ip', value: 'get_linode_ip' },
        { label: 'get_linode_ips', value: 'get_linode_ips' }
    ]}
>
<TabItem value="get_linode_ip">

A single IP address.

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
<TabItem value="get_linode_ips">

Requested Linode's networking configuration.

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
    <td><CopyableCode code="ipv4" /></td>
    <td><code>object</code></td>
    <td>__Read-only__ Information about this Linode's IPv4 addresses.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv6" /></td>
    <td><code>object</code></td>
    <td>__Read-only__ Information about this Linode's IPv6 addresses.</td>
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
    <td><a href="#get_linode_ip"><CopyableCode code="get_linode_ip" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>View information for a Linode's set of IPs, its Linode interfaces and VPC IPs and ranges.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_linode_ips"><CopyableCode code="get_linode_ips" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns networking information for a single Linode.<br /><br />&gt; 📘<br />&gt;<br />&gt; If the target Linode has several configuration profiles that include a Virtual Private Cloud (VPC) interface, the response lists address information for all of the VPCs.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_add_linode_ip"><CopyableCode code="post_add_linode_ip" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__type"><code>data__type</code></a>, <a href="#parameter-data__public"><code>data__public</code></a></td>
    <td></td>
    <td>Allocates a public or private IPv4 address to a Linode. Public IP Addresses, after the one included with each Linode, incur an additional monthly charge. If you need an additional public IP Address you must request one - please [Open a support ticket](https://techdocs.akamai.com/linode-api/reference/post-ticket). You may not add more than one private IPv4 address to a single Linode.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_linode_ip"><CopyableCode code="put_linode_ip" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-data__rdns"><code>data__rdns</code></a></td>
    <td></td>
    <td>Updates the reverse DNS (RDNS) for a Linode's IP Address. This may be done for both IPv4 and IPv6 addresses.<br /><br />Setting the RDNS to `null` for a public IPv4 address, resets it to the default `ip.linodeusercontent.com` RDNS value.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_linode_ip"><CopyableCode code="delete_linode_ip" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes a public or private IPv4 address associated with this Linode. This will fail if it is the Linode's last remaining public IPv4 address, or if the address has a 1:1 NAT with an active VPC Subnet address.<br /><br />&gt; 📘<br />&gt;<br />&gt; You can't use this operation to delete an IP assigned to a Linode interface. Run the [update the Linode interface](https://techdocs.akamai.com/linode-api/reference/put-linode-interface) operation instead.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_linode_ip"
    values={[
        { label: 'get_linode_ip', value: 'get_linode_ip' },
        { label: 'get_linode_ips', value: 'get_linode_ips' }
    ]}
>
<TabItem value="get_linode_ip">

View information for a Linode's set of IPs, its Linode interfaces and VPC IPs and ranges.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

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
FROM linode.linode.ip_addresses;
```
</TabItem>
<TabItem value="get_linode_ips">

Returns networking information for a single Linode.<br /><br />&gt; 📘<br />&gt;<br />&gt; If the target Linode has several configuration profiles that include a Virtual Private Cloud (VPC) interface, the response lists address information for all of the VPCs.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
ipv4,
ipv6
FROM linode.linode.ip_addresses;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_add_linode_ip"
    values={[
        { label: 'post_add_linode_ip', value: 'post_add_linode_ip' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_add_linode_ip">

Allocates a public or private IPv4 address to a Linode. Public IP Addresses, after the one included with each Linode, incur an additional monthly charge. If you need an additional public IP Address you must request one - please [Open a support ticket](https://techdocs.akamai.com/linode-api/reference/post-ticket). You may not add more than one private IPv4 address to a single Linode.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.linode.ip_addresses (
data__public,
data__type
)
SELECT 
{{ public }} --required,
'{{ type }}' --required
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
vpc_nat_1_1
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: ip_addresses
  props:
    - name: public
      value: boolean
      description: >
        Whether to create a public or private IPv4 address.
        
    - name: type
      value: string
      description: >
        The type of address you are allocating. Only IPv4 addresses may be allocated through this operation.
        
      valid_values: ['ipv4']
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_linode_ip"
    values={[
        { label: 'put_linode_ip', value: 'put_linode_ip' }
    ]}
>
<TabItem value="put_linode_ip">

Updates the reverse DNS (RDNS) for a Linode's IP Address. This may be done for both IPv4 and IPv6 addresses.<br /><br />Setting the RDNS to `null` for a public IPv4 address, resets it to the default `ip.linodeusercontent.com` RDNS value.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.linode.ip_addresses
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


## `DELETE` examples

<Tabs
    defaultValue="delete_linode_ip"
    values={[
        { label: 'delete_linode_ip', value: 'delete_linode_ip' }
    ]}
>
<TabItem value="delete_linode_ip">

Deletes a public or private IPv4 address associated with this Linode. This will fail if it is the Linode's last remaining public IPv4 address, or if the address has a 1:1 NAT with an active VPC Subnet address.<br /><br />&gt; 📘<br />&gt;<br />&gt; You can't use this operation to delete an IP assigned to a Linode interface. Run the [update the Linode interface](https://techdocs.akamai.com/linode-api/reference/put-linode-interface) operation instead.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.linode.ip_addresses;
```
</TabItem>
</Tabs>
