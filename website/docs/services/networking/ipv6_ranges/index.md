--- 
title: ipv6_ranges
hide_title: false
hide_table_of_contents: false
keywords:
  - ipv6_ranges
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

Creates, updates, deletes, gets or lists an <code>ipv6_ranges</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipv6_ranges</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.networking.ipv6_ranges" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_ipv6_range"
    values={[
        { label: 'get_ipv6_range', value: 'get_ipv6_range' },
        { label: 'get_ipv6_ranges', value: 'get_ipv6_ranges' }
    ]}
>
<TabItem value="get_ipv6_range">

Returns IPv6 range information.

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
    <td><CopyableCode code="is_bgp" /></td>
    <td><code>boolean</code></td>
    <td>__Read-only__ Whether this IPv6 range is shared.</td>
</tr>
<tr>
    <td><CopyableCode code="linodes" /></td>
    <td><code>array</code></td>
    <td>__Read-only__ A list of Linodes targeted by this IPv6 range. Includes Linodes with IP sharing.</td>
</tr>
<tr>
    <td><CopyableCode code="prefix" /></td>
    <td><code>integer</code></td>
    <td>The prefix length of the address. The total number of addresses that can be assigned from this range is calculated as 2&lt;sup&gt;(128 - prefix length)&lt;/sup&gt;.</td>
</tr>
<tr>
    <td><CopyableCode code="range" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The IPv6 address of this range. (example: 2600:3c01::)</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The region for this range of IPv6 addresses. (example: us-east)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_ipv6_ranges">

The IPv6 ranges on your Account.

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
    <td><a href="#get_ipv6_range"><CopyableCode code="get_ipv6_range" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>View IPv6 range information.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_ipv6_ranges"><CopyableCode code="get_ipv6_ranges" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Displays the IPv6 ranges on your Account.<br /><br />  - An IPv6 range is a `/64` or `/56` block of IPv6 addresses routed to a single Linode in a given [region](https://techdocs.akamai.com/linode-api/reference/get-regions).<br /><br />  - Your Linode is responsible for routing individual addresses in the range, or handling traffic for all the addresses in the range.<br /><br />  - Run the [Create an IPv6 range](https://techdocs.akamai.com/linode-api/reference/post-ipv6-range) operation to add a `/64` or `/56` block of IPv6 addresses to your account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_ipv6_range"><CopyableCode code="post_ipv6_range" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__prefix_length"><code>data__prefix_length</code></a></td>
    <td></td>
    <td>Creates an IPv6 Range and assigns it based on the provided Linode or route target IPv6 SLAAC address. See the `ipv6` property when running the [Get a Linode](https://techdocs.akamai.com/linode-api/reference/get-linode-instance) operation to view a Linode's IPv6 SLAAC address.<br /><br />- Either `linode_id` or `route_target` is required in a request.<br />- `linode_id` and `route_target` are mutually exclusive. Submitting values for both properties in a request results in an error.<br />- Upon a successful request, an IPv6 range is created in the [region](https://techdocs.akamai.com/linode-api/reference/get-regions) that corresponds to the provided `linode_id` or `route_target`.<br />- Your Linode is responsible for routing individual addresses in the range, or handling traffic for all the addresses in the range.<br />- Run the [Assign IP addresses](https://techdocs.akamai.com/linode-api/reference/post-assign-ips) operation to re-assign IPv6 Ranges to your Linodes.<br /><br />&gt; 📘<br />&gt;<br />&gt; - A Linode can only have one IPv6 range targeting its SLAAC address.<br />&gt; - An account can only have one IPv6 range in each [region](https://techdocs.akamai.com/linode-api/reference/get-regions).<br />&gt; - [Open a support ticket](https://techdocs.akamai.com/linode-api/reference/post-ticket) to request expansion of these restrictions.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_ipv6_range"><CopyableCode code="delete_ipv6_range" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Removes this IPv6 range from your account and disconnects the range from any assigned Linodes.<br /><br />&gt; 📘<br />&gt;<br />&gt; You can't delete shared IPv6 ranges. Contact Customer Support for assistance.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_ipv6_range"
    values={[
        { label: 'get_ipv6_range', value: 'get_ipv6_range' },
        { label: 'get_ipv6_ranges', value: 'get_ipv6_ranges' }
    ]}
>
<TabItem value="get_ipv6_range">

View IPv6 range information.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
is_bgp,
linodes,
prefix,
range,
region
FROM linode.networking.ipv6_ranges
;
```
</TabItem>
<TabItem value="get_ipv6_ranges">

Displays the IPv6 ranges on your Account.<br /><br />  - An IPv6 range is a `/64` or `/56` block of IPv6 addresses routed to a single Linode in a given [region](https://techdocs.akamai.com/linode-api/reference/get-regions).<br /><br />  - Your Linode is responsible for routing individual addresses in the range, or handling traffic for all the addresses in the range.<br /><br />  - Run the [Create an IPv6 range](https://techdocs.akamai.com/linode-api/reference/post-ipv6-range) operation to add a `/64` or `/56` block of IPv6 addresses to your account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.networking.ipv6_ranges
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_ipv6_range"
    values={[
        { label: 'post_ipv6_range', value: 'post_ipv6_range' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_ipv6_range">

Creates an IPv6 Range and assigns it based on the provided Linode or route target IPv6 SLAAC address. See the `ipv6` property when running the [Get a Linode](https://techdocs.akamai.com/linode-api/reference/get-linode-instance) operation to view a Linode's IPv6 SLAAC address.<br /><br />- Either `linode_id` or `route_target` is required in a request.<br />- `linode_id` and `route_target` are mutually exclusive. Submitting values for both properties in a request results in an error.<br />- Upon a successful request, an IPv6 range is created in the [region](https://techdocs.akamai.com/linode-api/reference/get-regions) that corresponds to the provided `linode_id` or `route_target`.<br />- Your Linode is responsible for routing individual addresses in the range, or handling traffic for all the addresses in the range.<br />- Run the [Assign IP addresses](https://techdocs.akamai.com/linode-api/reference/post-assign-ips) operation to re-assign IPv6 Ranges to your Linodes.<br /><br />&gt; 📘<br />&gt;<br />&gt; - A Linode can only have one IPv6 range targeting its SLAAC address.<br />&gt; - An account can only have one IPv6 range in each [region](https://techdocs.akamai.com/linode-api/reference/get-regions).<br />&gt; - [Open a support ticket](https://techdocs.akamai.com/linode-api/reference/post-ticket) to request expansion of these restrictions.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.networking.ipv6_ranges (
data__linode_id,
data__prefix_length,
data__route_target
)
SELECT 
{{ linode_id }},
{{ prefix_length }} /* required */,
'{{ route_target }}'
RETURNING
range,
route_target
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: ipv6_ranges
  props:
    - name: linode_id
      value: integer
      description: >
        The ID of the Linode to assign this range to. The SLAAC address for the provided Linode is used as the range's `route_target`.

- __Required__ if `route_target` is omitted from the request.

- Mutually exclusive with `route_target`. Submitting values for both properties in a request results in an error.
        
    - name: prefix_length
      value: integer
      description: >
        The prefix length of the IPv6 range.
        
      valid_values: ['56', '64']
    - name: route_target
      value: string
      description: >
        The IPv6 SLAAC address to assign this range to.

- __Required__ if `linode_id` is omitted from the request.

- Mutually exclusive with `linode_id`. Submitting values for both properties in a request results in an error.

> 📘
>
> You need to omit the `/128` prefix length of the SLAAC address when using this property.
        
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_ipv6_range"
    values={[
        { label: 'delete_ipv6_range', value: 'delete_ipv6_range' }
    ]}
>
<TabItem value="delete_ipv6_range">

Removes this IPv6 range from your account and disconnects the range from any assigned Linodes.<br /><br />&gt; 📘<br />&gt;<br />&gt; You can't delete shared IPv6 ranges. Contact Customer Support for assistance.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.networking.ipv6_ranges
;
```
</TabItem>
</Tabs>
