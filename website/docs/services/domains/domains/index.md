--- 
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - domains
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

Creates, updates, deletes, gets or lists a <code>domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.domains.domains" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_domain"
    values={[
        { label: 'get_domain', value: 'get_domain' },
        { label: 'get_domains', value: 'get_domains' }
    ]}
>
<TabItem value="get_domain">

A single Domain in Linode's DNS Manager.

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
    <td>__Read-only__ This domain's unique ID.</td>
</tr>
<tr>
    <td><CopyableCode code="axfr_ips" /></td>
    <td><code>array</code></td>
    <td>The list of IPs that may perform a zone transfer for this domain. The total combined length of all data within this array cannot exceed 1000 characters.  &gt; 📘 &gt; &gt; This is potentially dangerous, and should be set to an empty list unless you intend to use it.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description for this domain. This is for display purposes only.</td>
</tr>
<tr>
    <td><CopyableCode code="domain" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The domain this domain represents. domain labels cannot be longer than 63 characters and must conform to [RFC1035](https://tools.ietf.org/html/rfc1035). domains must be unique on Linode's platform, including across different Linode accounts; there cannot be two domains representing the same domain. (example: example.org, pattern: <code>^(\*\.)?([a-zA-Z0-9-_]&#123;1,63&#125;\.)+([a-zA-Z]&#123;2,3&#125;\.)?([a-zA-Z]&#123;2,16&#125;|xn--[a-zA-Z0-9]+)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="expire_sec" /></td>
    <td><code>integer</code></td>
    <td>The amount of time in seconds that may pass before this domain is no longer authoritative.  - Valid values are 0, 30, 120, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.  - Any other value is rounded up to the nearest valid value.  - A value of 0 is equivalent to the default value of 1209600.</td>
</tr>
<tr>
    <td><CopyableCode code="group" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The group this domain belongs to.  This is for display purposes only.</td>
</tr>
<tr>
    <td><CopyableCode code="master_ips" /></td>
    <td><code>array</code></td>
    <td>The IP addresses representing the master DNS for this domain. At least one value is required for `type` slave domains. The total combined length of all data within this array cannot exceed 1000 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="refresh_sec" /></td>
    <td><code>integer</code></td>
    <td>The amount of time in seconds before this domain should be refreshed.  - Valid values are 0, 30, 120, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.  - Any other value is rounded up to the nearest valid value.  - A value of 0 is equivalent to the default value of 14400.</td>
</tr>
<tr>
    <td><CopyableCode code="retry_sec" /></td>
    <td><code>integer</code></td>
    <td>The interval, in seconds, at which a failed refresh should be retried.  - Valid values are 0, 30, 120, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.  - Any other value is rounded up to the nearest valid value.  - A value of 0 is equivalent to the default value of 14400.</td>
</tr>
<tr>
    <td><CopyableCode code="soa_email" /></td>
    <td><code>string (email)</code></td>
    <td>Start of Authority email address. This is required for `type` master domains. (example: admin@example.org)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Used to control whether this domain is currently being rendered. (default: active, example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>__Filterable__ An array of tags applied to this object.  Tags are for organizational purposes only.</td>
</tr>
<tr>
    <td><CopyableCode code="ttl_sec" /></td>
    <td><code>integer</code></td>
    <td>"Time to Live" - the amount of time in seconds that this domain's records may be cached by resolvers or other domain servers.  - Valid values are 0, 30, 120, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.  - Any other value is rounded up to the nearest valid value.  - A value of 0 is equivalent to the default value of 86400.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Whether this domain represents the authoritative source of information for the domain it describes (`master`), or whether it is a read-only copy of a master (`slave`). (example: master)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_domains">

A paginated list of Domains you have registered.

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
    <td><a href="#get_domain"><CopyableCode code="get_domain" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>This is a single Domain that you have registered in Linode's DNS Manager. Linode is not a registrar, and in order for this Domain record to work you must own the domain and point your registrar at Linode's nameservers.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_domains"><CopyableCode code="get_domains" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>This is a collection of Domains that you have registered in Linode's DNS Manager.  Linode is not a registrar, and in order for these to work you must own the domains and point your registrar at Linode's nameservers.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_domain"><CopyableCode code="post_domain" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__domain"><code>data__domain</code></a>, <a href="#parameter-data__type"><code>data__type</code></a></td>
    <td></td>
    <td>Adds a new Domain to Linode's DNS Manager. Linode is not a registrar, and you must own the domain before adding it here. Be sure to point your registrar to Linode's nameservers so that the records hosted here are used.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_domain"><CopyableCode code="put_domain" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Update information about a Domain in Linode's DNS Manager.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_domain"><CopyableCode code="delete_domain" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes a Domain from Linode's DNS Manager. The Domain will be removed from Linode's nameservers shortly after this operation completes. This also deletes all associated Domain Records.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_import_domain"><CopyableCode code="post_import_domain" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-domain"><code>domain</code></a>, <a href="#parameter-remote_nameserver"><code>remote_nameserver</code></a></td>
    <td></td>
    <td>Imports a domain zone from a remote nameserver. Your nameserver must allow zone transfers (AXFR) from the following IPs:<br /><br />- 96.126.114.97<br />- 96.126.114.98<br />- 2600:3c00::5e<br />- 2600:3c00::5f<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_clone_domain"><CopyableCode code="post_clone_domain" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-domain"><code>domain</code></a></td>
    <td></td>
    <td>Clones a Domain and all associated DNS records from a Domain that is registered in Linode's DNS manager.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_domain"
    values={[
        { label: 'get_domain', value: 'get_domain' },
        { label: 'get_domains', value: 'get_domains' }
    ]}
>
<TabItem value="get_domain">

This is a single Domain that you have registered in Linode's DNS Manager. Linode is not a registrar, and in order for this Domain record to work you must own the domain and point your registrar at Linode's nameservers.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
axfr_ips,
description,
domain,
expire_sec,
group,
master_ips,
refresh_sec,
retry_sec,
soa_email,
status,
tags,
ttl_sec,
type
FROM linode.domains.domains;
```
</TabItem>
<TabItem value="get_domains">

This is a collection of Domains that you have registered in Linode's DNS Manager.  Linode is not a registrar, and in order for these to work you must own the domains and point your registrar at Linode's nameservers.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.domains.domains
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}';
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_domain"
    values={[
        { label: 'post_domain', value: 'post_domain' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_domain">

Adds a new Domain to Linode's DNS Manager. Linode is not a registrar, and you must own the domain before adding it here. Be sure to point your registrar to Linode's nameservers so that the records hosted here are used.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.domains.domains (
data__axfr_ips,
data__description,
data__domain,
data__expire_sec,
data__group,
data__master_ips,
data__refresh_sec,
data__retry_sec,
data__soa_email,
data__status,
data__tags,
data__ttl_sec,
data__type
)
SELECT 
'{{ axfr_ips }}',
'{{ description }}',
'{{ domain }}' --required,
{{ expire_sec }},
'{{ group }}',
'{{ master_ips }}',
{{ refresh_sec }},
{{ retry_sec }},
'{{ soa_email }}',
'{{ status }}',
'{{ tags }}',
{{ ttl_sec }},
'{{ type }}' --required
RETURNING
id,
axfr_ips,
description,
domain,
expire_sec,
group,
master_ips,
refresh_sec,
retry_sec,
soa_email,
status,
tags,
ttl_sec,
type
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: domains
  props:
    - name: axfr_ips
      value: array
      description: >
        The list of IPs that may perform a zone transfer for this domain. The total combined length of all data within this array cannot exceed 1000 characters.

> 📘
>
> This is potentially dangerous, and should be set to an empty list unless you intend to use it.
        
    - name: description
      value: string
      description: >
        A description for this domain. This is for display purposes only.
        
    - name: domain
      value: string
      description: >
        __Filterable__ The domain this domain represents. domain labels cannot be longer than 63 characters and must conform to [RFC1035](https://tools.ietf.org/html/rfc1035). domains must be unique on Linode's platform, including across different Linode accounts; there cannot be two domains representing the same domain.
        
    - name: expire_sec
      value: integer
      description: >
        The amount of time in seconds that may pass before this domain is no longer authoritative.

- Valid values are 0, 30, 120, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.

- Any other value is rounded up to the nearest valid value.

- A value of 0 is equivalent to the default value of 1209600.
        
      default: 0
    - name: group
      value: string
      description: >
        __Filterable__ The group this domain belongs to.  This is for display purposes only.
        
    - name: master_ips
      value: array
      description: >
        The IP addresses representing the master DNS for this domain. At least one value is required for `type` slave domains. The total combined length of all data within this array cannot exceed 1000 characters.
        
    - name: refresh_sec
      value: integer
      description: >
        The amount of time in seconds before this domain should be refreshed.

- Valid values are 0, 30, 120, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.

- Any other value is rounded up to the nearest valid value.

- A value of 0 is equivalent to the default value of 14400.
        
      default: 0
    - name: retry_sec
      value: integer
      description: >
        The interval, in seconds, at which a failed refresh should be retried.

- Valid values are 0, 30, 120, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.

- Any other value is rounded up to the nearest valid value.

- A value of 0 is equivalent to the default value of 14400.
        
      default: 0
    - name: soa_email
      value: string
      description: >
        Start of Authority email address. This is required for `type` master domains.
        
    - name: status
      value: string
      description: >
        Used to control whether this domain is currently being rendered.
        
      valid_values: ['disabled', 'active']
      default: active
    - name: tags
      value: array
      description: >
        __Filterable__ An array of tags applied to this object.  Tags are for organizational purposes only.
        
    - name: ttl_sec
      value: integer
      description: >
        "Time to Live" - the amount of time in seconds that this domain's records may be cached by resolvers or other domain servers.

- Valid values are 0, 30, 120, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.

- Any other value is rounded up to the nearest valid value.

- A value of 0 is equivalent to the default value of 86400.
        
      default: 0
    - name: type
      value: string
      description: >
        Whether this domain represents the authoritative source of information for the domain it describes (`master`), or whether it is a read-only copy of a master (`slave`).
        
      valid_values: ['master', 'slave']
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_domain"
    values={[
        { label: 'put_domain', value: 'put_domain' }
    ]}
>
<TabItem value="put_domain">

Update information about a Domain in Linode's DNS Manager.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.domains.domains
SET 
data__axfr_ips = '{{ axfr_ips }}',
data__description = '{{ description }}',
data__domain = '{{ domain }}',
data__expire_sec = {{ expire_sec }},
data__group = '{{ group }}',
data__master_ips = '{{ master_ips }}',
data__refresh_sec = {{ refresh_sec }},
data__retry_sec = {{ retry_sec }},
data__soa_email = '{{ soa_email }}',
data__status = '{{ status }}',
data__tags = '{{ tags }}',
data__ttl_sec = {{ ttl_sec }},
data__type = '{{ type }}'
WHERE 

RETURNING
id,
axfr_ips,
description,
domain,
expire_sec,
group,
master_ips,
refresh_sec,
retry_sec,
soa_email,
status,
tags,
ttl_sec,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_domain"
    values={[
        { label: 'delete_domain', value: 'delete_domain' }
    ]}
>
<TabItem value="delete_domain">

Deletes a Domain from Linode's DNS Manager. The Domain will be removed from Linode's nameservers shortly after this operation completes. This also deletes all associated Domain Records.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.domains.domains;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="post_import_domain"
    values={[
        { label: 'post_import_domain', value: 'post_import_domain' },
        { label: 'post_clone_domain', value: 'post_clone_domain' }
    ]}
>
<TabItem value="post_import_domain">

Imports a domain zone from a remote nameserver. Your nameserver must allow zone transfers (AXFR) from the following IPs:<br /><br />- 96.126.114.97<br />- 96.126.114.98<br />- 2600:3c00::5e<br />- 2600:3c00::5f<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.domains.domains.post_import_domain 
@@json=
'{
"domain": "{{ domain }}", 
"remote_nameserver": "{{ remote_nameserver }}"
}';
```
</TabItem>
<TabItem value="post_clone_domain">

Clones a Domain and all associated DNS records from a Domain that is registered in Linode's DNS manager.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.domains.domains.post_clone_domain 
@@json=
'{
"domain": "{{ domain }}"
}';
```
</TabItem>
</Tabs>
