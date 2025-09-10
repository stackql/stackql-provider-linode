--- 
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
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

Creates, updates, deletes, gets or lists an <code>events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.account.events" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_event"
    values={[
        { label: 'get_event', value: 'get_event' },
        { label: 'get_events', value: 'get_events' }
    ]}
>
<TabItem value="get_event">

An Event object.

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
    <td>__Read-only__ The unique ID of this event.</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The action that caused this event. New actions may be added in the future. (example: ticket_create)</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When the system created this event. (example: 2018-01-01T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>number</code></td>
    <td>__Read-only__ The number of seconds that it takes for the event to complete.</td>
</tr>
<tr>
    <td><CopyableCode code="entity" /></td>
    <td><code>object</code></td>
    <td>__Read-only__ Detailed information about the entity that triggered this event.</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>Additional information about the event. This can be a more detailed representation of an event that can help you diagnose non-obvious failures. (example: None)</td>
</tr>
<tr>
    <td><CopyableCode code="percent_complete" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ A percentage estimating the amount of time remaining for an event. Returned as `null` for notification events.</td>
</tr>
<tr>
    <td><CopyableCode code="rate" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The rate of completion of the event. Only some events return a `rate`, such as the `migration` and `resize` events.</td>
</tr>
<tr>
    <td><CopyableCode code="read" /></td>
    <td><code>boolean</code></td>
    <td>__Read-only__ If a user on your account has [marked an event as read](https://techdocs.akamai.com/linode-api/reference/post-event-read).</td>
</tr>
<tr>
    <td><CopyableCode code="secondary_entity" /></td>
    <td><code>object</code></td>
    <td>__Read-only__ Detailed information about the event's secondary entity, if applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="seen" /></td>
    <td><code>boolean</code></td>
    <td>__Read-only__ If a user on your account has [marked an event as seen](https://techdocs.akamai.com/linode-api/reference/post-event-seen).</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The current status of this event.</td>
</tr>
<tr>
    <td><CopyableCode code="time_remaining" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The estimated time remaining until the event completes. This is only returned for some in-progress migration events. Otherwise, `percent_complete` indicates how long until completion.</td>
</tr>
<tr>
    <td><CopyableCode code="username" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The name of the user whose action caused the event. (example: exampleUser)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_events">

Returns a paginated list of Event objects from the last 90 days.

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
    <td>The current [page](https://techdocs.akamai.com/linode-api/reference/pagination).</td>
</tr>
<tr>
    <td><CopyableCode code="pages" /></td>
    <td><code>integer</code></td>
    <td>The total number of [pages](https://techdocs.akamai.com/linode-api/reference/pagination).</td>
</tr>
<tr>
    <td><CopyableCode code="results" /></td>
    <td><code>integer</code></td>
    <td>The total number of results.</td>
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
    <td><a href="#get_event"><CopyableCode code="get_event" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Returns a single event object.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_events"><CopyableCode code="get_events" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Returns a collection of event objects that represent actions you've taken on your account, over the last 90 days. The events returned depend on your user grants.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_event_seen"><CopyableCode code="post_event_seen" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Acknowledge an event by marking it as seen.<br /><br />&gt; 📘<br />&gt;<br />&gt; On June 17, 2025, the "Mark an event as read" operation was sunset. Attempts to call it will return a 404. Use this operation instead.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_event"
    values={[
        { label: 'get_event', value: 'get_event' },
        { label: 'get_events', value: 'get_events' }
    ]}
>
<TabItem value="get_event">

Returns a single event object.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
action,
created,
duration,
entity,
message,
percent_complete,
rate,
read,
secondary_entity,
seen,
status,
time_remaining,
username
FROM linode.account.events;
```
</TabItem>
<TabItem value="get_events">

Returns a collection of event objects that represent actions you've taken on your account, over the last 90 days. The events returned depend on your user grants.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
data,
page,
pages,
results
FROM linode.account.events
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}';
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="post_event_seen"
    values={[
        { label: 'post_event_seen', value: 'post_event_seen' }
    ]}
>
<TabItem value="post_event_seen">

Acknowledge an event by marking it as seen.<br /><br />&gt; 📘<br />&gt;<br />&gt; On June 17, 2025, the "Mark an event as read" operation was sunset. Attempts to call it will return a 404. Use this operation instead.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.account.events.post_event_seen 
;
```
</TabItem>
</Tabs>
