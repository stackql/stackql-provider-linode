--- 
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
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

Creates, updates, deletes, gets or lists an <code>apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.profile.apps" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_profile_app"
    values={[
        { label: 'get_profile_app', value: 'get_profile_app' },
        { label: 'get_profile_apps', value: 'get_profile_apps' }
    ]}
>
<TabItem value="get_profile_app">

The app requested.

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
    <td>__Read-only__ This authorization's ID, used for revoking access.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Filterable__, __Read-only__ When this app was authorized. (example: 2018-01-01T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="expiry" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Filterable__, __Read-only__ When the app's access to your account expires. If `null`, the app's access must be revoked manually. (example: 2018-01-15T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Filterable__, __Read-only__ The name of the application you've authorized. (example: example-app)</td>
</tr>
<tr>
    <td><CopyableCode code="scopes" /></td>
    <td><code>string (oauth-scopes)</code></td>
    <td>__Read-only__ The OAuth scopes this app was authorized with.  This defines what parts of your Account the app is allowed to access. (example: linodes:read_only)</td>
</tr>
<tr>
    <td><CopyableCode code="thumbnail_url" /></td>
    <td><code>string (url)</code></td>
    <td>__Read-only__ The URL at which this app's thumbnail may be accessed.</td>
</tr>
<tr>
    <td><CopyableCode code="website" /></td>
    <td><code>string (url)</code></td>
    <td>__Read-only__ The website where you can get more information about this app. (example: example.org)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_profile_apps">

A paginated list of apps you've authorized.

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
    <td><a href="#get_profile_app"><CopyableCode code="get_profile_app" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns information about a single app you've authorized to access your Account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_profile_apps"><CopyableCode code="get_profile_apps" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>This is a collection of OAuth apps that you've given access to your Account, and includes the level of access granted.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_profile_app"><CopyableCode code="delete_profile_app" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Expires this app token. This token may no longer be used to access your Account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_profile_app"
    values={[
        { label: 'get_profile_app', value: 'get_profile_app' },
        { label: 'get_profile_apps', value: 'get_profile_apps' }
    ]}
>
<TabItem value="get_profile_app">

Returns information about a single app you've authorized to access your Account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
created,
expiry,
label,
scopes,
thumbnail_url,
website
FROM linode.profile.apps
;
```
</TabItem>
<TabItem value="get_profile_apps">

This is a collection of OAuth apps that you've given access to your Account, and includes the level of access granted.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.profile.apps
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_profile_app"
    values={[
        { label: 'delete_profile_app', value: 'delete_profile_app' }
    ]}
>
<TabItem value="delete_profile_app">

Expires this app token. This token may no longer be used to access your Account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.profile.apps
;
```
</TabItem>
</Tabs>
