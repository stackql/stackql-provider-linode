--- 
title: subnets
hide_title: false
hide_table_of_contents: false
keywords:
  - subnets
  - vpcs
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

Creates, updates, deletes, gets or lists a <code>subnets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.vpcs.subnets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_vpc_subnet"
    values={[
        { label: 'get_vpc_subnet', value: 'get_vpc_subnet' },
        { label: 'get_vpc_subnets', value: 'get_vpc_subnets' }
    ]}
>
<TabItem value="get_vpc_subnet">

A VPC Subnet object.

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
    <td>__Filterable__, __Read-only__ The unique ID of the VPC Subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Filterable__, __Read-only__ The date-time of VPC Subnet creation. (example: 2023-07-11T00:00:00)</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4" /></td>
    <td><code>string (ip)</code></td>
    <td>IPv4 range in CIDR canonical form.  - The range must belong to a private address space as defined in [RFC1918](https://datatracker.ietf.org/doc/html/rfc1918). - Allowed prefix lengths: 1-29. - The range must not overlap with 192.168.128.0/17. - The range must not overlap with other Subnets on the same VPC. (example: 10.0.1.0/24)</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The VPC Subnet's label, for display purposes only.  - Must be unique among the VPC's Subnets. - Can only contain ASCII letters, numbers, and hyphens (`-`). You can't use two consecutive hyphens (`--`). (example: cool-vpc-subnet)</td>
</tr>
<tr>
    <td><CopyableCode code="linodes" /></td>
    <td><code>array</code></td>
    <td>__Read-only__ An array of Linode IDs assigned to the VPC Subnet.  A Linode is assigned to a VPC Subnet if it has a Configuration Profile with a `vpc` purpose interface with the subnet's `subnet_id`. Even if the Configuration Profile is not active, meaning the Linode does not have access to the Subnet, the Linode still appears in this array.</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Filterable__, __Read-only__ The date-time of the most recent VPC Subnet update. (example: 2023-09-11T00:00:00)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_vpc_subnets">

A paginated list of VPC Subnet objects.

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
    <td>__Filterable__, __Read-only__ The unique ID of the VPC Subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Filterable__, __Read-only__ The date-time of VPC Subnet creation. (example: 2023-07-11T00:00:00)</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4" /></td>
    <td><code>string (ip)</code></td>
    <td>IPv4 range in CIDR canonical form.  - The range must belong to a private address space as defined in [RFC1918](https://datatracker.ietf.org/doc/html/rfc1918). - Allowed prefix lengths: 1-29. - The range must not overlap with 192.168.128.0/17. - The range must not overlap with other Subnets on the same VPC. (example: 10.0.1.0/24)</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The VPC Subnet's label, for display purposes only.  - Must be unique among the VPC's Subnets. - Can only contain ASCII letters, numbers, and hyphens (`-`). You can't use two consecutive hyphens (`--`). (example: cool-vpc-subnet)</td>
</tr>
<tr>
    <td><CopyableCode code="linodes" /></td>
    <td><code>array</code></td>
    <td>__Read-only__ An array of Linode IDs assigned to the VPC Subnet.  A Linode is assigned to a VPC Subnet if it has a Configuration Profile with a `vpc` purpose interface with the subnet's `subnet_id`. Even if the Configuration Profile is not active, meaning the Linode does not have access to the Subnet, the Linode still appears in this array.</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Filterable__, __Read-only__ The date-time of the most recent VPC Subnet update. (example: 2023-09-11T00:00:00)</td>
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
    <td><a href="#get_vpc_subnet"><CopyableCode code="get_vpc_subnet" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get information about a single VPC Subnet.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)</td>
</tr>
<tr>
    <td><a href="#get_vpc_subnets"><CopyableCode code="get_vpc_subnets" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Get information about all VPC Subnets associated with a VPC.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)</td>
</tr>
<tr>
    <td><a href="#post_vpc_subnet"><CopyableCode code="post_vpc_subnet" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__ipv4"><code>data__ipv4</code></a>, <a href="#parameter-data__label"><code>data__label</code></a></td>
    <td></td>
    <td>Create a VPC Subnet.<br /><br />- The User accessing this operation must have `read_write` grants to the VPC.<br />- A successful request triggers a `subnet_create` event.<br /><br />Once a VPC Subnet is created, it can be attached to a Linode by assigning the Subnet to one of the Linode's Configuration Profile Interfaces. This step can be accomplished with the following operations:<br /><br />- [Create a Linode](https://techdocs.akamai.com/linode-api/reference/post-linode-instance)<br />- [Create a config profile](https://techdocs.akamai.com/linode-api/reference/post-add-linode-config)<br />- [Update a config profile](https://techdocs.akamai.com/linode-api/reference/put-linode-config)<br />- [Add a configuration profile interface](https://techdocs.akamai.com/linode-api/reference/post-linode-config-interface)<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_vpc_subnet"><CopyableCode code="put_vpc_subnet" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Update a VPC Subnet.<br /><br />- The User accessing this operation must have `read_write` grants to the VPC.<br />- A successful request triggers a `subnet_update` event.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_vpc_subnet"><CopyableCode code="delete_vpc_subnet" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Delete a single VPC subnet.<br /><br />The user accessing this operation must have `read_write` grants to the VPC. A successful request triggers a `subnet_delete` event.<br /><br />&gt; 📘<br />&gt;<br />&gt; You need to delete all the Configuration Profile Interfaces that this subnet is assigned to before you can delete it. If those interfaces are active, the associated Linode needs to be shut down before they can be removed.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_vpc_subnet"
    values={[
        { label: 'get_vpc_subnet', value: 'get_vpc_subnet' },
        { label: 'get_vpc_subnets', value: 'get_vpc_subnets' }
    ]}
>
<TabItem value="get_vpc_subnet">

Get information about a single VPC Subnet.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)

```sql
SELECT
id,
created,
ipv4,
label,
linodes,
updated
FROM linode.vpcs.subnets
;
```
</TabItem>
<TabItem value="get_vpc_subnets">

Get information about all VPC Subnets associated with a VPC.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)

```sql
SELECT
id,
created,
ipv4,
label,
linodes,
updated
FROM linode.vpcs.subnets
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_vpc_subnet"
    values={[
        { label: 'post_vpc_subnet', value: 'post_vpc_subnet' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_vpc_subnet">

Create a VPC Subnet.<br /><br />- The User accessing this operation must have `read_write` grants to the VPC.<br />- A successful request triggers a `subnet_create` event.<br /><br />Once a VPC Subnet is created, it can be attached to a Linode by assigning the Subnet to one of the Linode's Configuration Profile Interfaces. This step can be accomplished with the following operations:<br /><br />- [Create a Linode](https://techdocs.akamai.com/linode-api/reference/post-linode-instance)<br />- [Create a config profile](https://techdocs.akamai.com/linode-api/reference/post-add-linode-config)<br />- [Update a config profile](https://techdocs.akamai.com/linode-api/reference/put-linode-config)<br />- [Add a configuration profile interface](https://techdocs.akamai.com/linode-api/reference/post-linode-config-interface)<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.vpcs.subnets (
data__ipv4,
data__label
)
SELECT 
'{{ ipv4 }}' /* required */,
'{{ label }}' /* required */
RETURNING
id,
created,
ipv4,
label,
linodes,
updated
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: subnets
  props:
    - name: ipv4
      value: string
      description: >
        IPv4 range in CIDR canonical form.

- The range must belong to a private address space as defined in [RFC1918](https://datatracker.ietf.org/doc/html/rfc1918).
- Allowed prefix lengths: 1-29.
- The range must not overlap with 192.168.128.0/17.
- The range must not overlap with other Subnets on the same VPC.
        
    - name: label
      value: string
      description: >
        __Filterable__ The VPC Subnet's label, for display purposes only.

- Must be unique among the VPC's Subnets.
- Can only contain ASCII letters, numbers, and hyphens (`-`). You can't use two consecutive hyphens (`--`).
        
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_vpc_subnet"
    values={[
        { label: 'put_vpc_subnet', value: 'put_vpc_subnet' }
    ]}
>
<TabItem value="put_vpc_subnet">

Update a VPC Subnet.<br /><br />- The User accessing this operation must have `read_write` grants to the VPC.<br />- A successful request triggers a `subnet_update` event.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.vpcs.subnets
SET 
data__label = '{{ label }}'
RETURNING
id,
created,
ipv4,
label,
linodes,
updated;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_vpc_subnet"
    values={[
        { label: 'delete_vpc_subnet', value: 'delete_vpc_subnet' }
    ]}
>
<TabItem value="delete_vpc_subnet">

Delete a single VPC subnet.<br /><br />The user accessing this operation must have `read_write` grants to the VPC. A successful request triggers a `subnet_delete` event.<br /><br />&gt; 📘<br />&gt;<br />&gt; You need to delete all the Configuration Profile Interfaces that this subnet is assigned to before you can delete it. If those interfaces are active, the associated Linode needs to be shut down before they can be removed.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.vpcs.subnets
;
```
</TabItem>
</Tabs>
