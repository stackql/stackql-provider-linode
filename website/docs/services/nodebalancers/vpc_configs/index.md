--- 
title: vpc_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_configs
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

Creates, updates, deletes, gets or lists a <code>vpc_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.nodebalancers.vpc_configs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_node_balancer_vpc_config"
    values={[
        { label: 'get_node_balancer_vpc_config', value: 'get_node_balancer_vpc_config' },
        { label: 'get_node_balancer_vpcs', value: 'get_node_balancer_vpcs' }
    ]}
>
<TabItem value="get_node_balancer_vpc_config">

The requested NodeBalancer VPC configuration.

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
    <td>__Read-only__ Identifies the VPC configuration for this NodeBalancer.</td>
</tr>
<tr>
    <td><CopyableCode code="nodebalancer_id" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ Identifies the NodeBalancer.</td>
</tr>
<tr>
    <td><CopyableCode code="subnet_id" /></td>
    <td><code>integer</code></td>
    <td>The VPC's subnet. Run the [List VPCs](https://techdocs.akamai.com/linode-api/reference/get-vpcs) operation provides data for your VPCs and their subnets.</td>
</tr>
<tr>
    <td><CopyableCode code="vpc_id" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The `id` of the VPC configured for this NodeBalancer.</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4_range" /></td>
    <td><code>string</code></td>
    <td>A CIDR range for the VPC's IPv4 addresses. The NodeBalancer sources IP addresses from this range when routing traffic to the backend VPC nodes. (example: 10.100.5.100/30)</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4_range_auto_assign" /></td>
    <td><code>boolean</code></td>
    <td>Enables the use of a larger `ipv4_range` subnet for multiple NodeBalancers within the same VPC by allocating smaller `/30` subnets for each NodeBalancer's backends.  - When set to `true`, the system automatically allocates the smallest possible subnet (`/30`) from the provided `ipv4_range` for the NodeBalancer's backend interface. If the specified range doesn't have enough available IPs to allocate a `/30` subnet, the creation fails.  - When set to `false`, the NodeBalancer is created using the entire `ipv4_range` as specified, without attempting to allocate a `/30` subnet.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_node_balancer_vpcs">

A paginated list of NodeBalancer VPC configurations.

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
    <td><a href="#get_node_balancer_vpc_config"><CopyableCode code="get_node_balancer_vpc_config" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns a single VPC configuration for the NodeBalancer ID.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_node_balancer_vpcs"><CopyableCode code="get_node_balancer_vpcs" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Returns a paginated list of VPC configurations for the NodeBalancer.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_node_balancer_vpc_config"
    values={[
        { label: 'get_node_balancer_vpc_config', value: 'get_node_balancer_vpc_config' },
        { label: 'get_node_balancer_vpcs', value: 'get_node_balancer_vpcs' }
    ]}
>
<TabItem value="get_node_balancer_vpc_config">

Returns a single VPC configuration for the NodeBalancer ID.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
nodebalancer_id,
subnet_id,
vpc_id,
ipv4_range,
ipv4_range_auto_assign
FROM linode.nodebalancers.vpc_configs;
```
</TabItem>
<TabItem value="get_node_balancer_vpcs">

Returns a paginated list of VPC configurations for the NodeBalancer.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.nodebalancers.vpc_configs
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}';
```
</TabItem>
</Tabs>
