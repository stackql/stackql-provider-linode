--- 
title: stack_scripts
hide_title: false
hide_table_of_contents: false
keywords:
  - stack_scripts
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

Creates, updates, deletes, gets or lists a <code>stack_scripts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stack_scripts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.linode.stack_scripts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_stack_script"
    values={[
        { label: 'get_stack_script', value: 'get_stack_script' },
        { label: 'get_stack_scripts', value: 'get_stack_scripts' }
    ]}
>
<TabItem value="get_stack_script">

A single StackScript.

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
    <td>__Read-only__ The unique ID of this StackScript.</td>
</tr>
<tr>
    <td><CopyableCode code="user_gravatar_id" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The Gravatar ID for the User who created the StackScript. (example: a445b305abda30ebc766bc7fda037c37)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ The date this StackScript was created. (example: 2018-01-01T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="deployments_active" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ Count of currently active, deployed Linodes created from this StackScript.</td>
</tr>
<tr>
    <td><CopyableCode code="deployments_total" /></td>
    <td><code>integer</code></td>
    <td>__Filterable__, __Read-only__ The total number of times this StackScript has been deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ A description for the StackScript. (example: This StackScript installs and configures MySQL)</td>
</tr>
<tr>
    <td><CopyableCode code="images" /></td>
    <td><code>array</code></td>
    <td>An array of Image IDs. These are the Images that can be deployed with this StackScript.  `any/all` indicates that all available Images, including private Images, are accepted.</td>
</tr>
<tr>
    <td><CopyableCode code="is_public" /></td>
    <td><code>boolean</code></td>
    <td>__Filterable__ This determines whether other users can use your StackScript. __Once a StackScript is made public, it cannot be made private.__</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The StackScript's label is for display purposes only. (example: a-stackscript)</td>
</tr>
<tr>
    <td><CopyableCode code="mine" /></td>
    <td><code>boolean</code></td>
    <td>__Filterable__, __Read-only__ Returns `true` if this StackScript is owned by the account of the user making the request, and the user making the request is unrestricted or has access to this StackScript.</td>
</tr>
<tr>
    <td><CopyableCode code="rev_note" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ This field allows you to add notes for the set of revisions made to this StackScript. (example: Set up MySQL)</td>
</tr>
<tr>
    <td><CopyableCode code="script" /></td>
    <td><code>string</code></td>
    <td>The script to execute when provisioning a new Linode with this StackScript. (example: \"#!/bin/bash\", x-linode-cli-format: file)</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ The date this StackScript was last updated. (example: 2018-01-01T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="user_defined_fields" /></td>
    <td><code>array</code></td>
    <td>__Read-only__ This is a list of fields defined with a special syntax inside this StackScript that allow for supplying customized parameters during deployment. See [Declare User-Defined Fields (UDFs)](https://www.linode.com/docs/products/tools/stackscripts/guides/write-a-custom-script/#declare-user-defined-fields-udfs) for more information.</td>
</tr>
<tr>
    <td><CopyableCode code="username" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The User who created the StackScript. (example: myuser)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_stack_scripts">

A list of StackScripts available to the User, including private StackScripts owned by the User if the request is authenticated.

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
    <td><a href="#get_stack_script"><CopyableCode code="get_stack_script" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns all of the information about a specified StackScript, including the contents of the script.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_stack_scripts"><CopyableCode code="get_stack_scripts" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>If the request is not authenticated, only public StackScripts are returned.<br /><br />For more information on StackScripts, please read our [StackScripts documentation](https://www.linode.com/docs/products/tools/stackscripts/).<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_add_stack_script"><CopyableCode code="post_add_stack_script" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__script"><code>data__script</code></a>, <a href="#parameter-data__label"><code>data__label</code></a>, <a href="#parameter-data__images"><code>data__images</code></a></td>
    <td></td>
    <td>Creates a StackScript in your Account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_stack_script"><CopyableCode code="put_stack_script" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Updates a StackScript.<br /><br />__Once a StackScript is made public, it cannot be made private.__<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_stack_script"><CopyableCode code="delete_stack_script" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes a private StackScript you have permission to `read_write`. You cannot delete a public StackScript.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_stack_script"
    values={[
        { label: 'get_stack_script', value: 'get_stack_script' },
        { label: 'get_stack_scripts', value: 'get_stack_scripts' }
    ]}
>
<TabItem value="get_stack_script">

Returns all of the information about a specified StackScript, including the contents of the script.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
user_gravatar_id,
created,
deployments_active,
deployments_total,
description,
images,
is_public,
label,
mine,
rev_note,
script,
updated,
user_defined_fields,
username
FROM linode.linode.stack_scripts;
```
</TabItem>
<TabItem value="get_stack_scripts">

If the request is not authenticated, only public StackScripts are returned.<br /><br />For more information on StackScripts, please read our [StackScripts documentation](https://www.linode.com/docs/products/tools/stackscripts/).<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.linode.stack_scripts
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}';
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_add_stack_script"
    values={[
        { label: 'post_add_stack_script', value: 'post_add_stack_script' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_add_stack_script">

Creates a StackScript in your Account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.linode.stack_scripts (
data__description,
data__images,
data__is_public,
data__label,
data__rev_note,
data__script
)
SELECT 
'{{ description }}',
'{{ images }}' --required,
{{ is_public }},
'{{ label }}' --required,
'{{ rev_note }}',
'{{ script }}' --required
RETURNING
id,
user_gravatar_id,
created,
deployments_active,
deployments_total,
description,
images,
is_public,
label,
mine,
rev_note,
script,
updated,
user_defined_fields,
username
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: stack_scripts
  props:
    - name: description
      value: string
      description: >
        __Filterable__ A description for the StackScript.
        
    - name: images
      value: array
      description: >
        An array of Image IDs. These are the Images that can be deployed with this StackScript.

`any/all` indicates that all available Images, including private Images, are accepted.
        
    - name: is_public
      value: boolean
      description: >
        __Filterable__ This determines whether other users can use your StackScript. __Once a StackScript is made public, it cannot be made private.__
        
    - name: label
      value: string
      description: >
        __Filterable__ The StackScript's label is for display purposes only.
        
    - name: rev_note
      value: string
      description: >
        __Filterable__ This field allows you to add notes for the set of revisions made to this StackScript.
        
    - name: script
      value: string
      description: >
        The script to execute when provisioning a new Linode with this StackScript.
        
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_stack_script"
    values={[
        { label: 'put_stack_script', value: 'put_stack_script' }
    ]}
>
<TabItem value="put_stack_script">

Updates a StackScript.<br /><br />__Once a StackScript is made public, it cannot be made private.__<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.linode.stack_scripts
SET 
data__description = '{{ description }}',
data__images = '{{ images }}',
data__is_public = {{ is_public }},
data__label = '{{ label }}',
data__rev_note = '{{ rev_note }}',
data__script = '{{ script }}'
WHERE 

RETURNING
id,
user_gravatar_id,
created,
deployments_active,
deployments_total,
description,
images,
is_public,
label,
mine,
rev_note,
script,
updated,
user_defined_fields,
username;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_stack_script"
    values={[
        { label: 'delete_stack_script', value: 'delete_stack_script' }
    ]}
>
<TabItem value="delete_stack_script">

Deletes a private StackScript you have permission to `read_write`. You cannot delete a public StackScript.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.linode.stack_scripts;
```
</TabItem>
</Tabs>
