--- 
title: two_factor_authentication
hide_title: false
hide_table_of_contents: false
keywords:
  - two_factor_authentication
  - profile
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

Creates, updates, deletes, gets or lists a <code>two_factor_authentication</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>two_factor_authentication</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.profile.two_factor_authentication" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#post_tfa_disable"><CopyableCode code="post_tfa_disable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Disables Two Factor Authentication for your User. Once successful, login attempts from untrusted computers will only require a password before being successful. This is less secure, and is discouraged.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_tfa_enable"><CopyableCode code="post_tfa_enable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Generates a Two Factor secret for your User. To enable TFA for your User, enter the secret obtained from this operation with the [Enable two factor authentication](https://techdocs.akamai.com/linode-api/reference/post-tfa-confirm) operation. Once enabled, logins from untrusted computers are required to provide a TFA code before they are successful.<br /><br />Run the [Answer security questions](https://techdocs.akamai.com/linode-api/reference/post-security-questions) operation.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_tfa_confirm"><CopyableCode code="post_tfa_confirm" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Confirms that you can successfully generate Two Factor codes and enables TFA on your Account. Once this is complete, login attempts from untrusted computers will be required to provide a Two Factor code before they are successful.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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

## Lifecycle Methods

<Tabs
    defaultValue="post_tfa_disable"
    values={[
        { label: 'post_tfa_disable', value: 'post_tfa_disable' },
        { label: 'post_tfa_enable', value: 'post_tfa_enable' },
        { label: 'post_tfa_confirm', value: 'post_tfa_confirm' }
    ]}
>
<TabItem value="post_tfa_disable">

Disables Two Factor Authentication for your User. Once successful, login attempts from untrusted computers will only require a password before being successful. This is less secure, and is discouraged.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.profile.two_factor_authentication.post_tfa_disable 
;
```
</TabItem>
<TabItem value="post_tfa_enable">

Generates a Two Factor secret for your User. To enable TFA for your User, enter the secret obtained from this operation with the [Enable two factor authentication](https://techdocs.akamai.com/linode-api/reference/post-tfa-confirm) operation. Once enabled, logins from untrusted computers are required to provide a TFA code before they are successful.<br /><br />Run the [Answer security questions](https://techdocs.akamai.com/linode-api/reference/post-security-questions) operation.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.profile.two_factor_authentication.post_tfa_enable 
;
```
</TabItem>
<TabItem value="post_tfa_confirm">

Confirms that you can successfully generate Two Factor codes and enables TFA on your Account. Once this is complete, login attempts from untrusted computers will be required to provide a Two Factor code before they are successful.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.profile.two_factor_authentication.post_tfa_confirm 
@@json=
'{
"tfa_code": "{{ tfa_code }}"
}';
```
</TabItem>
</Tabs>
