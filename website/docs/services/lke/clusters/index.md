--- 
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - lke
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

Creates, updates, deletes, gets or lists a <code>clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.lke.clusters" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_lke_cluster"
    values={[
        { label: 'get_lke_cluster', value: 'get_lke_cluster' },
        { label: 'get_lke_clusters', value: 'get_lke_clusters' }
    ]}
>
<TabItem value="get_lke_cluster">

Returns a single Kubernetes cluster.

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
    <td>__Read-only__ This Kubernetes cluster's unique ID.</td>
</tr>
<tr>
    <td><CopyableCode code="apl_enabled" /></td>
    <td><code>boolean</code></td>
    <td>__Write-once__ Indicates whether the Akamai App Platform is installed during creation of the LKE cluster. It defaults to `false`. If set to `true`, `control_plane.high_availability` also needs to be `true`. Automatic installation of the App Platform is only possible when creating a new cluster (not when modifying existing clusters).</td>
</tr>
<tr>
    <td><CopyableCode code="control_plane" /></td>
    <td><code>object</code></td>
    <td>Defines settings for the Kubernetes control plane, including enabling High Availability (HA) for the control plane.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When this Kubernetes cluster was created. (example: 2019-09-12T21:25:30Z)</td>
</tr>
<tr>
    <td><CopyableCode code="k8s_version" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The desired Kubernetes version for this Kubernetes cluster in the format of `<major>.<minor>`. The latest supported patch version is deployed. (example: 1.32)</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ This Kubernetes cluster's unique label for display purposes only. Labels have the following constraints:    - UTF-8 characters will be returned by the API using escape sequences of their Unicode code points. For example, the Japanese character _か_ is 3 bytes in UTF-8 (`0xE382AB`). Its Unicode code point is 2 bytes (`0x30AB`). APIv4 supports this character and the API will return it as the escape sequence using six 1 byte characters which represent 2 bytes of Unicode code point (`"\u30ab"`).    - 4 byte UTF-8 characters are not supported.    - If the label is entirely composed of UTF-8 characters, the API response will return the code points using up to 193 1 byte characters. (example: lkecluster12345)</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ This Kubernetes cluster's location. (example: us-central)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>__Filterable__ An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.</td>
</tr>
<tr>
    <td><CopyableCode code="tier" /></td>
    <td><code>string</code></td>
    <td>__Beta__, __Filterable__ The desired Kubernetes tier, either `standard` or `enterprise`.  &gt; 🚧 &gt; &gt; This field is in beta and only works when using the beta API. Call the URL with the `apiVersion` path parameter set to `v4beta`. (example: standard)</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When this Kubernetes cluster was updated. (example: 2019-09-13T21:24:16Z)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_lke_clusters">

Returns an array of all Kubernetes clusters on your Account.

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
    <td><a href="#get_lke_cluster"><CopyableCode code="get_lke_cluster" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a specific Cluster by ID.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_lke_clusters"><CopyableCode code="get_lke_clusters" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Lists current Kubernetes clusters available on your account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_lke_cluster"><CopyableCode code="post_lke_cluster" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__label"><code>data__label</code></a>, <a href="#parameter-data__region"><code>data__region</code></a>, <a href="#parameter-data__k8s_version"><code>data__k8s_version</code></a>, <a href="#parameter-data__node_pools"><code>data__node_pools</code></a></td>
    <td></td>
    <td>Creates a Kubernetes cluster. The Kubernetes cluster will be created asynchronously. You can use the events system to determine when the Kubernetes cluster is ready to use. Please note that it often takes 2-5 minutes before the [Kubernetes API endpoints](https://techdocs.akamai.com/linode-api/reference/get-lke-cluster-api-endpoints) and the [Kubeconfig file](https://techdocs.akamai.com/linode-api/reference/get-lke-cluster-kubeconfig) for the new cluster are ready.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_lke_cluster"><CopyableCode code="put_lke_cluster" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Updates a Kubernetes cluster.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_lke_cluster"><CopyableCode code="delete_lke_cluster" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes a Cluster you have permission to `read_write`.<br /><br />__Deleting a Cluster is a destructive action and cannot be undone.__<br /><br />Deleting a Cluster:<br /><br />- Deletes all Linodes in all pools within this Kubernetes cluster<br />- Deletes all supporting Kubernetes services for this Kubernetes cluster (API server, etcd, etc)<br />- Deletes all NodeBalancers created by this Kubernetes cluster<br />- Does not delete any of the volumes created by this Kubernetes cluster<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_lke_cluster_recycle"><CopyableCode code="post_lke_cluster_recycle" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Recycles all nodes in all pools of a designated Kubernetes Cluster. All Linodes within the Cluster will be deleted and replaced with new Linodes on a rolling basis, which may take several minutes. Replacement Nodes are installed with the latest available patch version for the Cluster's current Kubernetes minor release.<br /><br />__Any local storage on deleted Linodes (such as `hostPath` and `emptyDir` volumes, or `local` PersistentVolumes) will be erased.__<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_lke_cluster_regenerate"><CopyableCode code="post_lke_cluster_regenerate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Regenerate the Kubeconfig file and/or the service account token for a Cluster.<br /><br />This is a helper operation that allows performing both the [Delete a Kubeconfig](https://techdocs.akamai.com/linode-api/reference/delete-lke-cluster-kubeconfig) and the [Delete a service token](https://techdocs.akamai.com/linode-api/reference/delete-lke-service-token) operations with a single request.<br /><br />When using this operation, at least one of `kubeconfig` or `servicetoken` is required.<br /><br />&gt; 📘<br />&gt;<br />&gt; When regenerating a service account token, the cluster's control plane components and Linode CSI drivers are also restarted and configured with the new token. High availability clusters shouldn't experience any disruption, while standard clusters may experience brief control plane downtime while components are restarted.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_lke_service_token"><CopyableCode code="delete_lke_service_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Delete and regenerate the service account token for a Cluster.<br /><br />&gt; 📘<br />&gt;<br />&gt; When you regenerate a service account token, the cluster's control plane components and Linode CSI drivers are also restarted and configured with the new token. High availability clusters shouldn't experience any disruption, while standard clusters may experience brief control plane downtime while components are restarted.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_lke_cluster"
    values={[
        { label: 'get_lke_cluster', value: 'get_lke_cluster' },
        { label: 'get_lke_clusters', value: 'get_lke_clusters' }
    ]}
>
<TabItem value="get_lke_cluster">

Get a specific Cluster by ID.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
apl_enabled,
control_plane,
created,
k8s_version,
label,
region,
tags,
tier,
updated
FROM linode.lke.clusters
;
```
</TabItem>
<TabItem value="get_lke_clusters">

Lists current Kubernetes clusters available on your account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.lke.clusters
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_lke_cluster"
    values={[
        { label: 'post_lke_cluster', value: 'post_lke_cluster' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_lke_cluster">

Creates a Kubernetes cluster. The Kubernetes cluster will be created asynchronously. You can use the events system to determine when the Kubernetes cluster is ready to use. Please note that it often takes 2-5 minutes before the [Kubernetes API endpoints](https://techdocs.akamai.com/linode-api/reference/get-lke-cluster-api-endpoints) and the [Kubeconfig file](https://techdocs.akamai.com/linode-api/reference/get-lke-cluster-kubeconfig) for the new cluster are ready.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.lke.clusters (
data__apl_enabled,
data__control_plane,
data__k8s_version,
data__label,
data__node_pools,
data__region,
data__tags,
data__tier
)
SELECT 
{{ apl_enabled }},
'{{ control_plane }}',
'{{ k8s_version }}' /* required */,
'{{ label }}' /* required */,
'{{ node_pools }}' /* required */,
'{{ region }}' /* required */,
'{{ tags }}',
'{{ tier }}'
RETURNING
id,
apl_enabled,
control_plane,
created,
k8s_version,
label,
region,
tags,
tier,
updated
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: clusters
  props:
    - name: apl_enabled
      value: boolean
      description: >
        __Write-once__ Indicates whether the Akamai App Platform is installed during creation of the LKE cluster. It defaults to `false`. If set to `true`, `control_plane.high_availability` also needs to be `true`. Automatic installation of the App Platform is only possible when creating a new cluster (not when modifying existing clusters).
        
    - name: control_plane
      value: object
      description: >
        Defines settings for the Kubernetes control plane, including High Availability (HA) and an IP-based Access Control List (ACL) for the control plane components.
        
    - name: k8s_version
      value: string
      description: >
        __Filterable__ The desired Kubernetes version for this Kubernetes cluster in the format of `<major>.<minor>`. The latest supported patch version is deployed.
        
    - name: label
      value: string
      description: >
        __Filterable__ This Kubernetes cluster's unique label for display purposes only. Labels have the following constraints:

  - UTF-8 characters will be returned by the API using escape sequences of their Unicode code points. For example, the Japanese character _か_ is 3 bytes in UTF-8 (`0xE382AB`). Its Unicode code point is 2 bytes (`0x30AB`). APIv4 supports this character and the API will return it as the escape sequence using six 1 byte characters which represent 2 bytes of Unicode code point (`"\u30ab"`).

  - 4 byte UTF-8 characters are not supported.

  - If the label is entirely composed of UTF-8 characters, the API response will return the code points using up to 193 1 byte characters.
        
    - name: node_pools
      value: array
    - name: region
      value: string
      description: >
        __Filterable__ This Kubernetes cluster's location.
        
    - name: tags
      value: array
      description: >
        __Filterable__ An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.
        
    - name: tier
      value: string
      description: >
        __Beta__, __Filterable__ The desired Kubernetes tier, either `standard` or `enterprise`.

> 🚧
>
> This field is in beta and only works when using the beta API. Call the URL with the `apiVersion` path parameter set to `v4beta`.
        
      valid_values: ['standard', 'enterprise']
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_lke_cluster"
    values={[
        { label: 'put_lke_cluster', value: 'put_lke_cluster' }
    ]}
>
<TabItem value="put_lke_cluster">

Updates a Kubernetes cluster.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.lke.clusters
SET 
data__control_plane = '{{ control_plane }}',
data__k8s_version = '{{ k8s_version }}',
data__label = '{{ label }}',
data__tags = '{{ tags }}'
RETURNING
created,
k8s_version,
label,
region,
tags,
updated;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_lke_cluster"
    values={[
        { label: 'delete_lke_cluster', value: 'delete_lke_cluster' }
    ]}
>
<TabItem value="delete_lke_cluster">

Deletes a Cluster you have permission to `read_write`.<br /><br />__Deleting a Cluster is a destructive action and cannot be undone.__<br /><br />Deleting a Cluster:<br /><br />- Deletes all Linodes in all pools within this Kubernetes cluster<br />- Deletes all supporting Kubernetes services for this Kubernetes cluster (API server, etcd, etc)<br />- Deletes all NodeBalancers created by this Kubernetes cluster<br />- Does not delete any of the volumes created by this Kubernetes cluster<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.lke.clusters
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="post_lke_cluster_recycle"
    values={[
        { label: 'post_lke_cluster_recycle', value: 'post_lke_cluster_recycle' },
        { label: 'post_lke_cluster_regenerate', value: 'post_lke_cluster_regenerate' },
        { label: 'delete_lke_service_token', value: 'delete_lke_service_token' }
    ]}
>
<TabItem value="post_lke_cluster_recycle">

Recycles all nodes in all pools of a designated Kubernetes Cluster. All Linodes within the Cluster will be deleted and replaced with new Linodes on a rolling basis, which may take several minutes. Replacement Nodes are installed with the latest available patch version for the Cluster's current Kubernetes minor release.<br /><br />__Any local storage on deleted Linodes (such as `hostPath` and `emptyDir` volumes, or `local` PersistentVolumes) will be erased.__<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.lke.clusters.post_lke_cluster_recycle 

;
```
</TabItem>
<TabItem value="post_lke_cluster_regenerate">

Regenerate the Kubeconfig file and/or the service account token for a Cluster.<br /><br />This is a helper operation that allows performing both the [Delete a Kubeconfig](https://techdocs.akamai.com/linode-api/reference/delete-lke-cluster-kubeconfig) and the [Delete a service token](https://techdocs.akamai.com/linode-api/reference/delete-lke-service-token) operations with a single request.<br /><br />When using this operation, at least one of `kubeconfig` or `servicetoken` is required.<br /><br />&gt; 📘<br />&gt;<br />&gt; When regenerating a service account token, the cluster's control plane components and Linode CSI drivers are also restarted and configured with the new token. High availability clusters shouldn't experience any disruption, while standard clusters may experience brief control plane downtime while components are restarted.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.lke.clusters.post_lke_cluster_regenerate 
@@json=
'{
"kubeconfig": {{ kubeconfig }}, 
"servicetoken": {{ servicetoken }}
}'
;
```
</TabItem>
<TabItem value="delete_lke_service_token">

Delete and regenerate the service account token for a Cluster.<br /><br />&gt; 📘<br />&gt;<br />&gt; When you regenerate a service account token, the cluster's control plane components and Linode CSI drivers are also restarted and configured with the new token. High availability clusters shouldn't experience any disruption, while standard clusters may experience brief control plane downtime while components are restarted.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.lke.clusters.delete_lke_service_token 

;
```
</TabItem>
</Tabs>
