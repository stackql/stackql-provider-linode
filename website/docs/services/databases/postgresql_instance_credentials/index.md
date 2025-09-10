--- 
title: postgresql_instance_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - postgresql_instance_credentials
  - databases
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

Creates, updates, deletes, gets or lists a <code>postgresql_instance_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>postgresql_instance_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.databases.postgresql_instance_credentials" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_databases_postgre_sql_instance_credentials"
    values={[
        { label: 'get_databases_postgre_sql_instance_credentials', value: 'get_databases_postgre_sql_instance_credentials' }
    ]}
>
<TabItem value="get_databases_postgre_sql_instance_credentials">

PostgreSQL Managed Database root username and password.

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
    <td><CopyableCode code="password" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The randomly generated root password for the Managed Database instance. (example: s3cur3P@ssw0rd)</td>
</tr>
<tr>
    <td><CopyableCode code="username" /></td>
    <td><code>string</code></td>
    <td>__Read-only__ The root username for the Managed Database instance. (example: linroot)</td>
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
    <td><a href="#get_databases_postgre_sql_instance_credentials"><CopyableCode code="get_databases_postgre_sql_instance_credentials" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Display the root username and password for an accessible PostgreSQL Managed Database. The database's status needs to be `active`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_databases_postgre_sql_instance_credentials_reset"><CopyableCode code="post_databases_postgre_sql_instance_credentials_reset" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Reset the root password for a PostgreSQL Managed Database. A new root password is randomly generated and accessible with the [Get PostgreSQL Managed Database credentials](https://techdocs.akamai.com/linode-api/reference/get-databases-postgre-sql-instance-credentials) operation.<br /><br />- The database's status needs to be `active`.<br /><br />- Only unrestricted users can access this operation. These users have access regardless of the acting token's OAuth scopes.<br /><br />- It may take several seconds for credentials to reset.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_databases_postgre_sql_instance_credentials"
    values={[
        { label: 'get_databases_postgre_sql_instance_credentials', value: 'get_databases_postgre_sql_instance_credentials' }
    ]}
>
<TabItem value="get_databases_postgre_sql_instance_credentials">

Display the root username and password for an accessible PostgreSQL Managed Database. The database's status needs to be `active`.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
password,
username
FROM linode.databases.postgresql_instance_credentials;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="post_databases_postgre_sql_instance_credentials_reset"
    values={[
        { label: 'post_databases_postgre_sql_instance_credentials_reset', value: 'post_databases_postgre_sql_instance_credentials_reset' }
    ]}
>
<TabItem value="post_databases_postgre_sql_instance_credentials_reset">

Reset the root password for a PostgreSQL Managed Database. A new root password is randomly generated and accessible with the [Get PostgreSQL Managed Database credentials](https://techdocs.akamai.com/linode-api/reference/get-databases-postgre-sql-instance-credentials) operation.<br /><br />- The database's status needs to be `active`.<br /><br />- Only unrestricted users can access this operation. These users have access regardless of the acting token's OAuth scopes.<br /><br />- It may take several seconds for credentials to reset.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.databases.postgresql_instance_credentials.post_databases_postgre_sql_instance_credentials_reset 
;
```
</TabItem>
</Tabs>
