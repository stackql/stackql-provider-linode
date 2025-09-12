--- 
title: credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - credentials
  - managed
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

Creates, updates, deletes, gets or lists a <code>credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.managed.credentials" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_managed_credential"
    values={[
        { label: 'get_managed_credential', value: 'get_managed_credential' },
        { label: 'get_managed_credentials', value: 'get_managed_credentials' }
    ]}
>
<TabItem value="get_managed_credential">

The requested Managed Credential.

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
    <td>__Read-only__ This Credential's unique ID.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>The unique label for this Credential. This is for display purposes only. (example: prod-password-1, pattern: <code>[a-zA-Z0-9-_ \.]&#123;2,75&#125;</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="last_decrypted" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ The date this Credential was last decrypted by a member of Linode special forces. (example: 2018-01-01T00:01:01)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_managed_credentials">

A paginated list of ManagedCredentials.

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
    <td><a href="#get_managed_credential"><CopyableCode code="get_managed_credential" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns a single Managed Credential.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_managed_credentials"><CopyableCode code="get_managed_credentials" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Returns a paginated list of Managed Credentials on your Account.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_managed_credential"><CopyableCode code="post_managed_credential" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__label"><code>data__label</code></a>, <a href="#parameter-data__password"><code>data__password</code></a></td>
    <td></td>
    <td>Creates a Managed Credential. A Managed Credential is stored securely to allow Linode special forces to access your Managed Services and resolve issues.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_managed_credential"><CopyableCode code="put_managed_credential" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Updates the label of a Managed Credential. This operation does not update the username and password for a Managed Credential. To do this, run the [Update a managed credential's username and password](https://techdocs.akamai.com/linode-api/reference/post-managed-credential-username-password)) operation instead. This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_managed_credential_revoke"><CopyableCode code="post_managed_credential_revoke" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Deletes a Managed Credential.  Linode special forces will no longer have access to this Credential when attempting to resolve issues.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_managed_credential_username_password"><CopyableCode code="post_managed_credential_username_password" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-password"><code>password</code></a></td>
    <td></td>
    <td>Updates the username and password for a Managed Credential.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_managed_credential"
    values={[
        { label: 'get_managed_credential', value: 'get_managed_credential' },
        { label: 'get_managed_credentials', value: 'get_managed_credentials' }
    ]}
>
<TabItem value="get_managed_credential">

Returns a single Managed Credential.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
label,
last_decrypted
FROM linode.managed.credentials
;
```
</TabItem>
<TabItem value="get_managed_credentials">

Returns a paginated list of Managed Credentials on your Account.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.managed.credentials
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_managed_credential"
    values={[
        { label: 'post_managed_credential', value: 'post_managed_credential' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_managed_credential">

Creates a Managed Credential. A Managed Credential is stored securely to allow Linode special forces to access your Managed Services and resolve issues.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.managed.credentials (
data__label,
data__password,
data__username
)
SELECT 
'{{ label }}' /* required */,
'{{ password }}' /* required */,
'{{ username }}'
RETURNING
id,
label,
last_decrypted
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: credentials
  props:
    - name: label
      value: string
      description: >
        The unique label for this Credential. This is for display purposes only.
        
    - name: password
      value: string
      description: >
        The password to use when accessing the Managed Service.
        
    - name: username
      value: string
      description: >
        The username to use when accessing the Managed Service.
        
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_managed_credential"
    values={[
        { label: 'put_managed_credential', value: 'put_managed_credential' }
    ]}
>
<TabItem value="put_managed_credential">

Updates the label of a Managed Credential. This operation does not update the username and password for a Managed Credential. To do this, run the [Update a managed credential's username and password](https://techdocs.akamai.com/linode-api/reference/post-managed-credential-username-password)) operation instead. This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.managed.credentials
SET 
data__label = '{{ label }}'
RETURNING
id,
label,
last_decrypted;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="post_managed_credential_revoke"
    values={[
        { label: 'post_managed_credential_revoke', value: 'post_managed_credential_revoke' },
        { label: 'post_managed_credential_username_password', value: 'post_managed_credential_username_password' }
    ]}
>
<TabItem value="post_managed_credential_revoke">

Deletes a Managed Credential.  Linode special forces will no longer have access to this Credential when attempting to resolve issues.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.managed.credentials.post_managed_credential_revoke 

;
```
</TabItem>
<TabItem value="post_managed_credential_username_password">

Updates the username and password for a Managed Credential.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.managed.credentials.post_managed_credential_username_password 
@@json=
'{
"password": "{{ password }}", 
"username": "{{ username }}"
}'
;
```
</TabItem>
</Tabs>
