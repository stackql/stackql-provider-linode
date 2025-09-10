--- 
title: vpcs
hide_title: false
hide_table_of_contents: false
keywords:
  - vpcs
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

Creates, updates, deletes, gets or lists a <code>vpcs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpcs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.vpcs.vpcs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_vpc"
    values={[
        { label: 'get_vpc', value: 'get_vpc' },
        { label: 'get_vpcs', value: 'get_vpcs' }
    ]}
>
<TabItem value="get_vpc">

A VPC object.

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
    <td>__Filterable__, __Read-only__ The unique ID of the VPC.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Filterable__, __Read-only__ The date-time of VPC creation. (example: 2023-07-11T00:00:00)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A written description to help distinguish the VPC. (default: , example: A description of my VPC.)</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The VPC's label, for display purposes only.  - Needs to be unique among the Account's VPCs. - Can only contain ASCII letters, numbers, and hyphens (`-`). You can't use two consecutive hyphens (`--`). (example: cool-vpc)</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The Region for the VPC. (example: us-east)</td>
</tr>
<tr>
    <td><CopyableCode code="subnets" /></td>
    <td><code>array</code></td>
    <td>A list of subnets associated with the VPC.</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Filterable__, __Read-only__ The date-time of the most recent VPC update. (example: 2023-09-11T00:00:00)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_vpcs">

A paginated list of VPC objects.

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
    <td>__Filterable__, __Read-only__ The unique ID of the VPC.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Filterable__, __Read-only__ The date-time of VPC creation. (example: 2023-07-11T00:00:00)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A written description to help distinguish the VPC. (default: , example: A description of my VPC.)</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The VPC's label, for display purposes only.  - Needs to be unique among the Account's VPCs. - Can only contain ASCII letters, numbers, and hyphens (`-`). You can't use two consecutive hyphens (`--`). (example: cool-vpc)</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The Region for the VPC. (example: us-east)</td>
</tr>
<tr>
    <td><CopyableCode code="subnets" /></td>
    <td><code>array</code></td>
    <td>A list of subnets associated with the VPC.</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Filterable__, __Read-only__ The date-time of the most recent VPC update. (example: 2023-09-11T00:00:00)</td>
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
    <td><a href="#get_vpc"><CopyableCode code="get_vpc" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get information about a single VPC.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)</td>
</tr>
<tr>
    <td><a href="#get_vpcs"><CopyableCode code="get_vpcs" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Display all VPCs on your account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)</td>
</tr>
<tr>
    <td><a href="#post_vpc"><CopyableCode code="post_vpc" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__label"><code>data__label</code></a>, <a href="#parameter-data__region"><code>data__region</code></a></td>
    <td></td>
    <td>Create a new VPC and optionally associated VPC Subnets.<br /><br />- Users must have the `add_vpc` grant to access this operation.<br />- A successful request triggers a `vpc_create` event and `subnet_create` events for any created VPC Subnets.<br /><br />Once a VPC is created, it can be attached to a Linode by assigning a VPC Subnet to one of the Linode's Configuration Profile Interfaces. This step can be accomplished with the following operations:<br /><br />- [Create a Linode](https://techdocs.akamai.com/linode-api/reference/post-linode-instance)<br />- [Create a config profile](https://techdocs.akamai.com/linode-api/reference/post-add-linode-config)<br />- [Update a config profile](https://techdocs.akamai.com/linode-api/reference/put-linode-config)<br />- [Add a configuration profile interface](https://techdocs.akamai.com/linode-api/reference/post-linode-config-interface)<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_vpc"><CopyableCode code="put_vpc" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Update an existing VPC.<br /><br />- The User accessing this operation must have `read_write` grants to the VPC.<br />- A successful request triggers a `vpc_update` event.<br /><br />To update a VPC's Subnet, run the [Update a VPC subnet](https://techdocs.akamai.com/linode-api/reference/put-vpc-subnet) operation.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_vpc"><CopyableCode code="delete_vpc" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Delete a single VPC and all of its Subnets.<br /><br />- The User accessing this operation must have `read_write` grants to the VPC.<br />- A successful request triggers a `vpc_delete` event and `subnet_delete` events for each deleted VPC Subnet.<br />- All of the VPC's Subnets must be eligible for deletion. Accordingly, all Configuration Profile Interfaces that each Subnet is assigned to must first be deleted. If those Interfaces are active, the associated Linodes must first be shut down before they can be removed. If any Subnet cannot be deleted, then neither the VPC nor any of its Subnets are deleted.<br />- You can't delete a VPC if a NodeBalancer is attached to one of its subnets.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_vpc"
    values={[
        { label: 'get_vpc', value: 'get_vpc' },
        { label: 'get_vpcs', value: 'get_vpcs' }
    ]}
>
<TabItem value="get_vpc">

Get information about a single VPC.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)

```sql
SELECT
id,
created,
description,
label,
region,
subnets,
updated
FROM linode.vpcs.vpcs;
```
</TabItem>
<TabItem value="get_vpcs">

Display all VPCs on your account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)

```sql
SELECT
id,
created,
description,
label,
region,
subnets,
updated
FROM linode.vpcs.vpcs
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}';
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_vpc"
    values={[
        { label: 'post_vpc', value: 'post_vpc' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_vpc">

Create a new VPC and optionally associated VPC Subnets.<br /><br />- Users must have the `add_vpc` grant to access this operation.<br />- A successful request triggers a `vpc_create` event and `subnet_create` events for any created VPC Subnets.<br /><br />Once a VPC is created, it can be attached to a Linode by assigning a VPC Subnet to one of the Linode's Configuration Profile Interfaces. This step can be accomplished with the following operations:<br /><br />- [Create a Linode](https://techdocs.akamai.com/linode-api/reference/post-linode-instance)<br />- [Create a config profile](https://techdocs.akamai.com/linode-api/reference/post-add-linode-config)<br />- [Update a config profile](https://techdocs.akamai.com/linode-api/reference/put-linode-config)<br />- [Add a configuration profile interface](https://techdocs.akamai.com/linode-api/reference/post-linode-config-interface)<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.vpcs.vpcs (
data__subnets,
data__description,
data__label,
data__region
)
SELECT 
'{{ subnets }}',
'{{ description }}',
'{{ label }}' --required,
'{{ region }}' --required
RETURNING
id,
created,
description,
label,
region,
subnets,
updated
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: vpcs
  props:
    - name: subnets
      value: array
      description: >
        A list of subnets associated with the VPC.
        
    - name: description
      value: string
      description: >
        A written description to help distinguish the VPC.
        
      default: 
    - name: label
      value: string
      description: >
        __Filterable__ The VPC's label, for display purposes only.

- Needs to be unique among the Account's VPCs.
- Can only contain ASCII letters, numbers, and hyphens (`-`). You can't use two consecutive hyphens (`--`).
        
    - name: region
      value: string
      description: >
        __Filterable__ The Region for the VPC.
        
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_vpc"
    values={[
        { label: 'put_vpc', value: 'put_vpc' }
    ]}
>
<TabItem value="put_vpc">

Update an existing VPC.<br /><br />- The User accessing this operation must have `read_write` grants to the VPC.<br />- A successful request triggers a `vpc_update` event.<br /><br />To update a VPC's Subnet, run the [Update a VPC subnet](https://techdocs.akamai.com/linode-api/reference/put-vpc-subnet) operation.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.vpcs.vpcs
SET 
data__description = '{{ description }}',
data__label = '{{ label }}'
WHERE 

RETURNING
id,
created,
description,
label,
region,
subnets,
updated;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_vpc"
    values={[
        { label: 'delete_vpc', value: 'delete_vpc' }
    ]}
>
<TabItem value="delete_vpc">

Delete a single VPC and all of its Subnets.<br /><br />- The User accessing this operation must have `read_write` grants to the VPC.<br />- A successful request triggers a `vpc_delete` event and `subnet_delete` events for each deleted VPC Subnet.<br />- All of the VPC's Subnets must be eligible for deletion. Accordingly, all Configuration Profile Interfaces that each Subnet is assigned to must first be deleted. If those Interfaces are active, the associated Linodes must first be shut down before they can be removed. If any Subnet cannot be deleted, then neither the VPC nor any of its Subnets are deleted.<br />- You can't delete a VPC if a NodeBalancer is attached to one of its subnets.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.vpcs.vpcs;
```
</TabItem>
</Tabs>
