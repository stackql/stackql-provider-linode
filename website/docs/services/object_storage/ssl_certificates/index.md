--- 
title: ssl_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - ssl_certificates
  - object_storage
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

Creates, updates, deletes, gets or lists a <code>ssl_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ssl_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.object_storage.ssl_certificates" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_object_storage_ssl"
    values={[
        { label: 'get_object_storage_ssl', value: 'get_object_storage_ssl' }
    ]}
>
<TabItem value="get_object_storage_ssl">

Returns a boolean value indicating if this bucket has a corresponding TLS/SSL certificate that was uploaded by an Account user.

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
    <td><CopyableCode code="ssl" /></td>
    <td><code>boolean</code></td>
    <td>__Read-only__ A boolean indicating if this Bucket has a corresponding TLS/SSL certificate that was uploaded by an Account user.</td>
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
    <td><a href="#get_object_storage_ssl"><CopyableCode code="get_object_storage_ssl" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns a boolean value indicating if this bucket has a corresponding TLS/SSL certificate that was uploaded by an Account user.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_object_storage_ssl"><CopyableCode code="post_object_storage_ssl" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__certificate"><code>data__certificate</code></a>, <a href="#parameter-data__private_key"><code>data__private_key</code></a></td>
    <td></td>
    <td>Upload a TLS/SSL certificate and private key to be served when you visit your Object Storage bucket via HTTPS. Your TLS/SSL certificate and private key are stored encrypted at rest.<br /><br />To replace an expired certificate, [delete your current certificates](https://techdocs.akamai.com/linode-api/reference/delete-object-storage-ssl) and upload a new one.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_object_storage_ssl"><CopyableCode code="delete_object_storage_ssl" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes this Object Storage bucket's user uploaded TLS/SSL certificate and private key.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_object_storage_ssl"
    values={[
        { label: 'get_object_storage_ssl', value: 'get_object_storage_ssl' }
    ]}
>
<TabItem value="get_object_storage_ssl">

Returns a boolean value indicating if this bucket has a corresponding TLS/SSL certificate that was uploaded by an Account user.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
ssl
FROM linode.object_storage.ssl_certificates;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_object_storage_ssl"
    values={[
        { label: 'post_object_storage_ssl', value: 'post_object_storage_ssl' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_object_storage_ssl">

Upload a TLS/SSL certificate and private key to be served when you visit your Object Storage bucket via HTTPS. Your TLS/SSL certificate and private key are stored encrypted at rest.<br /><br />To replace an expired certificate, [delete your current certificates](https://techdocs.akamai.com/linode-api/reference/delete-object-storage-ssl) and upload a new one.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.object_storage.ssl_certificates (
data__certificate,
data__private_key
)
SELECT 
'{{ certificate }}' --required,
'{{ private_key }}' --required
RETURNING
ssl
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: ssl_certificates
  props:
    - name: certificate
      value: string
      description: >
        Your Base64 encoded and PEM formatted SSL certificate.

Line breaks must be represented as `\n` in the string for requests (but not when using the Linode CLI)
        
    - name: private_key
      value: string
      description: >
        The private key associated with this TLS/SSL certificate.

Line breaks must be represented as `\n` in the string for requests (but not when using the Linode CLI)
        
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_object_storage_ssl"
    values={[
        { label: 'delete_object_storage_ssl', value: 'delete_object_storage_ssl' }
    ]}
>
<TabItem value="delete_object_storage_ssl">

Deletes this Object Storage bucket's user uploaded TLS/SSL certificate and private key.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.object_storage.ssl_certificates;
```
</TabItem>
</Tabs>
