--- 
title: records
hide_title: false
hide_table_of_contents: false
keywords:
  - records
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

Creates, updates, deletes, gets or lists a <code>records</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>records</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.domains.records" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_domain_record"
    values={[
        { label: 'get_domain_record', value: 'get_domain_record' },
        { label: 'get_domain_records', value: 'get_domain_records' }
    ]}
>
<TabItem value="get_domain_record">

A Domain Record object.

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
    <td>__Read-only__ This Record's unique ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The name of this Record. For requests, this property's actual usage and whether it is required depends on the type of record this represents:  `A` and `AAAA`: The hostname or FQDN of the Record.  `NS`: The subdomain, if any, to use with the Domain of the Record. Wildcard NS records (`*`) are not supported.  `MX`: The mail subdomain. For example, `sub` for the address `user@sub.example.com` under the `example.com` Domain.  - The left-most subdomain component may be an asterisk (`*`) to designate a wildcard subdomain. - Other subdomain components must only contain letters, digits, and hyphens, start with a letter, end with a letter or digit, and contain less than 64 characters. - Must be an empty string (`""`) for a Null MX Record.  `CNAME`: The hostname. Must be unique. Required.  `TXT`: The hostname.  `SRV`: Unused. Use the `service` property to set the service name for this record.  `CAA`: The subdomain. Omit or enter an empty string (`""`) to apply to the entire Domain.  `PTR`: See our guide on how to [Configure Your Linode for Reverse DNS (rDNS)](https://www.linode.com/docs/guides/configure-rdns/). (example: test)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When this Domain Record was created. (example: 2018-01-01T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>The port this Record points to. Only valid and required for SRV record requests.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>The priority of the target host for this Record. Lower values are preferred. Only valid for MX and SRV record requests. Required for SRV record requests.  Defaults to `0` for MX record requests. Must be `0` for Null MX records.</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>The protocol this Record's service communicates with. An underscore (`_`) is prepended automatically to the submitted value for this property. Only valid for SRV record requests.</td>
</tr>
<tr>
    <td><CopyableCode code="service" /></td>
    <td><code>string</code></td>
    <td>The name of the service. An underscore (`_`) is prepended and a period (`.`) is appended automatically to the submitted value for this property. Only valid and required for SRV record requests.</td>
</tr>
<tr>
    <td><CopyableCode code="tag" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The tag portion of a CAA record. Only valid and required for CAA record requests.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The target for this Record. For requests, this property's actual usage and whether it is required depends on the type of record this represents:  `A` and `AAAA`: The IP address. Use `[remote_addr]` to submit the IPv4 address of the request. Required.  `NS`: The name server. Must be a valid domain. Required.  `MX`: The mail server. Must be a valid domain unless creating a Null MX Record. Required.  - Must have less than 254 total characters. - The left-most domain component may be an asterisk (`*`) to designate a wildcard domain. - Other domain components must only contain letters, digits, and hyphens, start with a letter, end with a letter or digit, and contain less than 64 characters. - To create a [Null MX Record](https://datatracker.ietf.org/doc/html/rfc7505), first [remove](https://techdocs.akamai.com/linode-api/reference/delete-domain-record) any additional MX records, then create an MX record with empty strings (`""`) for the `target` and `name`. If a Domain has a Null MX record, new MX records cannot be created.  `CNAME`: The alias. Must be a valid domain. Required.  `TXT`: The value. Required.  `SRV`: The target domain or subdomain. If a subdomain is entered, it is automatically used with the Domain. To configure for a different domain, enter a valid FQDN. For example, the value `www` with a Domain for `example.com` results in a target set to `www.example.com`, whereas the value `sample.com` results in a target set to `sample.com`. Required.  `CAA`: The value. For `issue` or `issuewild` tags, the domain of your certificate issuer. For the `iodef` tag, a contact or submission URL (domain, http, https, or mailto). Requirements depend on the tag for this record:    - `issue`: The domain of your certificate issuer. Must include a valid domain. May include additional parameters separated with semicolons (`;`), for example: `www.example.com; foo=bar`   - `issuewild`: The domain of your wildcard certificate issuer. Must be a valid domain and must not start with an asterisk (`*`).   - `iodef`: Must be either (1) a valid domain, (2) a valid domain prepended with `http://` or `https://`, or (3) a valid email address prepended with `mailto:`.  `PTR`: Required. See our guide on how to [Configure Your Linode for Reverse DNS (rDNS)](https://www.linode.com/docs/guides/configure-rdns/).  With the exception of A, AAAA, and CAA records, this field accepts a trailing period. (example: 192.0.2.0)</td>
</tr>
<tr>
    <td><CopyableCode code="ttl_sec" /></td>
    <td><code>integer</code></td>
    <td>"Time to Live" - the amount of time in seconds that this Domain's records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The type of Record this is in the DNS system. For example, A records associate a domain name with an IPv4 address, and AAAA records associate a domain name with an IPv6 address. For more information, see the guides on [DNS Record Types](https://www.linode.com/docs/products/networking/dns-manager/guides/#dns-record-types). (example: A)</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When this Domain Record was last updated. (example: 2018-01-01T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="weight" /></td>
    <td><code>integer</code></td>
    <td>The relative weight of this Record used in the case of identical priority. Higher values are preferred. Only valid and required for SRV record requests.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_domain_records">

A list of Domain Records.

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
    <td><a href="#get_domain_record"><CopyableCode code="get_domain_record" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>View a single Record on this Domain.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_domain_records"><CopyableCode code="get_domain_records" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Returns a paginated list of Records configured on a Domain in Linode's DNS Manager.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_domain_record"><CopyableCode code="post_domain_record" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__type"><code>data__type</code></a></td>
    <td></td>
    <td>Adds a new Domain Record to the zonefile this Domain represents.<br /><br />Each domain can have up to 12,000 active records.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_domain_record"><CopyableCode code="put_domain_record" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Updates a single Record on this Domain.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_domain_record"><CopyableCode code="delete_domain_record" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Deletes a Record on this Domain.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_domain_record"
    values={[
        { label: 'get_domain_record', value: 'get_domain_record' },
        { label: 'get_domain_records', value: 'get_domain_records' }
    ]}
>
<TabItem value="get_domain_record">

View a single Record on this Domain.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
name,
created,
port,
priority,
protocol,
service,
tag,
target,
ttl_sec,
type,
updated,
weight
FROM linode.domains.records
;
```
</TabItem>
<TabItem value="get_domain_records">

Returns a paginated list of Records configured on a Domain in Linode's DNS Manager.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.domains.records
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_domain_record"
    values={[
        { label: 'post_domain_record', value: 'post_domain_record' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_domain_record">

Adds a new Domain Record to the zonefile this Domain represents.<br /><br />Each domain can have up to 12,000 active records.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.domains.records (
data__name,
data__port,
data__priority,
data__protocol,
data__service,
data__tag,
data__target,
data__ttl_sec,
data__type,
data__weight
)
SELECT 
'{{ name }}',
{{ port }},
{{ priority }},
'{{ protocol }}',
'{{ service }}',
'{{ tag }}',
'{{ target }}',
{{ ttl_sec }},
'{{ type }}' /* required */,
{{ weight }}
RETURNING
id,
name,
created,
port,
priority,
protocol,
service,
tag,
target,
ttl_sec,
type,
updated,
weight
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: records
  props:
    - name: name
      value: string
      description: >
        __Filterable__ The name of this Record. For requests, this property's actual usage and whether it is required depends on the type of record this represents:

`A` and `AAAA`: The hostname or FQDN of the Record.

`NS`: The subdomain, if any, to use with the Domain of the Record. Wildcard NS records (`*`) are not supported.

`MX`: The mail subdomain. For example, `sub` for the address `user@sub.example.com` under the `example.com` Domain.

- The left-most subdomain component may be an asterisk (`*`) to designate a wildcard subdomain.
- Other subdomain components must only contain letters, digits, and hyphens, start with a letter, end with a letter or digit, and contain less than 64 characters.
- Must be an empty string (`""`) for a Null MX Record.

`CNAME`: The hostname. Must be unique. Required.

`TXT`: The hostname.

`SRV`: Unused. Use the `service` property to set the service name for this record.

`CAA`: The subdomain. Omit or enter an empty string (`""`) to apply to the entire Domain.

`PTR`: See our guide on how to [Configure Your Linode for Reverse DNS
(rDNS)](https://www.linode.com/docs/guides/configure-rdns/).
        
    - name: port
      value: integer
      description: >
        The port this Record points to. Only valid and required for SRV record requests.
        
    - name: priority
      value: integer
      description: >
        The priority of the target host for this Record. Lower values are preferred. Only valid for MX and SRV record requests. Required for SRV record requests.

Defaults to `0` for MX record requests. Must be `0` for Null MX records.
        
    - name: protocol
      value: string
      description: >
        The protocol this Record's service communicates with. An underscore (`_`) is prepended automatically to the submitted value for this property. Only valid for SRV record requests.
        
    - name: service
      value: string
      description: >
        The name of the service. An underscore (`_`) is prepended and a period (`.`) is appended automatically to the submitted value for this property. Only valid and required for SRV record requests.
        
    - name: tag
      value: string
      description: >
        __Filterable__ The tag portion of a CAA record. Only valid and required for CAA record requests.
        
      valid_values: ['issue', 'issuewild', 'iodef']
    - name: target
      value: string
      description: >
        __Filterable__ The target for this Record. For requests, this property's actual usage and whether it is required depends on the type of record this represents:

`A` and `AAAA`: The IP address. Use `[remote_addr]` to submit the IPv4 address of the request. Required.

`NS`: The name server. Must be a valid domain. Required.

`MX`: The mail server. Must be a valid domain unless creating a Null MX Record. Required.

- Must have less than 254 total characters.
- The left-most domain component may be an asterisk (`*`) to designate a wildcard domain.
- Other domain components must only contain letters, digits, and hyphens, start with a letter, end with a letter or digit, and contain less than 64 characters.
- To create a [Null MX Record](https://datatracker.ietf.org/doc/html/rfc7505), first [remove](https://techdocs.akamai.com/linode-api/reference/delete-domain-record) any additional MX records, then create an MX record with empty strings (`""`) for the `target` and `name`. If a Domain has a Null MX record, new MX records cannot be created.

`CNAME`: The alias. Must be a valid domain. Required.

`TXT`: The value. Required.

`SRV`: The target domain or subdomain. If a subdomain is entered, it is automatically used with the Domain.
To configure for a different domain, enter a valid FQDN. For example, the value `www` with a Domain for
`example.com` results in a target set to `www.example.com`, whereas the value `sample.com` results in a
target set to `sample.com`. Required.

`CAA`: The value. For `issue` or `issuewild` tags, the domain of your certificate issuer. For the `iodef`
tag, a contact or submission URL (domain, http, https, or mailto). Requirements depend on the tag for this record:

  - `issue`: The domain of your certificate issuer. Must include a valid domain. May include additional parameters separated with semicolons (`;`), for example: `www.example.com; foo=bar`
  - `issuewild`: The domain of your wildcard certificate issuer. Must be a valid domain and must not start with an asterisk (`*`).
  - `iodef`: Must be either (1) a valid domain, (2) a valid domain prepended with `http://` or `https://`, or (3) a valid email address prepended with `mailto:`.

`PTR`: Required. See our guide on how to [Configure Your Linode for Reverse DNS
(rDNS)](https://www.linode.com/docs/guides/configure-rdns/).

With the exception of A, AAAA, and CAA records, this field accepts a trailing period.
        
    - name: ttl_sec
      value: integer
      description: >
        "Time to Live" - the amount of time in seconds that this Domain's records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.
        
    - name: type
      value: string
      description: >
        __Filterable__ The type of Record this is in the DNS system. For example, A records associate a domain name with an IPv4 address, and AAAA records associate a domain name with an IPv6 address. For more information, see the guides on [DNS Record Types](https://www.linode.com/docs/products/networking/dns-manager/guides/#dns-record-types).
        
      valid_values: ['A', 'AAAA', 'NS', 'MX', 'CNAME', 'TXT', 'SRV', 'PTR', 'CAA']
    - name: weight
      value: integer
      description: >
        The relative weight of this Record used in the case of identical priority. Higher values are preferred. Only valid and required for SRV record requests.
        
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_domain_record"
    values={[
        { label: 'put_domain_record', value: 'put_domain_record' }
    ]}
>
<TabItem value="put_domain_record">

Updates a single Record on this Domain.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.domains.records
SET 
data__name = '{{ name }}',
data__port = {{ port }},
data__priority = {{ priority }},
data__protocol = '{{ protocol }}',
data__service = '{{ service }}',
data__tag = '{{ tag }}',
data__target = '{{ target }}',
data__ttl_sec = {{ ttl_sec }},
data__weight = {{ weight }}
RETURNING
id,
name,
created,
port,
priority,
protocol,
service,
tag,
target,
ttl_sec,
type,
updated,
weight;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_domain_record"
    values={[
        { label: 'delete_domain_record', value: 'delete_domain_record' }
    ]}
>
<TabItem value="delete_domain_record">

Deletes a Record on this Domain.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.domains.records
;
```
</TabItem>
</Tabs>
