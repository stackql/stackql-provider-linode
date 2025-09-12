--- 
title: node_balancers
hide_title: false
hide_table_of_contents: false
keywords:
  - node_balancers
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

Creates, updates, deletes, gets or lists a <code>node_balancers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_balancers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.nodebalancers.node_balancers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_node_balancer"
    values={[
        { label: 'get_node_balancer', value: 'get_node_balancer' },
        { label: 'get_node_balancers', value: 'get_node_balancers' }
    ]}
>
<TabItem value="get_node_balancer">

The requested NodeBalancer object.

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
    <td>__Read-only__ This NodeBalancer's unique ID.</td>
</tr>
<tr>
    <td><CopyableCode code="client_conn_throttle" /></td>
    <td><code>integer</code></td>
    <td>Throttle TCP connections per second for TCP, HTTP, and HTTPS configurations.  Set to `0` (zero) to disable throttling.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When this NodeBalancer was created. (example: 2018-01-01T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ This NodeBalancer's hostname, beginning with its IP address and ending with _.ip.linodeusercontent.com_. (example: 192.0.2.1.ip.linodeusercontent.com)</td>
</tr>
<tr>
    <td><CopyableCode code="ipv4" /></td>
    <td><code>string (ip)</code></td>
    <td>__Filterable__, __Read-only__ This NodeBalancer's public IPv4 address. (example: 203.0.113.1)</td>
</tr>
<tr>
    <td><CopyableCode code="ipv6" /></td>
    <td><code>string (ip)</code></td>
    <td>__Read-only__ This NodeBalancer's public IPv6 address.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ This NodeBalancer's label. These must be unique on your Account. (example: balancer12345, pattern: <code>[a-zA-Z0-9-_]&#123;3,32&#125;</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="lke_cluster" /></td>
    <td><code>object</code></td>
    <td>__Read-only__ This NodeBalancer's related LKE cluster, if any. The value is `null` if this NodeBalancer isn't related to an LKE cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>__Filterable__, __Read-only__ The Region where this NodeBalancer is located. NodeBalancers only support backends in the same Region. (example: us-east)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>__Filterable__ An array of Tags applied to this object.  Tags are for organizational purposes only.</td>
</tr>
<tr>
    <td><CopyableCode code="transfer" /></td>
    <td><code>object</code></td>
    <td>__Read-only__ Information about the amount of transfer this NodeBalancer has had so far this month.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The type of NodeBalancer. (example: premium)</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When this NodeBalancer was last updated. (example: 2018-03-01T00:01:01)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_node_balancers">

A paginated list of NodeBalancers.

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
    <td><a href="#get_node_balancer"><CopyableCode code="get_node_balancer" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns a single NodeBalancer you can access.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_node_balancers"><CopyableCode code="get_node_balancers" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Returns a paginated list of NodeBalancers you have access to.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_node_balancer"><CopyableCode code="post_node_balancer" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__region"><code>data__region</code></a></td>
    <td></td>
    <td>Creates a NodeBalancer in the requested Region. Only available in [regions](https://techdocs.akamai.com/linode-api/reference/get-regions) with "NodeBalancers" in their `capabilities`.<br /><br />NodeBalancers require a port config with at least one backend node to start serving requests.<br /><br />When using the Linode CLI to create a NodeBalancer, first create a NodeBalancer without any configs. Then, create configs and nodes for that NodeBalancer with the respective [Create a config](https://techdocs.akamai.com/linode-api/reference/post-node-balancer-config) and [Create a node](https://techdocs.akamai.com/linode-api/reference/post-node-balancer-node) operations.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_node_balancer"><CopyableCode code="put_node_balancer" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Updates information about a NodeBalancer you can access.<br /><br />&gt; 🚧<br />&gt;<br />&gt; You can configure UDP on the same NodeBalancer that also uses TCP, HTTP, or HTTPS, but only when managing it through the API. If UDP is configured and you make changes to the TCP, HTTP or HTTPS settings in Cloud Manager, the existing UDP configuration will be overwritten. This is because Cloud Manager doesn't currently support UDP.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_node_balancer"><CopyableCode code="delete_node_balancer" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes a NodeBalancer.<br /><br />__This is a destructive action and cannot be undone.__<br /><br />Deleting a NodeBalancer will also delete all associated Configs and Nodes, although the backend servers represented by the Nodes will not be changed or removed. Deleting a NodeBalancer will cause you to lose access to the IP Addresses assigned to this NodeBalancer.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_node_balancer"
    values={[
        { label: 'get_node_balancer', value: 'get_node_balancer' },
        { label: 'get_node_balancers', value: 'get_node_balancers' }
    ]}
>
<TabItem value="get_node_balancer">

Returns a single NodeBalancer you can access.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
client_conn_throttle,
created,
hostname,
ipv4,
ipv6,
label,
lke_cluster,
region,
tags,
transfer,
type,
updated
FROM linode.nodebalancers.node_balancers
;
```
</TabItem>
<TabItem value="get_node_balancers">

Returns a paginated list of NodeBalancers you have access to.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.nodebalancers.node_balancers
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_node_balancer"
    values={[
        { label: 'post_node_balancer', value: 'post_node_balancer' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_node_balancer">

Creates a NodeBalancer in the requested Region. Only available in [regions](https://techdocs.akamai.com/linode-api/reference/get-regions) with "NodeBalancers" in their `capabilities`.<br /><br />NodeBalancers require a port config with at least one backend node to start serving requests.<br /><br />When using the Linode CLI to create a NodeBalancer, first create a NodeBalancer without any configs. Then, create configs and nodes for that NodeBalancer with the respective [Create a config](https://techdocs.akamai.com/linode-api/reference/post-node-balancer-config) and [Create a node](https://techdocs.akamai.com/linode-api/reference/post-node-balancer-node) operations.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.nodebalancers.node_balancers (
data__client_conn_throttle,
data__configs,
data__firewall_id,
data__label,
data__region,
data__tags,
data__vpcs
)
SELECT 
{{ client_conn_throttle }},
'{{ configs }}',
{{ firewall_id }},
'{{ label }}',
'{{ region }}' /* required */,
'{{ tags }}',
'{{ vpcs }}'
RETURNING
id,
client_conn_throttle,
created,
hostname,
ipv4,
ipv6,
label,
lke_cluster,
region,
tags,
transfer,
type,
updated
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: node_balancers
  props:
    - name: client_conn_throttle
      value: integer
      description: >
        Throttle TCP connections per second for TCP, HTTP, and HTTPS configurations.  Set to `0` (zero) to disable throttling.
        
    - name: configs
      value: array
      description: >
        The port configs to create for this NodeBalancer. Each config needs a unique port and at least one node.
        
    - name: firewall_id
      value: integer
      description: >
        The ID of the Firewall to assign to the NodeBalancer.

- A NodeBalancer can have only one Firewall assigned to it.
- Firewalls control inbound network traffic to NodeBalancers.
        
    - name: label
      value: string
      description: >
        __Filterable__ This NodeBalancer's label. These must be unique on your Account.
        
    - name: region
      value: string
      description: >
        The ID of the Region to create this NodeBalancer in.
        
    - name: tags
      value: array
      description: >
        An array of Tags applied to this object. Tags are for organizational purposes only.
        
    - name: vpcs
      value: array
      description: >
        You can have only one `vpcs` in a NodeBalancer configuration. If any of your backend nodes are VPC Linodes, specify the VPC subnet and CIDR range. NodeBalancer routes traffic to backend VPC nodes through this subnet. The specified VPC subnet must exist within the same data center as the NodeBalancer, and the provided IP range must be contained within the subnet's CIDR block. All IP addresses within the specified range must be free and available for assignment. Once the NodeBalancer is created, its VPC cannot be changed.
        
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_node_balancer"
    values={[
        { label: 'put_node_balancer', value: 'put_node_balancer' }
    ]}
>
<TabItem value="put_node_balancer">

Updates information about a NodeBalancer you can access.<br /><br />&gt; 🚧<br />&gt;<br />&gt; You can configure UDP on the same NodeBalancer that also uses TCP, HTTP, or HTTPS, but only when managing it through the API. If UDP is configured and you make changes to the TCP, HTTP or HTTPS settings in Cloud Manager, the existing UDP configuration will be overwritten. This is because Cloud Manager doesn't currently support UDP.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.nodebalancers.node_balancers
SET 
data__client_conn_throttle = {{ client_conn_throttle }},
data__label = '{{ label }}',
data__tags = '{{ tags }}'
RETURNING
id,
client_conn_throttle,
created,
hostname,
ipv4,
ipv6,
label,
lke_cluster,
region,
tags,
transfer,
type,
updated;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_node_balancer"
    values={[
        { label: 'delete_node_balancer', value: 'delete_node_balancer' }
    ]}
>
<TabItem value="delete_node_balancer">

Deletes a NodeBalancer.<br /><br />__This is a destructive action and cannot be undone.__<br /><br />Deleting a NodeBalancer will also delete all associated Configs and Nodes, although the backend servers represented by the Nodes will not be changed or removed. Deleting a NodeBalancer will cause you to lose access to the IP Addresses assigned to this NodeBalancer.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.nodebalancers.node_balancers
;
```
</TabItem>
</Tabs>
