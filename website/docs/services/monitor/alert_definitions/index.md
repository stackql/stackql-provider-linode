--- 
title: alert_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_definitions
  - monitor
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

Creates, updates, deletes, gets or lists an <code>alert_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alert_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.monitor.alert_definitions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_alert_definition"
    values={[
        { label: 'get_alert_definition', value: 'get_alert_definition' },
        { label: 'get_alert_definitions_for_service_type', value: 'get_alert_definitions_for_service_type' },
        { label: 'get_alert_definitions', value: 'get_alert_definitions' }
    ]}
>
<TabItem value="get_alert_definition">

Returns the specified alert definition.

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
    <td>The unique identifier for the alert definition.</td>
</tr>
<tr>
    <td><CopyableCode code="alert_channels" /></td>
    <td><code>array</code></td>
    <td>The alert channels set up for use with this alert. Run the [List alert channels](https://techdocs.akamai.com/linode-api/reference/get-alert-channels) operation to see all of the available channels.</td>
</tr>
<tr>
    <td><CopyableCode code="class" /></td>
    <td><code>string</code></td>
    <td>The plan type for the Managed Database cluster, either `shared` or `dedicated`. This only applies to a `system` alert for a `service_type` of `dbaas` (Managed Databases). For `user` alerts for `dbaas`, this is returned as `null`. (example: dedicated)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the alert definition was created. (example: 2025-03-20 01:42:11)</td>
</tr>
<tr>
    <td><CopyableCode code="created_by" /></td>
    <td><code>string</code></td>
    <td>For a `user` alert definition, this is the user on your account that [created](https://techdocs.akamai.com/linode-api/reference/post-alert-definition-for-service-type) it. For a `system` alert definition, this is returned as `system`. (example: system)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An additional description for the alert definition. (example: Alert for my PostgreSQL database)</td>
</tr>
<tr>
    <td><CopyableCode code="entity_ids" /></td>
    <td><code>array</code></td>
    <td>The `id` for each individual entity from a `service_type`. Get this value by running the list operation for the appropriate entity. For example, if your entity is one of your PostgreSQL databases, run the [List PostgreSQL Managed Databases](https://techdocs.akamai.com/linode-api/reference/get-databases-postgre-sql-instances) operation and store the `id` for the appropriate database from the response.  &gt; 📘 &gt; &gt; The format `type` for an `entity_id` may vary, based on the Akamai Cloud `service_type`. For example, the `dbaas` service returns an integer value for an `id`, that you'd use for the `entity_id`, while other services may return a string for their `id`. With the Alerts operations, all of these formats are recognized as an `entity_id`, when you include them as a `string`.</td>
</tr>
<tr>
    <td><CopyableCode code="has_more_resources" /></td>
    <td><code>boolean</code></td>
    <td>Whether there are additional `entity_ids` associated with the alert for which the user doesn't have at least `read-only` access.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>The name of the alert definition. This is used for display purposes in Akamai Cloud Manager. (example: High Memory Usage Plan Dedicated)</td>
</tr>
<tr>
    <td><CopyableCode code="rule_criteria" /></td>
    <td><code>object</code></td>
    <td>Details for the rules required to trigger the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="service_type" /></td>
    <td><code>string</code></td>
    <td>The identifier for the Akamai Cloud Computing service. Use this value to call out the service in other Monitor operations in the API. Currently, only the Managed Databases (`dbaas`) service is supported. (example: dbaas)</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>integer</code></td>
    <td>The severity of the alert. Supported values include `3` for info, `2` for low, `1` for medium, and `0` for severe.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the alert. This can be either `enabled`, `disabled`, `in progress`, or `failed`. (example: enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="trigger_conditions" /></td>
    <td><code>object</code></td>
    <td>The conditions that need to be met to send a notification for the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of alert. This can be either `user` for an alert specific to the current user, or `system` for one that applies to all users on your account. (example: system)</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the alert definition was last updated. This is the same as `created` if the alert definition hasn't been updated. (example: 2025-03-20 01:42:11)</td>
</tr>
<tr>
    <td><CopyableCode code="updated_by" /></td>
    <td><code>string</code></td>
    <td>For a `user` alert definition, this is the user on your account that last [updated](https://techdocs.akamai.com/linode-api/reference/put-alert-definition) it. For a `system` alert definition, this is returned as `system`. If it hasn't been updated, this value is the same as `created_by`. (example: system)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_alert_definitions_for_service_type">

Returns a paginated list of alert definitions for the specified service type.

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
<TabItem value="get_alert_definitions">

Returns a paginated list of all alert definitions.

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
    <td><a href="#get_alert_definition"><CopyableCode code="get_alert_definition" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>__Beta__ Returns a specific alert definition. Include the appropriate `service_type` and `alert_id` as path parameters.<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation is beta. Call it using the `v4beta` path in its URL.<br />&gt;<br />&gt; - Currently, only the Managed Databases (`dbaas`) service type is supported. __OAuth scopes__.<br /><br />    ```<br />    monitor:read_only<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)<br /><br />-<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)</td>
</tr>
<tr>
    <td><a href="#get_alert_definitions_for_service_type"><CopyableCode code="get_alert_definitions_for_service_type" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>__Beta__ Returns all available alert definitions for a specific service type. Include the appropriate `service_type` as a path parameter.<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation is beta. Call it using the `v4beta` path in its URL.<br />&gt;<br />&gt; - Currently, only the Managed Databases (`dbaas`) service type is supported. __OAuth scopes__.<br /><br />    ```<br />    monitor:read_only<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)<br /><br />-<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)</td>
</tr>
<tr>
    <td><a href="#get_alert_definitions"><CopyableCode code="get_alert_definitions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>__Beta__ Returns all available alert definitions on your account.<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation is beta. Call it using the `v4beta` path in its URL.<br />&gt;<br />&gt; - [Filtering](https://techdocs.akamai.com/linode-api/reference/filtering-and-sorting) is supported for specific objects, labeled as **Filterable**. However, only the `+and` and `+or` operators are supported, and you can't nest filter operators. __OAuth scopes__.<br /><br />    ```<br />    monitor:read_only<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)<br /><br />-<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)</td>
</tr>
<tr>
    <td><a href="#post_alert_definition_for_service_type"><CopyableCode code="post_alert_definition_for_service_type" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__label"><code>data__label</code></a>, <a href="#parameter-data__severity"><code>data__severity</code></a>, <a href="#parameter-data__rule_criteria"><code>data__rule_criteria</code></a>, <a href="#parameter-data__trigger_conditions"><code>data__trigger_conditions</code></a>, <a href="#parameter-data__channel_ids"><code>data__channel_ids</code></a></td>
    <td></td>
    <td>__Beta__ Create a new alert definition for a specific service type. Include the appropriate `service_type` as a path parameter. These are referred to as `user` alerts. You need `read_only` access to the [scope](https://techdocs.akamai.com/linode-api/reference/oauth-reference) for the selected `service_type`.<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation is beta. Call it using the `v4beta` path in its URL.<br />&gt;<br />&gt; - Currently, only the Managed Databases (`dbaas`) service type is supported. __OAuth scopes__.<br /><br />    ```<br />    monitor:read_write<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)<br /><br />-<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)</td>
</tr>
<tr>
    <td><a href="#put_alert_definition"><CopyableCode code="put_alert_definition" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>__Beta__ Update an existing alert definition. Include the appropriate `service_type` and `alert_id` as path parameters. You need `read_only` access to the [scope](https://techdocs.akamai.com/linode-api/reference/oauth-reference) for the selected `service_type`. Only include the objects in the request that you want to update. Leave any object out of the request to leave it set as is.<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation is beta. Call it using the `v4beta` path in its URL.<br />&gt;<br />&gt; - Currently, only the Managed Databases (`dbaas`) service type is supported.<br /><br />**User alert definitions**<br /><br />When updating an alert definition you've [created](https://techdocs.akamai.com/linode-api/reference/post-alert-definition-for-service-type), you can change the `status` to `enabled` or `disabled`. You can also modify the `label`, `description`, `severity`, `entity_ids`, `rule_criteria`, `trigger_conditions`, and `channel_ids` objects. If updating the `entity_ids`, `rule_criteria`, or `channel_ids` list objects, these points apply:<br /><br />- If you want to keep an existing item, you need to include it in the list.<br /><br />- If you want to remove an existing item, leave it out of the list.<br /><br />- To add a new item, include it in the list.<br /><br />- You can't pass an empty list to remove all items. This doesn't apply to the `entity_ids` or `dimension_filters` (in `rule_criteria`) list objects, because they are optional, while all other list objects are required.<br /><br />**System alert definitions**<br /><br />These are the default alert definitions offered by Akamai. You can only edit the `entity_ids` list object for these alerts. All of the points above regarding editing a list object apply here, too. __OAuth scopes__.<br /><br />    ```<br />    monitor:read_write<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)<br /><br />-<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)</td>
</tr>
<tr>
    <td><a href="#delete_alert_definition"><CopyableCode code="delete_alert_definition" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>__Beta__ Delete a specific alert definition on your account. Include the appropriate `service_type` and `alert_id` as path parameters.<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation is beta. Call it using the `v4beta` path in its URL.<br />&gt;<br />&gt; - You need `read_only` access to the [scope](https://techdocs.akamai.com/linode-api/reference/get-started#oauth-reference) for the target `service_type`.<br />&gt;<br />&gt; - An [alert definition](https://techdocs.akamai.com/linode-api/reference/get-alert-definitions) with a `type` of `system` can't be deleted.<br />&gt;<br />&gt; - Currently, only the Managed Databases (`dbaas`) service type is supported.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_alert_definition"
    values={[
        { label: 'get_alert_definition', value: 'get_alert_definition' },
        { label: 'get_alert_definitions_for_service_type', value: 'get_alert_definitions_for_service_type' },
        { label: 'get_alert_definitions', value: 'get_alert_definitions' }
    ]}
>
<TabItem value="get_alert_definition">

__Beta__ Returns a specific alert definition. Include the appropriate `service_type` and `alert_id` as path parameters.<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation is beta. Call it using the `v4beta` path in its URL.<br />&gt;<br />&gt; - Currently, only the Managed Databases (`dbaas`) service type is supported. __OAuth scopes__.<br /><br />    ```<br />    monitor:read_only<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)<br /><br />-<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)

```sql
SELECT
id,
alert_channels,
class,
created,
created_by,
description,
entity_ids,
has_more_resources,
label,
rule_criteria,
service_type,
severity,
status,
trigger_conditions,
type,
updated,
updated_by
FROM linode.monitor.alert_definitions
;
```
</TabItem>
<TabItem value="get_alert_definitions_for_service_type">

__Beta__ Returns all available alert definitions for a specific service type. Include the appropriate `service_type` as a path parameter.<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation is beta. Call it using the `v4beta` path in its URL.<br />&gt;<br />&gt; - Currently, only the Managed Databases (`dbaas`) service type is supported. __OAuth scopes__.<br /><br />    ```<br />    monitor:read_only<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)<br /><br />-<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)

```sql
SELECT
data,
page,
pages,
results
FROM linode.monitor.alert_definitions
;
```
</TabItem>
<TabItem value="get_alert_definitions">

__Beta__ Returns all available alert definitions on your account.<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation is beta. Call it using the `v4beta` path in its URL.<br />&gt;<br />&gt; - [Filtering](https://techdocs.akamai.com/linode-api/reference/filtering-and-sorting) is supported for specific objects, labeled as **Filterable**. However, only the `+and` and `+or` operators are supported, and you can't nest filter operators. __OAuth scopes__.<br /><br />    ```<br />    monitor:read_only<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)<br /><br />-<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)

```sql
SELECT
data,
page,
pages,
results
FROM linode.monitor.alert_definitions
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_alert_definition_for_service_type"
    values={[
        { label: 'post_alert_definition_for_service_type', value: 'post_alert_definition_for_service_type' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_alert_definition_for_service_type">

__Beta__ Create a new alert definition for a specific service type. Include the appropriate `service_type` as a path parameter. These are referred to as `user` alerts. You need `read_only` access to the [scope](https://techdocs.akamai.com/linode-api/reference/oauth-reference) for the selected `service_type`.<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation is beta. Call it using the `v4beta` path in its URL.<br />&gt;<br />&gt; - Currently, only the Managed Databases (`dbaas`) service type is supported. __OAuth scopes__.<br /><br />    ```<br />    monitor:read_write<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)<br /><br />-<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)

```sql
INSERT INTO linode.monitor.alert_definitions (
data__channel_ids,
data__description,
data__entity_ids,
data__label,
data__rule_criteria,
data__severity,
data__trigger_conditions
)
SELECT 
'{{ channel_ids }}' /* required */,
'{{ description }}',
'{{ entity_ids }}',
'{{ label }}' /* required */,
'{{ rule_criteria }}' /* required */,
{{ severity }} /* required */,
'{{ trigger_conditions }}' /* required */
RETURNING
id,
alert_channels,
class,
created,
created_by,
description,
entity_ids,
has_more_resources,
label,
rule_criteria,
service_type,
severity,
status,
trigger_conditions,
type,
updated,
updated_by
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: alert_definitions
  props:
    - name: channel_ids
      value: array
      description: >
        The identifiers for the alert channels to use for the alert. Run the [List alert channels](https://techdocs.akamai.com/linode-api/reference/get-alert-channels) operation and store the `id` for the applicable channels.
        
    - name: description
      value: string
      description: >
        An additional description for the alert definition.
        
    - name: entity_ids
      value: array
      description: >
        The `id` for each individual entity from a `service_type`. Get this value by running the list operation for the appropriate entity. For example, if your entity is one of your PostgreSQL databases, run the [List PostgreSQL Managed Databases](https://techdocs.akamai.com/linode-api/reference/get-databases-postgre-sql-instances) operation and store the `id` for the appropriate database from the response.

> 📘
>
> - You need `read_only` access to the [scope](https://techdocs.akamai.com/linode-api/reference/get-started#oauth-reference) for the `service_type` for each of the `entity_ids`.
>
> - The format `type` for an `entity_id` may vary, based on the Akamai Cloud `service_type`. For example, the `dbaas` service returns an integer value for an `id`, that you'd use for the `entity_id`, while other services may return a string for their `id`. With the Alerts operations, all of these formats are recognized as an `entity_id`, when you include them as a `string`.
        
    - name: label
      value: string
      description: >
        The name of the alert definition. This is used for display purposes in Akamai Cloud Manager.
        
    - name: rule_criteria
      value: object
      description: >
        Details for the rules required to trigger the alert.
        
    - name: severity
      value: integer
      description: >
        The severity of the alert. Supported values include `3` for info, `2` for low, `1` for medium, and `0` for severe.
        
      valid_values: ['0', '1', '2', '3']
    - name: trigger_conditions
      value: object
      description: >
        The conditions that need to be met to send a notification for the alert.
        
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_alert_definition"
    values={[
        { label: 'put_alert_definition', value: 'put_alert_definition' }
    ]}
>
<TabItem value="put_alert_definition">

__Beta__ Update an existing alert definition. Include the appropriate `service_type` and `alert_id` as path parameters. You need `read_only` access to the [scope](https://techdocs.akamai.com/linode-api/reference/oauth-reference) for the selected `service_type`. Only include the objects in the request that you want to update. Leave any object out of the request to leave it set as is.<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation is beta. Call it using the `v4beta` path in its URL.<br />&gt;<br />&gt; - Currently, only the Managed Databases (`dbaas`) service type is supported.<br /><br />**User alert definitions**<br /><br />When updating an alert definition you've [created](https://techdocs.akamai.com/linode-api/reference/post-alert-definition-for-service-type), you can change the `status` to `enabled` or `disabled`. You can also modify the `label`, `description`, `severity`, `entity_ids`, `rule_criteria`, `trigger_conditions`, and `channel_ids` objects. If updating the `entity_ids`, `rule_criteria`, or `channel_ids` list objects, these points apply:<br /><br />- If you want to keep an existing item, you need to include it in the list.<br /><br />- If you want to remove an existing item, leave it out of the list.<br /><br />- To add a new item, include it in the list.<br /><br />- You can't pass an empty list to remove all items. This doesn't apply to the `entity_ids` or `dimension_filters` (in `rule_criteria`) list objects, because they are optional, while all other list objects are required.<br /><br />**System alert definitions**<br /><br />These are the default alert definitions offered by Akamai. You can only edit the `entity_ids` list object for these alerts. All of the points above regarding editing a list object apply here, too. __OAuth scopes__.<br /><br />    ```<br />    monitor:read_write<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)<br /><br />-<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)

```sql
REPLACE linode.monitor.alert_definitions
SET 
data__channel_ids = '{{ channel_ids }}',
data__description = '{{ description }}',
data__entity_ids = '{{ entity_ids }}',
data__label = '{{ label }}',
data__rule_criteria = '{{ rule_criteria }}',
data__severity = {{ severity }},
data__status = '{{ status }}',
data__trigger_conditions = '{{ trigger_conditions }}'
RETURNING
id,
alert_channels,
class,
created,
created_by,
description,
entity_ids,
has_more_resources,
label,
rule_criteria,
service_type,
severity,
status,
trigger_conditions,
type,
updated,
updated_by;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_alert_definition"
    values={[
        { label: 'delete_alert_definition', value: 'delete_alert_definition' }
    ]}
>
<TabItem value="delete_alert_definition">

__Beta__ Delete a specific alert definition on your account. Include the appropriate `service_type` and `alert_id` as path parameters.<br /><br />&gt; 📘<br />&gt;<br />&gt; - This operation is beta. Call it using the `v4beta` path in its URL.<br />&gt;<br />&gt; - You need `read_only` access to the [scope](https://techdocs.akamai.com/linode-api/reference/get-started#oauth-reference) for the target `service_type`.<br />&gt;<br />&gt; - An [alert definition](https://techdocs.akamai.com/linode-api/reference/get-alert-definitions) with a `type` of `system` can't be deleted.<br />&gt;<br />&gt; - Currently, only the Managed Databases (`dbaas`) service type is supported.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.monitor.alert_definitions
;
```
</TabItem>
</Tabs>
