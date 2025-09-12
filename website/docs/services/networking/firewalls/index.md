--- 
title: firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls
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

Creates, updates, deletes, gets or lists a <code>firewalls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.networking.firewalls" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_firewall"
    values={[
        { label: 'get_firewall', value: 'get_firewall' },
        { label: 'get_firewalls', value: 'get_firewalls' }
    ]}
>
<TabItem value="get_firewall">

Returns information about this Firewall.

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
    <td>__Filterable__, __Read-only__ The Firewall's unique ID.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Filterable__, __Read-only__ When this Firewall was created. (example: 2018-01-01T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The Firewall's label, for display purposes only.  Firewall labels have the following constraints:    - Must begin and end with an alphanumeric character.   - May only consist of alphanumeric characters, hyphens (`-`), underscores (`_`) or periods (`.`).   - Cannot have two hyphens (`--`), underscores (`__`) or periods (`..`) in a row.   - Must be between 3 and 32 characters.   - Must be unique. (example: firewall123, pattern: <code>^[a-zA-Z]((?!--|__|\.\.)[a-zA-Z0-9-_.])+$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="rules" /></td>
    <td><code>object</code></td>
    <td>The inbound and outbound access rules to apply to the Firewall.  A Firewall may have up to 25 rules across its inbound and outbound rulesets.  Multiple rules are applied in order. If two rules conflict, the first rule takes precedence. For example, if the first rule accepts inbound traffic from an address, and the second rule drops inbound traffic the same address, the first rule applies and inbound traffic from that address is accepted.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The status of this Firewall.    - When a Firewall is first created its status is `enabled`.   - Run the [Update a firewall](https://techdocs.akamai.com/linode-api/reference/put-firewall) operation to set a Firewall's status to `enabled` or `disabled`.   - Run the [Delete a firewall](https://techdocs.akamai.com/linode-api/reference/delete-firewall) operation to delete a Firewall. (example: enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>__Filterable__ An array of tags applied to this object. Tags are for organizational purposes only.</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Filterable__, __Read-only__ When this Firewall was last updated. (example: 2018-01-02T00:01:01)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_firewalls">

Returns an array of Firewalls.

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
    <td><a href="#get_firewall"><CopyableCode code="get_firewall" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a specific Firewall resource by its ID. The Firewall's Devices will not be returned in the response. Instead, run the [List firewall devices](https://techdocs.akamai.com/linode-api/reference/get-firewall-devices) operation to review them.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_firewalls"><CopyableCode code="get_firewalls" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Returns a paginated list of accessible Firewalls.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_firewalls"><CopyableCode code="post_firewalls" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__label"><code>data__label</code></a>, <a href="#parameter-data__rules"><code>data__rules</code></a></td>
    <td></td>
    <td>Creates a Firewall to filter network traffic.<br /><br />- Use `rules` to create inbound and outbound access rules. Rule versions increment from `1` whenever the firewall's `rules` change.<br /><br />- Use `devices` to assign a firewall to a service such as a Linode that is using legacy config profiles, a Linode interface or a NodeBalancer. The firewall’s rules are then applied to that service. Requires a `read_write` [user grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) to the device.<br /><br />  - For Linodes using Linode interfaces, firewalls need to be assigned to `interfaces` and not the `linodes`. Firewall templates are available for both VPC Linode interfaces and public Linode interfaces, and come with pre-configured protection rules.<br /><br />  - For Linodes using legacy configuration profiles, firewalls are applied through the Linode. Public and VPC interfaces are subject to the firewall rules, while VLAN interfaces are not.<br /><br />- Currently, firewalls can be assigned to Linodes with legacy configuration profiles, Linode interfaces, and NodeBalancers.<br /><br />    - The same firewall can be assigned to multiple services at a time.<br /><br />- Use `firewall_id` to assign a firewall when [creating a Linode](https://techdocs.akamai.com/linode-api/reference/post-linode-instance) or when [adding a Linode interface](https://techdocs.akamai.com/linode-api/reference/post-linode-interface).<br /><br />- A service can have one assigned firewall enabled at a time.<br /><br />- Assigned Linodes must not have any ongoing live migrations.<br /><br />- A `firewall_create` event is generated when this operation succeeds.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_firewall"><CopyableCode code="put_firewall" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Updates information for a firewall.<br /><br />- Assigned Linodes must not have any ongoing live migrations.<br /><br />- If this operation changes a firewall's status, it generates a corresponding `firewall_enable` or `firewall_disable` event.<br /><br />This operation doesn't affect some parts of a firewall's configuration:<br /><br />- This operation doesn't set a firewall's devices. Instead, run the [Create a firewall device](https://techdocs.akamai.com/linode-api/reference/post-firewall-device) and [Delete a firewall device](https://techdocs.akamai.com/linode-api/reference/delete-firewall-device) operations to assign and remove this firewall from services.<br /><br />- A firewall's rules can't be changed with this operation. Instead, run the [Update firewall rules](https://techdocs.akamai.com/linode-api/reference/put-firewall-rules) operation to update your rules.<br /><br />- Use this operation to set a firewall's status to `enabled` or `disabled`.  But to set it to `deleted`, run the [Delete a firewall](https://techdocs.akamai.com/linode-api/reference/delete-firewall) operation.<br /><br />- An assigned default firewall can't be disabled.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_firewall"><CopyableCode code="delete_firewall" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Delete a firewall. This also removes all of the firewall's rules from any services the firewall was assigned to.<br /><br />- Assigned Linodes must not have any ongoing live migrations.<br /><br />- A `firewall_delete` event is generated when this operation returns successfully.<br /><br />- An assigned default firewall can't be deleted.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_firewall"
    values={[
        { label: 'get_firewall', value: 'get_firewall' },
        { label: 'get_firewalls', value: 'get_firewalls' }
    ]}
>
<TabItem value="get_firewall">

Get a specific Firewall resource by its ID. The Firewall's Devices will not be returned in the response. Instead, run the [List firewall devices](https://techdocs.akamai.com/linode-api/reference/get-firewall-devices) operation to review them.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
created,
label,
rules,
status,
tags,
updated
FROM linode.networking.firewalls
;
```
</TabItem>
<TabItem value="get_firewalls">

Returns a paginated list of accessible Firewalls.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.networking.firewalls
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_firewalls"
    values={[
        { label: 'post_firewalls', value: 'post_firewalls' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_firewalls">

Creates a Firewall to filter network traffic.<br /><br />- Use `rules` to create inbound and outbound access rules. Rule versions increment from `1` whenever the firewall's `rules` change.<br /><br />- Use `devices` to assign a firewall to a service such as a Linode that is using legacy config profiles, a Linode interface or a NodeBalancer. The firewall’s rules are then applied to that service. Requires a `read_write` [user grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) to the device.<br /><br />  - For Linodes using Linode interfaces, firewalls need to be assigned to `interfaces` and not the `linodes`. Firewall templates are available for both VPC Linode interfaces and public Linode interfaces, and come with pre-configured protection rules.<br /><br />  - For Linodes using legacy configuration profiles, firewalls are applied through the Linode. Public and VPC interfaces are subject to the firewall rules, while VLAN interfaces are not.<br /><br />- Currently, firewalls can be assigned to Linodes with legacy configuration profiles, Linode interfaces, and NodeBalancers.<br /><br />    - The same firewall can be assigned to multiple services at a time.<br /><br />- Use `firewall_id` to assign a firewall when [creating a Linode](https://techdocs.akamai.com/linode-api/reference/post-linode-instance) or when [adding a Linode interface](https://techdocs.akamai.com/linode-api/reference/post-linode-interface).<br /><br />- A service can have one assigned firewall enabled at a time.<br /><br />- Assigned Linodes must not have any ongoing live migrations.<br /><br />- A `firewall_create` event is generated when this operation succeeds.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.networking.firewalls (
data__label,
data__rules,
data__tags
)
SELECT 
'{{ label }}' /* required */,
'{{ rules }}' /* required */,
'{{ tags }}'
RETURNING
id,
created,
label,
rules,
status,
tags,
updated
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: firewalls
  props:
    - name: label
      value: string
      description: >
        __Filterable__ The Firewall's label, for display purposes only.

Firewall labels have the following constraints:

  - Must begin and end with an alphanumeric character.
  - May only consist of alphanumeric characters, hyphens (`-`), underscores (`_`) or periods (`.`).
  - Cannot have two hyphens (`--`), underscores (`__`) or periods (`..`) in a row.
  - Must be between 3 and 32 characters.
  - Must be unique.
        
    - name: rules
      value: object
      description: >
        The inbound and outbound access rules to apply to the Firewall.

A Firewall may have up to 25 rules across its inbound and outbound rulesets.

Multiple rules are applied in order. If two rules conflict, the first rule takes precedence. For example, if the first rule accepts inbound traffic from an address, and the second rule drops inbound traffic the same address, the first rule applies and inbound traffic from that address is accepted.
        
    - name: tags
      value: array
      description: >
        __Filterable__ An array of tags applied to this object. Tags are for organizational purposes only.
        
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_firewall"
    values={[
        { label: 'put_firewall', value: 'put_firewall' }
    ]}
>
<TabItem value="put_firewall">

Updates information for a firewall.<br /><br />- Assigned Linodes must not have any ongoing live migrations.<br /><br />- If this operation changes a firewall's status, it generates a corresponding `firewall_enable` or `firewall_disable` event.<br /><br />This operation doesn't affect some parts of a firewall's configuration:<br /><br />- This operation doesn't set a firewall's devices. Instead, run the [Create a firewall device](https://techdocs.akamai.com/linode-api/reference/post-firewall-device) and [Delete a firewall device](https://techdocs.akamai.com/linode-api/reference/delete-firewall-device) operations to assign and remove this firewall from services.<br /><br />- A firewall's rules can't be changed with this operation. Instead, run the [Update firewall rules](https://techdocs.akamai.com/linode-api/reference/put-firewall-rules) operation to update your rules.<br /><br />- Use this operation to set a firewall's status to `enabled` or `disabled`.  But to set it to `deleted`, run the [Delete a firewall](https://techdocs.akamai.com/linode-api/reference/delete-firewall) operation.<br /><br />- An assigned default firewall can't be disabled.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.networking.firewalls
SET 
data__label = '{{ label }}',
data__status = '{{ status }}',
data__tags = '{{ tags }}'
RETURNING
id,
created,
label,
rules,
status,
tags,
updated;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_firewall"
    values={[
        { label: 'delete_firewall', value: 'delete_firewall' }
    ]}
>
<TabItem value="delete_firewall">

Delete a firewall. This also removes all of the firewall's rules from any services the firewall was assigned to.<br /><br />- Assigned Linodes must not have any ongoing live migrations.<br /><br />- A `firewall_delete` event is generated when this operation returns successfully.<br /><br />- An assigned default firewall can't be deleted.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.networking.firewalls
;
```
</TabItem>
</Tabs>
