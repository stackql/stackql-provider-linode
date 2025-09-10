--- 
title: payment_methods
hide_title: false
hide_table_of_contents: false
keywords:
  - payment_methods
  - account
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

Creates, updates, deletes, gets or lists a <code>payment_methods</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>payment_methods</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.account.payment_methods" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_payment_method"
    values={[
        { label: 'get_payment_method', value: 'get_payment_method' },
        { label: 'get_payment_methods', value: 'get_payment_methods' }
    ]}
>
<TabItem value="get_payment_method">

Returns a Payment Method Object.

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
    <td>The unique ID of this Payment Method.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When the Payment Method was added to the Account. (example: 2018-01-15T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="data" /></td>
    <td><code></code></td>
    <td> (x-linode-cli-format: json)</td>
</tr>
<tr>
    <td><CopyableCode code="is_default" /></td>
    <td><code>boolean</code></td>
    <td>Whether this Payment Method is the default method for automatically processing service charges.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of Payment Method. (example: credit_card)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_payment_methods">

Returns a paginated list of Payment Method objects.

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
    <td><a href="#get_payment_method"><CopyableCode code="get_payment_method" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>View the details of the specified Payment Method.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_payment_methods"><CopyableCode code="get_payment_methods" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Returns a paginated list of Payment Methods for this Account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_payment_method"><CopyableCode code="post_payment_method" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__type"><code>data__type</code></a>, <a href="#parameter-data__data"><code>data__data</code></a>, <a href="#parameter-data__is_default"><code>data__is_default</code></a></td>
    <td></td>
    <td>Adds a Payment Method to your Account with the option to set it as the default method.<br /><br />- Adding a default Payment Method removes the default status from any other Payment Method.<br /><br />- An Account can have up to 6 active Payment Methods.<br /><br />- Up to 60 Payment Methods can be added each day.<br /><br />- Prior to adding a Payment Method, ensure that your billing address information is up-to-date with a valid `zip` by running the [Update your account](https://techdocs.akamai.com/linode-api/reference/put-account) operation.<br /><br />- A `payment_method_add` event is generated when a payment is successfully submitted.<br /><br />__Parent and child accounts__<br /><br />In a [parent and child account](https://www.linode.com/docs/guides/parent-child-accounts/) environment, the following apply:<br /><br />- Child account users can't run this operation. These users don't have access to billing-related operations.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_payment_method"><CopyableCode code="delete_payment_method" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deactivate the specified Payment Method.<br /><br />The default Payment Method can not be deleted. To add a new default Payment Method, run the [Add a payment method](https://techdocs.akamai.com/linode-api/reference/post-payment-method) operation. To designate an existing Payment Method as the default method, run the [Set a default payment method](https://techdocs.akamai.com/linode-api/reference/post-make-payment-method-default) operation.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_make_payment_method_default"><CopyableCode code="post_make_payment_method_default" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Make the specified Payment Method the default method for automatically processing payments. Removes the default status from any other Payment Method.<br /><br />__Parent and child accounts__<br /><br />In a [parent and child account](https://www.linode.com/docs/guides/parent-child-accounts/) environment, the following apply:<br /><br />- Child account users can't run this operation. These users don't have access to billing-related operations.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_payment_method"
    values={[
        { label: 'get_payment_method', value: 'get_payment_method' },
        { label: 'get_payment_methods', value: 'get_payment_methods' }
    ]}
>
<TabItem value="get_payment_method">

View the details of the specified Payment Method.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
created,
data,
is_default,
type
FROM linode.account.payment_methods;
```
</TabItem>
<TabItem value="get_payment_methods">

Returns a paginated list of Payment Methods for this Account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.account.payment_methods
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}';
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_payment_method"
    values={[
        { label: 'post_payment_method', value: 'post_payment_method' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_payment_method">

Adds a Payment Method to your Account with the option to set it as the default method.<br /><br />- Adding a default Payment Method removes the default status from any other Payment Method.<br /><br />- An Account can have up to 6 active Payment Methods.<br /><br />- Up to 60 Payment Methods can be added each day.<br /><br />- Prior to adding a Payment Method, ensure that your billing address information is up-to-date with a valid `zip` by running the [Update your account](https://techdocs.akamai.com/linode-api/reference/put-account) operation.<br /><br />- A `payment_method_add` event is generated when a payment is successfully submitted.<br /><br />__Parent and child accounts__<br /><br />In a [parent and child account](https://www.linode.com/docs/guides/parent-child-accounts/) environment, the following apply:<br /><br />- Child account users can't run this operation. These users don't have access to billing-related operations.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.account.payment_methods (
data__data,
data__is_default,
data__type
)
SELECT 
'{{ data }}' --required,
{{ is_default }} --required,
'{{ type }}' --required
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: payment_methods
  props:
    - name: data
      value: object
      description: >
        An object representing the credit card information you have on file with Linode to make Payments against your Account.
        
    - name: is_default
      value: boolean
      description: >
        Whether this Payment Method is the default method for automatically processing service charges.
        
    - name: type
      value: string
      description: >
        The type of Payment Method.

Alternative Payment Methods including Google Pay and PayPal can be added using the Cloud Manager. See the [Manage Payment Methods](https://www.linode.com/docs/products/platform/billing/guides/payment-methods/) guide
for details and instructions.
        
      valid_values: ['credit_card']
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_payment_method"
    values={[
        { label: 'delete_payment_method', value: 'delete_payment_method' }
    ]}
>
<TabItem value="delete_payment_method">

Deactivate the specified Payment Method.<br /><br />The default Payment Method can not be deleted. To add a new default Payment Method, run the [Add a payment method](https://techdocs.akamai.com/linode-api/reference/post-payment-method) operation. To designate an existing Payment Method as the default method, run the [Set a default payment method](https://techdocs.akamai.com/linode-api/reference/post-make-payment-method-default) operation.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.account.payment_methods;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="post_make_payment_method_default"
    values={[
        { label: 'post_make_payment_method_default', value: 'post_make_payment_method_default' }
    ]}
>
<TabItem value="post_make_payment_method_default">

Make the specified Payment Method the default method for automatically processing payments. Removes the default status from any other Payment Method.<br /><br />__Parent and child accounts__<br /><br />In a [parent and child account](https://www.linode.com/docs/guides/parent-child-accounts/) environment, the following apply:<br /><br />- Child account users can't run this operation. These users don't have access to billing-related operations.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.account.payment_methods.post_make_payment_method_default 
;
```
</TabItem>
</Tabs>
