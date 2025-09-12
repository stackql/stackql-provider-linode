--- 
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - longview
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

Creates, updates, deletes, gets or lists a <code>subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.longview.subscriptions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_longview_subscription"
    values={[
        { label: 'get_longview_subscription', value: 'get_longview_subscription' },
        { label: 'get_longview_subscriptions', value: 'get_longview_subscriptions' }
    ]}
>
<TabItem value="get_longview_subscription">

The requested Longview Subscription details.

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
    <td>__Read-only__ The unique ID of this Subscription tier. (example: longview-10)</td>
</tr>
<tr>
    <td><CopyableCode code="clients_included" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The number of Longview Clients that may be created with this Subscription tier.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ A display name for this Subscription tier. (example: Longview Pro 10 pack)</td>
</tr>
<tr>
    <td><CopyableCode code="price" /></td>
    <td><code>object</code></td>
    <td>__Read-only__ Pricing information about this Subscription tier.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_longview_subscriptions">

A paginated list of Longview Subscriptions.

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
    <td><a href="#get_longview_subscription"><CopyableCode code="get_longview_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get the Longview plan details as a single `LongviewSubscription` object for the provided subscription ID. This is a public endpoint and requires no authentication.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)</td>
</tr>
<tr>
    <td><a href="#get_longview_subscriptions"><CopyableCode code="get_longview_subscriptions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Returns a paginated list of available Longview Subscriptions. This is a public endpoint and requires no authentication.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)</td>
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
    defaultValue="get_longview_subscription"
    values={[
        { label: 'get_longview_subscription', value: 'get_longview_subscription' },
        { label: 'get_longview_subscriptions', value: 'get_longview_subscriptions' }
    ]}
>
<TabItem value="get_longview_subscription">

Get the Longview plan details as a single `LongviewSubscription` object for the provided subscription ID. This is a public endpoint and requires no authentication.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)

```sql
SELECT
id,
clients_included,
label,
price
FROM linode.longview.subscriptions
;
```
</TabItem>
<TabItem value="get_longview_subscriptions">

Returns a paginated list of available Longview Subscriptions. This is a public endpoint and requires no authentication.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)

```sql
SELECT
data,
page,
pages,
results
FROM linode.longview.subscriptions
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}'
;
```
</TabItem>
</Tabs>
