--- 
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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

Creates, updates, deletes, gets or lists a <code>users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.account.users" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_user"
    values={[
        { label: 'get_user', value: 'get_user' },
        { label: 'get_users', value: 'get_users' }
    ]}
>
<TabItem value="get_user">

The requested User object.

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
<TabItem value="get_users">

A paginated list of users.

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
    <td><a href="#get_user"><CopyableCode code="get_user" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns information about a single user on your account.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation can only be accessed by account users with _unrestricted_ access.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_users"><CopyableCode code="get_users" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Returns a paginated list of all users on your account.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation can only be accessed by account users with _unrestricted_ access.<br /><br />A user can access all or part of an account based on their access status and grants:<br /><br />- __Unrestricted access__. These users can access everything on an account.<br /><br />- __Restricted access__. These users can only access entities or perform actions they've been given specific grants to.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_user"><CopyableCode code="post_user" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__username"><code>data__username</code></a>, <a href="#parameter-data__email"><code>data__email</code></a></td>
    <td></td>
    <td>Creates a user on your account. You determine the new user's account access by setting it to restricted or unrestricted and by defining its grants. After completion, the API sends a confirmation message containing password creation and login instructions to the user's `email` address.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation can only be accessed by account users with _unrestricted_ access.<br /><br />__Parent and child accounts__<br /><br />In a [parent and child account](https://www.linode.com/docs/guides/parent-child-accounts/) environment, the following apply:<br /><br />- A parent account user can create new parent account users.<br /><br />- A child account can [update](https://techdocs.akamai.com/linode-api/reference/put-user) the child account parent user (proxy user) to `unrestricted`. This gives the proxy user access to create new child account users.<br /><br />- A child account user can create new child account users.<br /><br />- You can't create a proxy user. The proxy user in a child account is predefined when you initially provision the parent-child relationship.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_user"><CopyableCode code="put_user" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Update information about a user on your account, including its restricted status. When setting a user to `restricted`, the API sets no grants for it. You need to set grants so that user can access things on the account.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation can only be accessed by account users with _unrestricted_ access.<br /><br />__Parent and child accounts__<br /><br />In a [parent and child account](https://www.linode.com/docs/guides/parent-child-accounts/) environment, the following apply:<br /><br />- You can't edit the `username` or `email` values for the child account parent user (proxy user). These are predefined for the proxy user when you initially provision the parent-child relationship. Only a proxy user's `restricted` status can be modified. This can only be done by an unrestricted child account user.<br /><br />- A parent account using an unrestricted proxy user in a child account can modify the `username`, `email`, and `restricted` status for an existing child account user.<br /><br />- A restricted account user--parent or child--can't change their user to `unrestricted`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_user"><CopyableCode code="delete_user" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes a user. The API immediately logs the user out and removes all of its `grants`.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation can only be accessed by account users with _unrestricted_ access.<br /><br />__Parent and child accounts__<br /><br />In a [parent and child account](https://www.linode.com/docs/guides/parent-child-accounts/) environment, the following apply:<br /><br />- You can't delete a child account parent user (proxy user). The API returns a 403 error if you target a proxy user with this operation.<br /><br />- A parent account using an unrestricted proxy user can use this operation to delete a child account user.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_user"
    values={[
        { label: 'get_user', value: 'get_user' },
        { label: 'get_users', value: 'get_users' }
    ]}
>
<TabItem value="get_user">

Returns information about a single user on your account.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation can only be accessed by account users with _unrestricted_ access.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
*
FROM linode.account.users;
```
</TabItem>
<TabItem value="get_users">

Returns a paginated list of all users on your account.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation can only be accessed by account users with _unrestricted_ access.<br /><br />A user can access all or part of an account based on their access status and grants:<br /><br />- __Unrestricted access__. These users can access everything on an account.<br /><br />- __Restricted access__. These users can only access entities or perform actions they've been given specific grants to.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.account.users
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}';
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_user"
    values={[
        { label: 'post_user', value: 'post_user' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_user">

Creates a user on your account. You determine the new user's account access by setting it to restricted or unrestricted and by defining its grants. After completion, the API sends a confirmation message containing password creation and login instructions to the user's `email` address.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation can only be accessed by account users with _unrestricted_ access.<br /><br />__Parent and child accounts__<br /><br />In a [parent and child account](https://www.linode.com/docs/guides/parent-child-accounts/) environment, the following apply:<br /><br />- A parent account user can create new parent account users.<br /><br />- A child account can [update](https://techdocs.akamai.com/linode-api/reference/put-user) the child account parent user (proxy user) to `unrestricted`. This gives the proxy user access to create new child account users.<br /><br />- A child account user can create new child account users.<br /><br />- You can't create a proxy user. The proxy user in a child account is predefined when you initially provision the parent-child relationship.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.account.users (
data__email,
data__restricted,
data__username
)
SELECT 
'{{ email }}' --required,
{{ restricted }},
'{{ username }}' --required
RETURNING
email,
last_login,
password_created,
restricted,
ssh_keys,
tfa_enabled,
username,
verified_phone_number
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: users
  props:
    - name: email
      value: string
      description: >
        This user's email address. Akamai uses this address for account management communications.
        
    - name: restricted
      value: boolean
      description: >
        If `true`, this user needs specific access granted to perform actions or access entities on your account. Run [List a user's grants](https://techdocs.akamai.com/linode-api/reference/get-user-grants) for details on how to configure grants for a restricted user.
        
    - name: username
      value: string
      description: >
        __Filterable__ The name of this user. This user needs to use this value to log in. It may also display alongside actions this user performs, including events or public StackScripts.
        
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_user"
    values={[
        { label: 'put_user', value: 'put_user' }
    ]}
>
<TabItem value="put_user">

Update information about a user on your account, including its restricted status. When setting a user to `restricted`, the API sets no grants for it. You need to set grants so that user can access things on the account.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation can only be accessed by account users with _unrestricted_ access.<br /><br />__Parent and child accounts__<br /><br />In a [parent and child account](https://www.linode.com/docs/guides/parent-child-accounts/) environment, the following apply:<br /><br />- You can't edit the `username` or `email` values for the child account parent user (proxy user). These are predefined for the proxy user when you initially provision the parent-child relationship. Only a proxy user's `restricted` status can be modified. This can only be done by an unrestricted child account user.<br /><br />- A parent account using an unrestricted proxy user in a child account can modify the `username`, `email`, and `restricted` status for an existing child account user.<br /><br />- A restricted account user--parent or child--can't change their user to `unrestricted`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.account.users
SET 
data__email = '{{ email }}',
data__restricted = {{ restricted }},
data__username = '{{ username }}'
WHERE 

RETURNING
email,
last_login,
password_created,
restricted,
ssh_keys,
tfa_enabled,
user_type,
username,
verified_phone_number;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_user"
    values={[
        { label: 'delete_user', value: 'delete_user' }
    ]}
>
<TabItem value="delete_user">

Deletes a user. The API immediately logs the user out and removes all of its `grants`.<br /><br />&gt; 📘<br />&gt;<br />&gt; This operation can only be accessed by account users with _unrestricted_ access.<br /><br />__Parent and child accounts__<br /><br />In a [parent and child account](https://www.linode.com/docs/guides/parent-child-accounts/) environment, the following apply:<br /><br />- You can't delete a child account parent user (proxy user). The API returns a 403 error if you target a proxy user with this operation.<br /><br />- A parent account using an unrestricted proxy user can use this operation to delete a child account user.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.account.users;
```
</TabItem>
</Tabs>
