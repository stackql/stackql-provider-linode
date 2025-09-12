--- 
title: oauth_clients
hide_title: false
hide_table_of_contents: false
keywords:
  - oauth_clients
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

Creates, updates, deletes, gets or lists an <code>oauth_clients</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>oauth_clients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.account.oauth_clients" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_client"
    values={[
        { label: 'get_client', value: 'get_client' },
        { label: 'get_clients', value: 'get_clients' }
    ]}
>
<TabItem value="get_client">

Information about the requested client.

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
    <td>__Read-only__ The OAuth Client ID.  This is used to identify the client, and is a publicly known value (it is not a secret). (example: 2737bf16b39ab5d7b4a1)</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The name of this application.  This will be presented to users when they are asked to grant it access to their Account. (example: Test_Client_1)</td>
</tr>
<tr>
    <td><CopyableCode code="public" /></td>
    <td><code>boolean</code></td>
    <td>__Filterable__ If this is a public or private OAuth Client.  Public clients have a slightly different authentication workflow than private clients.  See the [OAuth spec](https://oauth.net/2/) for more details.</td>
</tr>
<tr>
    <td><CopyableCode code="redirect_uri" /></td>
    <td><code>string (url)</code></td>
    <td>The location a successful log in from [login.linode.com](https://login.linode.com) should be redirected to for this client.  The receiver of this redirect should be ready to accept an OAuth exchange code and finish the OAuth exchange. (example: https://example.org/oauth/callback)</td>
</tr>
<tr>
    <td><CopyableCode code="secret" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The OAuth Client secret, used in the OAuth exchange.  This is returned as `<REDACTED>` except when an OAuth Client is created or its secret is reset.  This is a secret, and should not be shared or disclosed publicly. (example: &lt;REDACTED&gt;)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The status of this application.  `active` by default. (example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="thumbnail_url" /></td>
    <td><code>string (url)</code></td>
    <td>__Read-only__ The URL where this client's thumbnail may be viewed, or `null` if this client does not have a thumbnail set. (example: https://api.linode.com/v4/account/clients/2737bf16b39ab5d7b4a1/thumbnail)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_clients">

A paginated list of OAuth Clients.

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
    <td><a href="#get_client"><CopyableCode code="get_client" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns information about a single OAuth client.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_clients"><CopyableCode code="get_clients" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Returns a paginated list of OAuth Clients registered to your Account.  OAuth Clients allow users to log into applications you write or host using their Linode Account, and may allow them to grant some level of access to their Linodes or other entities to your application.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_client"><CopyableCode code="post_client" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__label"><code>data__label</code></a>, <a href="#parameter-data__redirect_uri"><code>data__redirect_uri</code></a></td>
    <td></td>
    <td>Creates an OAuth Client, which can be used to allow users (using their Linode account) to log in to your own application, and optionally grant your application some amount of access to their Linodes or other entities.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_client"><CopyableCode code="put_client" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Update information about an OAuth Client on your Account. This can be especially useful to update the `redirect_uri` of your client in the event that the callback URL changed in your application.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_client"><CopyableCode code="delete_client" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes an OAuth Client registered with Linode. The Client ID and Client secret will no longer be accepted by [login.linode.com](https://login.linode.com), and all tokens issued to this client will be invalidated (meaning that if your application was using a token, it will no longer work).<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_reset_client_secret"><CopyableCode code="post_reset_client_secret" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Resets the OAuth Client secret for a client you own, and returns the OAuth Client with the plaintext secret. This secret is not supposed to be publicly known or disclosed anywhere. This can be used to generate a new secret in case the one you have has been leaked, or to get a new secret if you lost the original. The old secret is expired immediately, and logins to your client with the old secret will fail.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_client_thumbnail"><CopyableCode code="get_client_thumbnail" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Returns the PNG thumbnail for this OAuth Client.  This is a publicly viewable endpoint, and can be accessed without authentication.</td>
</tr>
<tr>
    <td><a href="#put_client_thumbnail"><CopyableCode code="put_client_thumbnail" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Upload a thumbnail for a client you own.  You must upload a PNG image file that will be returned when the thumbnail is retrieved.  This image will be publicly viewable. __OAuth scopes__.<br /><br />    ```<br />    account:read_write<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_client"
    values={[
        { label: 'get_client', value: 'get_client' },
        { label: 'get_clients', value: 'get_clients' }
    ]}
>
<TabItem value="get_client">

Returns information about a single OAuth client.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
label,
public,
redirect_uri,
secret,
status,
thumbnail_url
FROM linode.account.oauth_clients
;
```
</TabItem>
<TabItem value="get_clients">

Returns a paginated list of OAuth Clients registered to your Account.  OAuth Clients allow users to log into applications you write or host using their Linode Account, and may allow them to grant some level of access to their Linodes or other entities to your application.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.account.oauth_clients
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_client"
    values={[
        { label: 'post_client', value: 'post_client' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_client">

Creates an OAuth Client, which can be used to allow users (using their Linode account) to log in to your own application, and optionally grant your application some amount of access to their Linodes or other entities.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.account.oauth_clients (
data__label,
data__public,
data__redirect_uri
)
SELECT 
'{{ label }}' /* required */,
{{ public }},
'{{ redirect_uri }}' /* required */
RETURNING
id,
label,
public,
redirect_uri,
secret,
status,
thumbnail_url
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: oauth_clients
  props:
    - name: label
      value: string
      description: >
        __Filterable__ The name of this application.  This will be presented to users when they are asked to grant it access to their Account.
        
    - name: public
      value: boolean
      description: >
        __Filterable__ If this is a public or private OAuth Client.  Public clients have a slightly different authentication workflow than private clients.  See the [OAuth spec](https://oauth.net/2/) for more details.
        
      default: false
    - name: redirect_uri
      value: string
      description: >
        The location a successful log in from [login.linode.com](https://login.linode.com) should be redirected to for this client.  The receiver of this redirect should be ready to accept an OAuth exchange code and finish the OAuth exchange.
        
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_client"
    values={[
        { label: 'put_client', value: 'put_client' }
    ]}
>
<TabItem value="put_client">

Update information about an OAuth Client on your Account. This can be especially useful to update the `redirect_uri` of your client in the event that the callback URL changed in your application.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.account.oauth_clients
SET 
data__label = '{{ label }}',
data__public = {{ public }},
data__redirect_uri = '{{ redirect_uri }}'
RETURNING
id,
label,
public,
redirect_uri,
secret,
status,
thumbnail_url;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_client"
    values={[
        { label: 'delete_client', value: 'delete_client' }
    ]}
>
<TabItem value="delete_client">

Deletes an OAuth Client registered with Linode. The Client ID and Client secret will no longer be accepted by [login.linode.com](https://login.linode.com), and all tokens issued to this client will be invalidated (meaning that if your application was using a token, it will no longer work).<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.account.oauth_clients
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="post_reset_client_secret"
    values={[
        { label: 'post_reset_client_secret', value: 'post_reset_client_secret' },
        { label: 'get_client_thumbnail', value: 'get_client_thumbnail' },
        { label: 'put_client_thumbnail', value: 'put_client_thumbnail' }
    ]}
>
<TabItem value="post_reset_client_secret">

Resets the OAuth Client secret for a client you own, and returns the OAuth Client with the plaintext secret. This secret is not supposed to be publicly known or disclosed anywhere. This can be used to generate a new secret in case the one you have has been leaked, or to get a new secret if you lost the original. The old secret is expired immediately, and logins to your client with the old secret will fail.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.account.oauth_clients.post_reset_client_secret 

;
```
</TabItem>
<TabItem value="get_client_thumbnail">

Returns the PNG thumbnail for this OAuth Client.  This is a publicly viewable endpoint, and can be accessed without authentication.

```sql
EXEC linode.account.oauth_clients.get_client_thumbnail 

;
```
</TabItem>
<TabItem value="put_client_thumbnail">

Upload a thumbnail for a client you own.  You must upload a PNG image file that will be returned when the thumbnail is retrieved.  This image will be publicly viewable. __OAuth scopes__.<br /><br />    ```<br />    account:read_write<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.account.oauth_clients.put_client_thumbnail 

;
```
</TabItem>
</Tabs>
