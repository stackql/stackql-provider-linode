--- 
title: firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls
  - nodebalancers
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
<tr><td><b>Id</b></td><td><CopyableCode code="linode.nodebalancers.firewalls" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_node_balancer_firewalls"
    values={[
        { label: 'get_node_balancer_firewalls', value: 'get_node_balancer_firewalls' }
    ]}
>
<TabItem value="get_node_balancer_firewalls">

Returns a paginated list of Firewalls assigned to this NodeBalancer.

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
    <td><a href="#get_node_balancer_firewalls"><CopyableCode code="get_node_balancer_firewalls" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>View information for Firewalls assigned to this NodeBalancer.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_node_balancer_firewalls"><CopyableCode code="put_node_balancer_firewalls" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-data__firewall_ids"><code>data__firewall_ids</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Replace the current list of assigned firewalls with a new list, or provide an empty list to remove all firewalls from this NodeBalancer.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_node_balancer_firewalls"
    values={[
        { label: 'get_node_balancer_firewalls', value: 'get_node_balancer_firewalls' }
    ]}
>
<TabItem value="get_node_balancer_firewalls">

View information for Firewalls assigned to this NodeBalancer.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
created,
label,
rules,
status,
tags,
updated
FROM linode.nodebalancers.firewalls
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_node_balancer_firewalls"
    values={[
        { label: 'put_node_balancer_firewalls', value: 'put_node_balancer_firewalls' }
    ]}
>
<TabItem value="put_node_balancer_firewalls">

Replace the current list of assigned firewalls with a new list, or provide an empty list to remove all firewalls from this NodeBalancer.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.nodebalancers.firewalls
SET 
data__firewall_ids = '{{ firewall_ids }}'
WHERE 
data__firewall_ids = '{{ firewall_ids }}' --required
AND page = '{{ page}}'
AND page_size = '{{ page_size}}'
RETURNING
data,
page,
pages,
results;
```
</TabItem>
</Tabs>
