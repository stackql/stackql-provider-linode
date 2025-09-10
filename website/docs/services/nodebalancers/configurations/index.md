--- 
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
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

Creates, updates, deletes, gets or lists a <code>configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.nodebalancers.configurations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_node_balancer_config"
    values={[
        { label: 'get_node_balancer_config', value: 'get_node_balancer_config' },
        { label: 'get_node_balancer_configs', value: 'get_node_balancer_configs' }
    ]}
>
<TabItem value="get_node_balancer_config">

The requested NodeBalancer config.

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
<TabItem value="get_node_balancer_configs">

A paginated list of NodeBalancer Configs.

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
    <td><a href="#get_node_balancer_config"><CopyableCode code="get_node_balancer_config" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns configuration information for a single port of this NodeBalancer.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_node_balancer_configs"><CopyableCode code="get_node_balancer_configs" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Returns a paginated list of NodeBalancer Configs associated with this NodeBalancer. NodeBalancer Configs represent individual ports that this NodeBalancer will accept traffic on, one Config per port.<br /><br />For example, if you wanted to accept standard HTTP traffic, you would need a Config listening on port 80.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_node_balancer_config"><CopyableCode code="post_node_balancer_config" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__nodes"><code>data__nodes</code></a></td>
    <td></td>
    <td>Creates a NodeBalancer configuration, which allows the NodeBalancer to accept traffic on a new port. You will need to add NodeBalancer nodes to the new configuration before it can actually serve requests.<br /><br />&gt; 🚧<br />&gt;<br />&gt; You can configure UDP on the same NodeBalancer that also uses TCP, HTTP, or HTTPS, but only when managing it through the API. If UDP is configured and you make changes to the TCP, HTTP or HTTPS settings in Cloud Manager, the existing UDP configuration will be overwritten. This is because Cloud Manager doesn't currently support UDP. __CLI: HTTPS__.<br /><br />    ```<br />    linode-cli nodebalancers config-create 12345 \<br />  --port 443 \<br />  --protocol https \<br />  --algorithm roundrobin \<br />  --stickiness http_cookie \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works" \<br />  --check_passive true \<br />  --proxy_protocol "none" \<br />  --ssl_cert "-----BEGIN CERTIFICATE-----<br />              CERTIFICATE_INFORMATION<br />              -----END CERTIFICATE-----" \<br />  --ssl_key "-----BEGIN PRIVATE KEY-----<br />             PRIVATE_KEY_INFORMATION<br />             -----END PRIVATE KEY-----" \<br />  --cipher_suite recommended<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: UDP__.<br /><br />    ```<br />    linode-cli nodebalancers config-create 12345 \<br />  --port 80 \<br />  --protocol udp \<br />  --algorithm ring_hash \<br />  --stickiness session \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works" \<br />  --udp_check_port 80<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: TCP__.<br /><br />    ```<br />    linode-cli nodebalancers config-create 12345 \<br />  --port 80 \<br />  --protocol tcp \<br />  --algorithm roundrobin \<br />  --stickiness none \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works" \<br />  --proxy_protocol "v2"<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: HTTP__.<br /><br />    ```<br />    linode-cli nodebalancers config-create 12345 \<br />  --port 440 \<br />  --protocol http \<br />  --algorithm roundrobin \<br />  --stickiness http_cookie \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works"<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_node_balancer_config"><CopyableCode code="put_node_balancer_config" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Updates the configuration for a single port on a NodeBalancer.<br /><br />&gt; 🚧<br />&gt;<br />&gt; You can configure UDP on the same NodeBalancer that also uses TCP, HTTP, or HTTPS, but only when managing it through the API. If UDP is configured and you make changes to the TCP, HTTP or HTTPS settings in Cloud Manager, the existing UDP configuration will be overwritten. This is because Cloud Manager doesn't currently support UDP. __CLI: HTTPS__.<br /><br />    ```<br />    linode-cli nodebalancers config-update \<br />  12345 4567 \<br />  --port 443 \<br />  --protocol https \<br />  --algorithm roundrobin \<br />  --stickiness http_cookie \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works" \<br />  --check_passive true \<br />  --proxy_protocol "none" \<br />  --ssl_cert "-----BEGIN CERTIFICATE-----<br />              CERTIFICATE_INFORMATION<br />              -----END CERTIFICATE-----" \<br />  --ssl_key "-----BEGIN PRIVATE KEY-----<br />             PRIVATE_KEY_INFORMATION<br />             -----END PRIVATE KEY-----" \<br />  --cipher_suite recommended<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: UDP__.<br /><br />    ```<br />    linode-cli nodebalancers config-update \<br />  12345 4567 \<br />  --port 80 \<br />  --protocol udp \<br />  --algorithm ring_hash \<br />  --stickiness session \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works" \<br />  --udp_check_port 80<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: TCP__.<br /><br />    ```<br />    linode-cli nodebalancers config-update \<br />  12345 4567 \<br />  --port 80 \<br />  --protocol tcp \<br />  --algorithm roundrobin \<br />  --stickiness none \<br />  --stickiness http_cookie \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works" \<br />  --proxy_protocol "v2"<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: HTTP__.<br /><br />    ```<br />    linode-cli nodebalancers config-update \<br />  12345 4567 \<br />  --port 440 \<br />  --protocol http \<br />  --algorithm roundrobin \<br />  --stickiness http_cookie \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works"<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_node_balancer_config"><CopyableCode code="delete_node_balancer_config" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes the Config for a port of this NodeBalancer.<br /><br />__This cannot be undone.__<br /><br />Once completed, this NodeBalancer will no longer respond to requests on the given port. This also deletes all associated NodeBalancerNodes, but the Linodes they were routing traffic to will be unchanged and will not be removed.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_rebuild_node_balancer_config"><CopyableCode code="post_rebuild_node_balancer_config" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-nodes"><code>nodes</code></a></td>
    <td></td>
    <td>Rebuilds a NodeBalancer config and its nodes that you have permission to modify.<br /><br />Use this operation to update a NodeBalancer's config and nodes with a single request.<br /><br />&gt; 🚧<br />&gt;<br />&gt; You can configure UDP on the same NodeBalancer that also uses TCP, HTTP, or HTTPS, but only when managing it through the API. If UDP is configured and you make changes to the TCP, HTTP or HTTPS settings in Cloud Manager, the existing UDP configuration will be overwritten. This is because Cloud Manager doesn't currently support UDP. __CLI: HTTPS__.<br /><br />    ```<br />    linode-cli nodebalancers config-rebuild \<br />  12345 4567 \<br />  --port 443 \<br />  --protocol https \<br />  --algorithm roundrobin \<br />  --stickiness http_cookie \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works" \<br />  --check_passive true \<br />  --proxy_protocol "none" \<br />  --ssl_cert "-----BEGIN CERTIFICATE-----<br />              CERTIFICATE_INFORMATION<br />              -----END CERTIFICATE-----" \<br />  --ssl_key "-----BEGIN PRIVATE KEY-----<br />             PRIVATE_KEY_INFORMATION<br />             -----END PRIVATE KEY-----" \<br />  --cipher_suite recommended \<br />  --nodes.label "node1" --nodes.address "192.168.210.120:80" --nodes.mode "accept" --nodes.weight 50 \<br />  --nodes '[&#123;"address":"192.168.210.122:80","label":"node2","weight":50,"mode":"accept"&#125;]' \<br />  --nodes '[&#123;"address":"10.0.0.45:80","label":"vpc-node","weight":10,"mode":"accept","subnet_id:1"&#125;]'<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: UDP__.<br /><br />    ```<br />    linode-cli nodebalancers config-rebuild \<br />   12345 4567 \<br />   --port 80 \<br />   --protocol udp \<br />   --algorithm ring_hash \<br />   --udp_check_port 80 \<br />   --nodes.label "node1" --nodes.address "192.168.210.120:80" --nodes.mode "accept" --nodes.weight 50 \<br />   --nodes '[&#123;"address":"192.168.210.122:80","label":"node2","weight":50&#125;]' \<br />   --nodes '[&#123;"address":"10.0.0.45:80","label":"vpc-node","weight":10,"mode":"accept","subnet_id:1"&#125;]'<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: TCP__.<br /><br />    ```<br />    linode-cli nodebalancers config-rebuild \<br />  12345 4567 \<br />  --port 80 \<br />  --protocol tcp \<br />  --algorithm roundrobin \<br />  --stickiness none \<br />  --proxy_protocol "v2"<br />  --nodes.label "node1" --nodes.address "192.168.210.120:80" --nodes.mode "accept" --nodes.weight 50 \<br />  --nodes '[&#123;"address":"192.168.210.122:80","label":"node2","weight":50,"mode":"accept"&#125;]' \<br />  --nodes '[&#123;"address":"10.0.0.45:80","label":"vpc-node","weight":10,"mode":"accept","subnet_id:1"&#125;]'<br />    ```<br /><br />[Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)<br /><br />- __CLI: HTTP__.<br /><br />    ```<br />    linode-cli nodebalancers config-rebuild \<br />  12345 4567 \<br />  --port 440 \<br />  --protocol http \<br />  --algorithm roundrobin \<br />  --stickiness none \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works" \<br />  --nodes.label "node1" --nodes.address "192.168.210.120:80" --nodes.mode "accept" --nodes.weight 50 \<br />  --nodes '[&#123;"address":"192.168.210.122:80","label":"node2","weight":50,"mode":"accept"&#125;]' \<br />  --nodes '[&#123;"address":"10.0.0.45:80","label":"vpc-node","weight":10,"mode":"accept","subnet_id:1"&#125;]'<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_node_balancer_config"
    values={[
        { label: 'get_node_balancer_config', value: 'get_node_balancer_config' },
        { label: 'get_node_balancer_configs', value: 'get_node_balancer_configs' }
    ]}
>
<TabItem value="get_node_balancer_config">

Returns configuration information for a single port of this NodeBalancer.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
*
FROM linode.nodebalancers.configurations;
```
</TabItem>
<TabItem value="get_node_balancer_configs">

Returns a paginated list of NodeBalancer Configs associated with this NodeBalancer. NodeBalancer Configs represent individual ports that this NodeBalancer will accept traffic on, one Config per port.<br /><br />For example, if you wanted to accept standard HTTP traffic, you would need a Config listening on port 80.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
*
FROM linode.nodebalancers.configurations
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}';
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_node_balancer_config"
    values={[
        { label: 'post_node_balancer_config', value: 'post_node_balancer_config' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_node_balancer_config">

Creates a NodeBalancer configuration, which allows the NodeBalancer to accept traffic on a new port. You will need to add NodeBalancer nodes to the new configuration before it can actually serve requests.<br /><br />&gt; 🚧<br />&gt;<br />&gt; You can configure UDP on the same NodeBalancer that also uses TCP, HTTP, or HTTPS, but only when managing it through the API. If UDP is configured and you make changes to the TCP, HTTP or HTTPS settings in Cloud Manager, the existing UDP configuration will be overwritten. This is because Cloud Manager doesn't currently support UDP. __CLI: HTTPS__.<br /><br />    ```<br />    linode-cli nodebalancers config-create 12345 \<br />  --port 443 \<br />  --protocol https \<br />  --algorithm roundrobin \<br />  --stickiness http_cookie \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works" \<br />  --check_passive true \<br />  --proxy_protocol "none" \<br />  --ssl_cert "-----BEGIN CERTIFICATE-----<br />              CERTIFICATE_INFORMATION<br />              -----END CERTIFICATE-----" \<br />  --ssl_key "-----BEGIN PRIVATE KEY-----<br />             PRIVATE_KEY_INFORMATION<br />             -----END PRIVATE KEY-----" \<br />  --cipher_suite recommended<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: UDP__.<br /><br />    ```<br />    linode-cli nodebalancers config-create 12345 \<br />  --port 80 \<br />  --protocol udp \<br />  --algorithm ring_hash \<br />  --stickiness session \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works" \<br />  --udp_check_port 80<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: TCP__.<br /><br />    ```<br />    linode-cli nodebalancers config-create 12345 \<br />  --port 80 \<br />  --protocol tcp \<br />  --algorithm roundrobin \<br />  --stickiness none \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works" \<br />  --proxy_protocol "v2"<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: HTTP__.<br /><br />    ```<br />    linode-cli nodebalancers config-create 12345 \<br />  --port 440 \<br />  --protocol http \<br />  --algorithm roundrobin \<br />  --stickiness http_cookie \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works"<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.nodebalancers.configurations (
data__nodes
)
SELECT 
'{{ nodes }}' --required
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: configurations
  props:
    - name: nodes
      value: array
      description: >
        The NodeBalancer nodes that serve this config.

Some considerations for Nodes when rebuilding a config:

  - Current Nodes excluded from the request body will be deleted from the Config.
  - Current Nodes (identified by their Node ID) will be updated.
  - New Nodes (included without a Node ID) will be created.
        
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_node_balancer_config"
    values={[
        { label: 'put_node_balancer_config', value: 'put_node_balancer_config' }
    ]}
>
<TabItem value="put_node_balancer_config">

Updates the configuration for a single port on a NodeBalancer.<br /><br />&gt; 🚧<br />&gt;<br />&gt; You can configure UDP on the same NodeBalancer that also uses TCP, HTTP, or HTTPS, but only when managing it through the API. If UDP is configured and you make changes to the TCP, HTTP or HTTPS settings in Cloud Manager, the existing UDP configuration will be overwritten. This is because Cloud Manager doesn't currently support UDP. __CLI: HTTPS__.<br /><br />    ```<br />    linode-cli nodebalancers config-update \<br />  12345 4567 \<br />  --port 443 \<br />  --protocol https \<br />  --algorithm roundrobin \<br />  --stickiness http_cookie \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works" \<br />  --check_passive true \<br />  --proxy_protocol "none" \<br />  --ssl_cert "-----BEGIN CERTIFICATE-----<br />              CERTIFICATE_INFORMATION<br />              -----END CERTIFICATE-----" \<br />  --ssl_key "-----BEGIN PRIVATE KEY-----<br />             PRIVATE_KEY_INFORMATION<br />             -----END PRIVATE KEY-----" \<br />  --cipher_suite recommended<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: UDP__.<br /><br />    ```<br />    linode-cli nodebalancers config-update \<br />  12345 4567 \<br />  --port 80 \<br />  --protocol udp \<br />  --algorithm ring_hash \<br />  --stickiness session \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works" \<br />  --udp_check_port 80<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: TCP__.<br /><br />    ```<br />    linode-cli nodebalancers config-update \<br />  12345 4567 \<br />  --port 80 \<br />  --protocol tcp \<br />  --algorithm roundrobin \<br />  --stickiness none \<br />  --stickiness http_cookie \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works" \<br />  --proxy_protocol "v2"<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: HTTP__.<br /><br />    ```<br />    linode-cli nodebalancers config-update \<br />  12345 4567 \<br />  --port 440 \<br />  --protocol http \<br />  --algorithm roundrobin \<br />  --stickiness http_cookie \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works"<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.nodebalancers.configurations
SET 
-- No updatable properties
WHERE 
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_node_balancer_config"
    values={[
        { label: 'delete_node_balancer_config', value: 'delete_node_balancer_config' }
    ]}
>
<TabItem value="delete_node_balancer_config">

Deletes the Config for a port of this NodeBalancer.<br /><br />__This cannot be undone.__<br /><br />Once completed, this NodeBalancer will no longer respond to requests on the given port. This also deletes all associated NodeBalancerNodes, but the Linodes they were routing traffic to will be unchanged and will not be removed.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.nodebalancers.configurations;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="post_rebuild_node_balancer_config"
    values={[
        { label: 'post_rebuild_node_balancer_config', value: 'post_rebuild_node_balancer_config' }
    ]}
>
<TabItem value="post_rebuild_node_balancer_config">

Rebuilds a NodeBalancer config and its nodes that you have permission to modify.<br /><br />Use this operation to update a NodeBalancer's config and nodes with a single request.<br /><br />&gt; 🚧<br />&gt;<br />&gt; You can configure UDP on the same NodeBalancer that also uses TCP, HTTP, or HTTPS, but only when managing it through the API. If UDP is configured and you make changes to the TCP, HTTP or HTTPS settings in Cloud Manager, the existing UDP configuration will be overwritten. This is because Cloud Manager doesn't currently support UDP. __CLI: HTTPS__.<br /><br />    ```<br />    linode-cli nodebalancers config-rebuild \<br />  12345 4567 \<br />  --port 443 \<br />  --protocol https \<br />  --algorithm roundrobin \<br />  --stickiness http_cookie \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works" \<br />  --check_passive true \<br />  --proxy_protocol "none" \<br />  --ssl_cert "-----BEGIN CERTIFICATE-----<br />              CERTIFICATE_INFORMATION<br />              -----END CERTIFICATE-----" \<br />  --ssl_key "-----BEGIN PRIVATE KEY-----<br />             PRIVATE_KEY_INFORMATION<br />             -----END PRIVATE KEY-----" \<br />  --cipher_suite recommended \<br />  --nodes.label "node1" --nodes.address "192.168.210.120:80" --nodes.mode "accept" --nodes.weight 50 \<br />  --nodes '[&#123;"address":"192.168.210.122:80","label":"node2","weight":50,"mode":"accept"&#125;]' \<br />  --nodes '[&#123;"address":"10.0.0.45:80","label":"vpc-node","weight":10,"mode":"accept","subnet_id:1"&#125;]'<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: UDP__.<br /><br />    ```<br />    linode-cli nodebalancers config-rebuild \<br />   12345 4567 \<br />   --port 80 \<br />   --protocol udp \<br />   --algorithm ring_hash \<br />   --udp_check_port 80 \<br />   --nodes.label "node1" --nodes.address "192.168.210.120:80" --nodes.mode "accept" --nodes.weight 50 \<br />   --nodes '[&#123;"address":"192.168.210.122:80","label":"node2","weight":50&#125;]' \<br />   --nodes '[&#123;"address":"10.0.0.45:80","label":"vpc-node","weight":10,"mode":"accept","subnet_id:1"&#125;]'<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />- __CLI: TCP__.<br /><br />    ```<br />    linode-cli nodebalancers config-rebuild \<br />  12345 4567 \<br />  --port 80 \<br />  --protocol tcp \<br />  --algorithm roundrobin \<br />  --stickiness none \<br />  --proxy_protocol "v2"<br />  --nodes.label "node1" --nodes.address "192.168.210.120:80" --nodes.mode "accept" --nodes.weight 50 \<br />  --nodes '[&#123;"address":"192.168.210.122:80","label":"node2","weight":50,"mode":"accept"&#125;]' \<br />  --nodes '[&#123;"address":"10.0.0.45:80","label":"vpc-node","weight":10,"mode":"accept","subnet_id:1"&#125;]'<br />    ```<br /><br />[Learn more...](https://www.linode.com/docs/products/tools/cli/get-started/)<br /><br />- __CLI: HTTP__.<br /><br />    ```<br />    linode-cli nodebalancers config-rebuild \<br />  12345 4567 \<br />  --port 440 \<br />  --protocol http \<br />  --algorithm roundrobin \<br />  --stickiness none \<br />  --check http_body \<br />  --check_interval 90 \<br />  --check_timeout 10 \<br />  --check_attempts 3 \<br />  --check_path "/test" \<br />  --check_body "it works" \<br />  --nodes.label "node1" --nodes.address "192.168.210.120:80" --nodes.mode "accept" --nodes.weight 50 \<br />  --nodes '[&#123;"address":"192.168.210.122:80","label":"node2","weight":50,"mode":"accept"&#125;]' \<br />  --nodes '[&#123;"address":"10.0.0.45:80","label":"vpc-node","weight":10,"mode":"accept","subnet_id:1"&#125;]'<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.nodebalancers.configurations.post_rebuild_node_balancer_config 
@@json=
'{
"nodes": "{{ nodes }}"
}';
```
</TabItem>
</Tabs>
