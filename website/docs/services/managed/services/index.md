--- 
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.managed.services" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_managed_service"
    values={[
        { label: 'get_managed_service', value: 'get_managed_service' },
        { label: 'get_managed_services', value: 'get_managed_services' }
    ]}
>
<TabItem value="get_managed_service">

The requested Managed Service.

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
    <td>__Read-only__ This Service's unique ID.</td>
</tr>
<tr>
    <td><CopyableCode code="address" /></td>
    <td><code>string (url)</code></td>
    <td>The URL at which this Service is monitored. URL parameters such as `?no-cache=1` are preserved. URL fragments/anchors such as `#monitor` are __not__ preserved. (example: https://example.org)</td>
</tr>
<tr>
    <td><CopyableCode code="body" /></td>
    <td><code>string</code></td>
    <td>What to expect to find in the response body for the Service to be considered up. (example: it worked)</td>
</tr>
<tr>
    <td><CopyableCode code="consultation_group" /></td>
    <td><code>string</code></td>
    <td>The group of ManagedContacts who should be notified or consulted with when an Issue is detected. (example: on-call)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When this Managed Service was created. (example: 2018-01-01T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="credentials" /></td>
    <td><code>array</code></td>
    <td>An array of ManagedCredential IDs that should be used when attempting to resolve issues with this Service.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>The label for this Service. This is for display purposes only. (example: prod-1, pattern: <code>[a-zA-Z0-9-_ \.]&#123;3,64&#125;</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Any information relevant to the Service that Linode special forces should know when attempting to resolve Issues. (example: The service name is my-cool-application)</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>The Region in which this Service is located. This is required if address is a private IP, and may not be set otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="service_type" /></td>
    <td><code>string</code></td>
    <td>How this Service is monitored. (example: url)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The current status of this Service. (example: ok)</td>
</tr>
<tr>
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer</code></td>
    <td>How long to wait, in seconds, for a response before considering the Service to be down.</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When this Managed Service was last updated. (example: 2018-03-01T00:01:01)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_managed_services">

A paginated list of Managed Services.

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
    <td><a href="#get_managed_service"><CopyableCode code="get_managed_service" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns information about a single Managed Service on your Account.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_managed_services"><CopyableCode code="get_managed_services" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns a paginated list of Managed Services on your Account. These are the services Linode Managed is monitoring and will report and attempt to resolve issues with.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_managed_service"><CopyableCode code="post_managed_service" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__label"><code>data__label</code></a>, <a href="#parameter-data__service_type"><code>data__service_type</code></a>, <a href="#parameter-data__address"><code>data__address</code></a>, <a href="#parameter-data__timeout"><code>data__timeout</code></a></td>
    <td></td>
    <td>Creates a Managed Service. Linode Managed will begin monitoring this service and reporting and attempting to resolve any Issues.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_managed_service"><CopyableCode code="put_managed_service" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Updates information about a Managed Service.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_managed_service"><CopyableCode code="delete_managed_service" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes a Managed Service.  This service will no longer be monitored by Linode Managed.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_disable_managed_service"><CopyableCode code="post_disable_managed_service" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Temporarily disables monitoring of a Managed Service.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_enable_managed_service"><CopyableCode code="post_enable_managed_service" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Enables monitoring of a Managed Service.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_managed_service"
    values={[
        { label: 'get_managed_service', value: 'get_managed_service' },
        { label: 'get_managed_services', value: 'get_managed_services' }
    ]}
>
<TabItem value="get_managed_service">

Returns information about a single Managed Service on your Account.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
address,
body,
consultation_group,
created,
credentials,
label,
notes,
region,
service_type,
status,
timeout,
updated
FROM linode.managed.services;
```
</TabItem>
<TabItem value="get_managed_services">

Returns a paginated list of Managed Services on your Account. These are the services Linode Managed is monitoring and will report and attempt to resolve issues with.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.managed.services;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_managed_service"
    values={[
        { label: 'post_managed_service', value: 'post_managed_service' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_managed_service">

Creates a Managed Service. Linode Managed will begin monitoring this service and reporting and attempting to resolve any Issues.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.managed.services (
data__address,
data__body,
data__consultation_group,
data__credentials,
data__label,
data__notes,
data__region,
data__service_type,
data__timeout
)
SELECT 
'{{ address }}' --required,
'{{ body }}',
'{{ consultation_group }}',
'{{ credentials }}',
'{{ label }}' --required,
'{{ notes }}',
'{{ region }}',
'{{ service_type }}' --required,
{{ timeout }} --required
RETURNING
id,
address,
body,
consultation_group,
created,
credentials,
label,
notes,
region,
service_type,
status,
timeout,
updated
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: services
  props:
    - name: address
      value: string
      description: >
        The URL at which this Service is monitored. URL parameters such as `?no-cache=1` are preserved. URL fragments/anchors such as `#monitor` are __not__ preserved.
        
    - name: body
      value: string
      description: >
        What to expect to find in the response body for the Service to be considered up.
        
    - name: consultation_group
      value: string
      description: >
        The group of ManagedContacts who should be notified or consulted with when an Issue is detected.
        
    - name: credentials
      value: array
      description: >
        An array of ManagedCredential IDs that should be used when attempting to resolve issues with this Service.
        
    - name: label
      value: string
      description: >
        The label for this Service. This is for display purposes only.
        
    - name: notes
      value: string
      description: >
        Any information relevant to the Service that Linode special forces should know when attempting to resolve Issues.
        
    - name: region
      value: string
      description: >
        The Region in which this Service is located. This is required if address is a private IP, and may not be set otherwise.
        
    - name: service_type
      value: string
      description: >
        How this Service is monitored.
        
      valid_values: ['url', 'tcp']
    - name: timeout
      value: integer
      description: >
        How long to wait, in seconds, for a response before considering the Service to be down.
        
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_managed_service"
    values={[
        { label: 'put_managed_service', value: 'put_managed_service' }
    ]}
>
<TabItem value="put_managed_service">

Updates information about a Managed Service.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.managed.services
SET 
data__address = '{{ address }}',
data__body = '{{ body }}',
data__consultation_group = '{{ consultation_group }}',
data__credentials = '{{ credentials }}',
data__label = '{{ label }}',
data__notes = '{{ notes }}',
data__region = '{{ region }}',
data__service_type = '{{ service_type }}',
data__timeout = {{ timeout }}
WHERE 

RETURNING
id,
address,
body,
consultation_group,
created,
credentials,
label,
notes,
region,
service_type,
status,
timeout,
updated;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_managed_service"
    values={[
        { label: 'delete_managed_service', value: 'delete_managed_service' }
    ]}
>
<TabItem value="delete_managed_service">

Deletes a Managed Service.  This service will no longer be monitored by Linode Managed.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.managed.services;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="post_disable_managed_service"
    values={[
        { label: 'post_disable_managed_service', value: 'post_disable_managed_service' },
        { label: 'post_enable_managed_service', value: 'post_enable_managed_service' }
    ]}
>
<TabItem value="post_disable_managed_service">

Temporarily disables monitoring of a Managed Service.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.managed.services.post_disable_managed_service 
;
```
</TabItem>
<TabItem value="post_enable_managed_service">

Enables monitoring of a Managed Service.<br /><br />This operation can only be accessed by the unrestricted users of an account.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.managed.services.post_enable_managed_service 
;
```
</TabItem>
</Tabs>
