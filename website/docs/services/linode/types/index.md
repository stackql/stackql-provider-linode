--- 
title: types
hide_title: false
hide_table_of_contents: false
keywords:
  - types
  - linode
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

Creates, updates, deletes, gets or lists a <code>types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.linode.types" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_linode_type"
    values={[
        { label: 'get_linode_type', value: 'get_linode_type' },
        { label: 'get_linode_types', value: 'get_linode_types' }
    ]}
>
<TabItem value="get_linode_type">

A single Linode Type.

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
    <td><code>string</code></td>
    <td>__Read-only__ The ID representing the Linode type. (example: g6-standard-2)</td>
</tr>
<tr>
    <td><CopyableCode code="addons" /></td>
    <td><code>object</code></td>
    <td>__Read-only__ Optional add-on services for Linodes and their associated cost.</td>
</tr>
<tr>
    <td><CopyableCode code="class" /></td>
    <td><code>string</code></td>
    <td>__Filterable__, __Read-only__ The class of the Linode type.  - `nanode`. These instances are good for low-duty workloads, where performance isn't critical.  - `standard`. These instances are good for medium-duty workloads, and offer a good mix of performance, resources, and price.  - `dedicated`. These instances are good for full-duty workloads where consistent performance is important.  - `premium` (limited regions). This includes the features of a `dedicated` instance as well as the latest AMD EPYC&trade; CPUs. This ensures your applications are running on the latest hardware with consistently high performance. Only available in [regions](https://techdocs.akamai.com/linode-api/reference/get-regions) with "Premium Plans" in their `capabilities`.  - `gpu` (limited regions). Linodes with dedicated NVIDIA Quadro&reg; RTX 6000 GPUs accelerate highly specialized applications such as machine learning, AI, and video transcoding. Only available in [regions](https://techdocs.akamai.com/linode-api/reference/get-regions) with `GPU Linodes` in their `capabilities`.  - `accelerated` (limited regions). These leverage the power of dedicated, application-specific integrated circuits (ASIC), starting with NETINT Video Processing Units (VPUs). They're ideal for video transcoding, media processing, and other compute-heavy workloads. Designed to offload specialized tasks, these instances deliver faster processing times and greater efficiency than traditional CPU-based solutions. Only available in [regions](https://techdocs.akamai.com/linode-api/reference/get-regions) with `Accelerated` in their `capabilities`.  - `highmem`. High Memory instances favor RAM over other resources, and can be good for memory hungry use cases like caching and in-memory databases. All High Memory plans contain dedicated CPU cores.  &gt; 📘 &gt; &gt; - A `nanode` class is listed as a 1 GB Linode in Cloud Manager. The API, the CLI, and billing continue to refer to these as a Nanode. &gt; &gt; - A `standard` class is listed as a Shared Linode in Cloud Manager. The API, the CLI, and billing still refer to these as Standard. (example: standard)</td>
</tr>
<tr>
    <td><CopyableCode code="disk" /></td>
    <td><code>integer</code></td>
    <td>__Filterable__, __Read-only__ The Linode type's disk size in MB.</td>
</tr>
<tr>
    <td><CopyableCode code="gpus" /></td>
    <td><code>integer</code></td>
    <td>__Filterable__, __Read-only__ The number of GPUs this Linode type offers.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Filterable__, __Read-only__ The display name for the Linode type. (example: Linode 4GB)</td>
</tr>
<tr>
    <td><CopyableCode code="memory" /></td>
    <td><code>integer</code></td>
    <td>__Filterable__, __Read-only__ Amount of RAM included in this Linode type.</td>
</tr>
<tr>
    <td><CopyableCode code="network_out" /></td>
    <td><code>integer</code></td>
    <td>__Filterable__, __Read-only__ The Mbits outbound bandwidth allocation.</td>
</tr>
<tr>
    <td><CopyableCode code="price" /></td>
    <td><code>object</code></td>
    <td>__Read-only__ The default cost of provisioning this Linode type. Prices are in U.S. dollars, broken down into hourly and monthly charges. Certain regions have different prices. For region-specific pricing, see `region_prices`.</td>
</tr>
<tr>
    <td><CopyableCode code="region_prices" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="successor" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ After a [mutate](https://techdocs.akamai.com/linode-api/reference/post-mutate-linode-instance), the Linode is upgraded to this Linode type. If `null`, this Linode type can't be mutated.</td>
</tr>
<tr>
    <td><CopyableCode code="transfer" /></td>
    <td><code>integer</code></td>
    <td>__Filterable__, __Read-only__ The monthly outbound transfer amount in MB.</td>
</tr>
<tr>
    <td><CopyableCode code="vcpus" /></td>
    <td><code>integer</code></td>
    <td>__Filterable__, __Read-only__ The number of VCPU cores this Linode type offers.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_linode_types">

A collection of Linode Types.

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
    <td>The Linode types.</td>
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
    <td><a href="#get_linode_type"><CopyableCode code="get_linode_type" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns information about a specific Linode Type, including pricing and specifications. This is used when [creating](https://techdocs.akamai.com/linode-api/reference/post-linode-instance) or [resizing](https://techdocs.akamai.com/linode-api/reference/post-resize-linode-instance) Linodes.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)</td>
</tr>
<tr>
    <td><a href="#get_linode_types"><CopyableCode code="get_linode_types" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns Linode Types, including pricing and specifications for each Type. Use these when [creating](https://techdocs.akamai.com/linode-api/reference/post-linode-instance) or [resizing](https://techdocs.akamai.com/linode-api/reference/post-resize-linode-instance) Linodes.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)</td>
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
    defaultValue="get_linode_type"
    values={[
        { label: 'get_linode_type', value: 'get_linode_type' },
        { label: 'get_linode_types', value: 'get_linode_types' }
    ]}
>
<TabItem value="get_linode_type">

Returns information about a specific Linode Type, including pricing and specifications. This is used when [creating](https://techdocs.akamai.com/linode-api/reference/post-linode-instance) or [resizing](https://techdocs.akamai.com/linode-api/reference/post-resize-linode-instance) Linodes.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)

```sql
SELECT
id,
addons,
class,
disk,
gpus,
label,
memory,
network_out,
price,
region_prices,
successor,
transfer,
vcpus
FROM linode.linode.types;
```
</TabItem>
<TabItem value="get_linode_types">

Returns Linode Types, including pricing and specifications for each Type. Use these when [creating](https://techdocs.akamai.com/linode-api/reference/post-linode-instance) or [resizing](https://techdocs.akamai.com/linode-api/reference/post-resize-linode-instance) Linodes.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)

```sql
SELECT
data,
page,
pages,
results
FROM linode.linode.types;
```
</TabItem>
</Tabs>
