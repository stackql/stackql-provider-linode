--- 
title: user_grants
hide_title: false
hide_table_of_contents: false
keywords:
  - user_grants
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

Creates, updates, deletes, gets or lists a <code>user_grants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.account.user_grants" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_user_grants"
    values={[
        { label: 'get_user_grants', value: 'get_user_grants' }
    ]}
>
<TabItem value="get_user_grants">

The User's grants.

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
    <td><CopyableCode code="database" /></td>
    <td><code>array</code></td>
    <td>The grants this user has for individual Managed Databases on this account.</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>array</code></td>
    <td>The grants this user has for individual domains on this account.</td>
</tr>
<tr>
    <td><CopyableCode code="firewall" /></td>
    <td><code>array</code></td>
    <td>The grants this user has for individual firewalls on this account.</td>
</tr>
<tr>
    <td><CopyableCode code="global" /></td>
    <td><code>object</code></td>
    <td>The grants the user has to all resources on your account.</td>
</tr>
<tr>
    <td><CopyableCode code="image" /></td>
    <td><code>array</code></td>
    <td>The grants this user has for individual images on this account.</td>
</tr>
<tr>
    <td><CopyableCode code="linode" /></td>
    <td><code>array</code></td>
    <td>The grants this user has for individual Linodes on this account.</td>
</tr>
<tr>
    <td><CopyableCode code="longview" /></td>
    <td><code>array</code></td>
    <td>The grants this user has for individual Longview Clients on this account.</td>
</tr>
<tr>
    <td><CopyableCode code="nodebalancer" /></td>
    <td><code>array</code></td>
    <td>The grants this user has for individual NodeBalancers on this account.</td>
</tr>
<tr>
    <td><CopyableCode code="stackscript" /></td>
    <td><code>array</code></td>
    <td>The grants this User has for individual StackScripts on this account.</td>
</tr>
<tr>
    <td><CopyableCode code="volume" /></td>
    <td><code>array</code></td>
    <td>The grants this user has individual Block Storage Volumes on this account.</td>
</tr>
<tr>
    <td><CopyableCode code="vpc" /></td>
    <td><code>array</code></td>
    <td>The grants this user has individual Virtual Private Clouds (VPCs) on this account.</td>
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
    <td><a href="#get_user_grants"><CopyableCode code="get_user_grants" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns the full grants structure for an account username you specify. This includes all entities on the account, and the level of access this user has to each of them.<br /><br />This doesn't apply to the account owner or the current authenticated user. You can run the [List grants](https://techdocs.akamai.com/linode-api/reference/get-profile-grants) operation to view those grants. However, this doesn't show the entities that they _don't_ have access to.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation can only be accessed by account users with _unrestricted_ access. __OAuth scopes__.<br /><br />    ```<br />    account:read_only<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_user_grants"><CopyableCode code="put_user_grants" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Update the grants for a [restricted](https://techdocs.akamai.com/linode-api/reference/post-user) user. This can be used to give a user access to new entities or actions, or take access away. Omit a grant object from the request to keep its current setting.<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation can only be accessed by account users with _unrestricted_ access.<br />&gt;<br />&gt; - This operation only applies to _restricted_ users. An unrestricted user has access to everything and doesn't use grants.<br /><br />__Parent and child accounts__<br /><br />In a [parent and child account](https://www.linode.com/docs/guides/parent-child-accounts/) environment, the following apply:<br /><br />- No child account user can modify the `account_access` grant for the child account parent user (proxy user).<br /><br />- An unrestricted child account user can configure all other grants for the proxy user, with the `global` object.<br /><br />- An unrestricted child account user can enable the `account_access` grant for other child account users. However, enabled child users are still subject to child user restrictions--they can't perform write operations for any billing or account information. __OAuth scopes__.<br /><br />    ```<br />    account:read_write<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_user_grants"
    values={[
        { label: 'get_user_grants', value: 'get_user_grants' }
    ]}
>
<TabItem value="get_user_grants">

Returns the full grants structure for an account username you specify. This includes all entities on the account, and the level of access this user has to each of them.<br /><br />This doesn't apply to the account owner or the current authenticated user. You can run the [List grants](https://techdocs.akamai.com/linode-api/reference/get-profile-grants) operation to view those grants. However, this doesn't show the entities that they _don't_ have access to.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation can only be accessed by account users with _unrestricted_ access. __OAuth scopes__.<br /><br />    ```<br />    account:read_only<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
database,
domain,
firewall,
global,
image,
linode,
longview,
nodebalancer,
stackscript,
volume,
vpc
FROM linode.account.user_grants
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_user_grants"
    values={[
        { label: 'put_user_grants', value: 'put_user_grants' }
    ]}
>
<TabItem value="put_user_grants">

Update the grants for a [restricted](https://techdocs.akamai.com/linode-api/reference/post-user) user. This can be used to give a user access to new entities or actions, or take access away. Omit a grant object from the request to keep its current setting.<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation can only be accessed by account users with _unrestricted_ access.<br />&gt;<br />&gt; - This operation only applies to _restricted_ users. An unrestricted user has access to everything and doesn't use grants.<br /><br />__Parent and child accounts__<br /><br />In a [parent and child account](https://www.linode.com/docs/guides/parent-child-accounts/) environment, the following apply:<br /><br />- No child account user can modify the `account_access` grant for the child account parent user (proxy user).<br /><br />- An unrestricted child account user can configure all other grants for the proxy user, with the `global` object.<br /><br />- An unrestricted child account user can enable the `account_access` grant for other child account users. However, enabled child users are still subject to child user restrictions--they can't perform write operations for any billing or account information. __OAuth scopes__.<br /><br />    ```<br />    account:read_write<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.account.user_grants
SET 
data__database = '{{ database }}',
data__domain = '{{ domain }}',
data__firewall = '{{ firewall }}',
data__global = '{{ global }}',
data__image = '{{ image }}',
data__linode = '{{ linode }}',
data__longview = '{{ longview }}',
data__nodebalancer = '{{ nodebalancer }}',
data__stackscript = '{{ stackscript }}',
data__volume = '{{ volume }}',
data__vpc = '{{ vpc }}'
RETURNING
database,
domain,
firewall,
global,
image,
linode,
longview,
nodebalancer,
stackscript,
volume,
vpc;
```
</TabItem>
</Tabs>
