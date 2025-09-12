--- 
title: nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - nodes
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

Creates, updates, deletes, gets or lists a <code>nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.nodebalancers.nodes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_node_balancer_node"
    values={[
        { label: 'get_node_balancer_node', value: 'get_node_balancer_node' },
        { label: 'get_node_balancer_config_nodes', value: 'get_node_balancer_config_nodes' }
    ]}
>
<TabItem value="get_node_balancer_node">

A paginated list of NodeBalancer nodes.

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
</TabItem>
<TabItem value="get_node_balancer_config_nodes">

A paginated list of NodeBalancer nodes.

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
    <td><a href="#get_node_balancer_node"><CopyableCode code="get_node_balancer_node" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns information about a single Node, a backend for this NodeBalancer's configured port.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_node_balancer_config_nodes"><CopyableCode code="get_node_balancer_config_nodes" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Returns a paginated list of NodeBalancer nodes associated with this Config. These are the backends that will be sent traffic for this port.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_node_balancer_node"><CopyableCode code="post_node_balancer_node" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__label"><code>data__label</code></a>, <a href="#parameter-data__address"><code>data__address</code></a></td>
    <td></td>
    <td>Creates a backend node that can receive traffic for the NodeBalancer configuration. Requests are routed to backend nodes on the specified port based on their `status`. The configurable fields for the backend node depend on the chosen protocol and whether the node is located within a Linode VPC.<br /><br />&gt; 🚧<br />&gt;<br />&gt; You can configure UDP on the same NodeBalancer that also uses TCP, HTTP, or HTTPS, but only when managing it through the API. If UDP is configured and you make changes to the TCP, HTTP or HTTPS settings in Cloud Manager, the existing UDP configuration will be overwritten. This is because Cloud Manager doesn't currently support UDP. __CLI: TCP, HTTP, HTTPS__.<br /><br />    ```<br />    linode-cli nodebalancers node-create \<br />  12345 4567 \<br />  --address 10.0.0.45:80 \<br />  --label node54321 \<br />  --weight 50 \<br />  --mode accept \<br />  --subnet_id 1<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: UDP__.<br /><br />    ```<br />    linode-cli nodebalancers node-create \<br />  12345 4567 \<br />  --address 192.168.210.120:80 \<br />  --label node54321 \<br />  --weight 50<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_node_balancer_node"><CopyableCode code="put_node_balancer_node" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Updates information about a node, a backend for this NodeBalancer's configured port.<br /><br />&gt; 🚧<br />&gt;<br />&gt; You can configure UDP on the same NodeBalancer that also uses TCP, HTTP, or HTTPS, but only when managing it through the API. If UDP is configured and you make changes to the TCP, HTTP or HTTPS settings in Cloud Manager, the existing UDP configuration will be overwritten. This is because Cloud Manager doesn't currently support UDP. __CLI: TCP, HTTP, HTTPS__.<br /><br />    ```<br />    linode-cli nodebalancers node-update \<br />  12345 4567 54321 \<br />  --address 192.168.210.120:80 \<br />  --label node54321 \<br />  --weight 50 \<br />  --mode accept<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: UDP__.<br /><br />    ```<br />    linode-cli nodebalancers node-create \<br />  12345 4567 \<br />  --address 192.168.210.120:80 \<br />  --label node54321 \<br />  --weight 50<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_node_balancer_config_node"><CopyableCode code="delete_node_balancer_config_node" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes a Node from this Config. This backend will no longer receive traffic for the configured port of this NodeBalancer.<br /><br />This does not change or remove the Linode whose address was used in the creation of this Node.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_node_balancer_node"
    values={[
        { label: 'get_node_balancer_node', value: 'get_node_balancer_node' },
        { label: 'get_node_balancer_config_nodes', value: 'get_node_balancer_config_nodes' }
    ]}
>
<TabItem value="get_node_balancer_node">

Returns information about a single Node, a backend for this NodeBalancer's configured port.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
*
FROM linode.nodebalancers.nodes
;
```
</TabItem>
<TabItem value="get_node_balancer_config_nodes">

Returns a paginated list of NodeBalancer nodes associated with this Config. These are the backends that will be sent traffic for this port.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.nodebalancers.nodes
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_node_balancer_node"
    values={[
        { label: 'post_node_balancer_node', value: 'post_node_balancer_node' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_node_balancer_node">

Creates a backend node that can receive traffic for the NodeBalancer configuration. Requests are routed to backend nodes on the specified port based on their `status`. The configurable fields for the backend node depend on the chosen protocol and whether the node is located within a Linode VPC.<br /><br />&gt; 🚧<br />&gt;<br />&gt; You can configure UDP on the same NodeBalancer that also uses TCP, HTTP, or HTTPS, but only when managing it through the API. If UDP is configured and you make changes to the TCP, HTTP or HTTPS settings in Cloud Manager, the existing UDP configuration will be overwritten. This is because Cloud Manager doesn't currently support UDP. __CLI: TCP, HTTP, HTTPS__.<br /><br />    ```<br />    linode-cli nodebalancers node-create \<br />  12345 4567 \<br />  --address 10.0.0.45:80 \<br />  --label node54321 \<br />  --weight 50 \<br />  --mode accept \<br />  --subnet_id 1<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: UDP__.<br /><br />    ```<br />    linode-cli nodebalancers node-create \<br />  12345 4567 \<br />  --address 192.168.210.120:80 \<br />  --label node54321 \<br />  --weight 50<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.nodebalancers.nodes (

)
SELECT 

;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: nodes
  props:
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_node_balancer_node"
    values={[
        { label: 'put_node_balancer_node', value: 'put_node_balancer_node' }
    ]}
>
<TabItem value="put_node_balancer_node">

Updates information about a node, a backend for this NodeBalancer's configured port.<br /><br />&gt; 🚧<br />&gt;<br />&gt; You can configure UDP on the same NodeBalancer that also uses TCP, HTTP, or HTTPS, but only when managing it through the API. If UDP is configured and you make changes to the TCP, HTTP or HTTPS settings in Cloud Manager, the existing UDP configuration will be overwritten. This is because Cloud Manager doesn't currently support UDP. __CLI: TCP, HTTP, HTTPS__.<br /><br />    ```<br />    linode-cli nodebalancers node-update \<br />  12345 4567 54321 \<br />  --address 192.168.210.120:80 \<br />  --label node54321 \<br />  --weight 50 \<br />  --mode accept<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: UDP__.<br /><br />    ```<br />    linode-cli nodebalancers node-create \<br />  12345 4567 \<br />  --address 192.168.210.120:80 \<br />  --label node54321 \<br />  --weight 50<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.nodebalancers.nodes
SET 
-- No updatable properties;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_node_balancer_config_node"
    values={[
        { label: 'delete_node_balancer_config_node', value: 'delete_node_balancer_config_node' }
    ]}
>
<TabItem value="delete_node_balancer_config_node">

Deletes a Node from this Config. This backend will no longer receive traffic for the configured port of this NodeBalancer.<br /><br />This does not change or remove the Linode whose address was used in the creation of this Node.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.nodebalancers.nodes
;
```
</TabItem>
</Tabs>
