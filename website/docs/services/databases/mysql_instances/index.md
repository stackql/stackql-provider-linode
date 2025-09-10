--- 
title: mysql_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - mysql_instances
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

Creates, updates, deletes, gets or lists a <code>mysql_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mysql_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.databases.mysql_instances" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_databases_mysql_instance"
    values={[
        { label: 'get_databases_mysql_instance', value: 'get_databases_mysql_instance' },
        { label: 'get_databases_mysql_instances', value: 'get_databases_mysql_instances' }
    ]}
>
<TabItem value="get_databases_mysql_instance">

Returns information for a single MySQL Managed Database.

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
    <td>__Read-only__ A unique ID that can be used to identify and reference the Managed Database.</td>
</tr>
<tr>
    <td><CopyableCode code="allow_list" /></td>
    <td><code>array</code></td>
    <td>Controls access to the Managed Database.  - Individually included IP addresses or CIDR ranges can access the Managed Database while all other sources are blocked.  - A standalone value of `0.0.0.0/0` allows all IP addresses access to the Managed Database.  - An empty array (`[]`) blocks all public and private connections to the Managed Database.</td>
</tr>
<tr>
    <td><CopyableCode code="cluster_size" /></td>
    <td><code>integer</code></td>
    <td>The number of Linode instance nodes deployed to the Managed Database.   - Choose `3` nodes to create a high availability cluster that consists of one primary node and two replica nodes.  - A `2` node cluster is only available with a dedicated plan. It consists of one primary node and one replica node.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When this Managed Database was created. (example: 2022-01-01T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="encrypted" /></td>
    <td><code>boolean</code></td>
    <td>__Read-only__ Whether the Managed Databases is encrypted. Currently required to be `true`.</td>
</tr>
<tr>
    <td><CopyableCode code="engine" /></td>
    <td><code>string</code></td>
    <td>__Filterable__, __Read-only__ The Managed Database engine type. (example: mysql)</td>
</tr>
<tr>
    <td><CopyableCode code="engine_config" /></td>
    <td><code>object</code></td>
    <td>Advanced parameters you can apply to a MySQL Managed Database, via our partner [Aiven's specification](https://aiven.io/docs/products/mysql/reference/advanced-params). Only include the objects for parameters you want to set in your database. Omit objects for parameters you don't want to define or change.  &gt; 📘 &gt; &gt; Aiven may offer additional parameters in their specification. Currently, only those listed here are supported for use in a MySQL Managed Database. You can also run the [List MySQL Managed Database advanced parameters](https://techdocs.akamai.com/linode-api/reference/get-databases-mysql-config) operation to see an up-to-date list.</td>
</tr>
<tr>
    <td><CopyableCode code="fork" /></td>
    <td><code>object</code></td>
    <td>Details on the database that was the target of the fork. This only exists if the database was restored by creating a fork from another [MySQL](https://techdocs.akamai.com/linode-api/reference/post-databases-mysql-instances) or [PostgreSQL](https://techdocs.akamai.com/linode-api/reference/post-databases-postgre-sql-instances) database.</td>
</tr>
<tr>
    <td><CopyableCode code="hosts" /></td>
    <td><code>object</code></td>
    <td>__Read-only__ The primary and secondary hosts for the Managed Database. These are assigned after provisioning is complete.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ A unique, user-defined string referring to the Managed Database. This string needs to be unique per Managed Database engine type. (example: example-db)</td>
</tr>
<tr>
    <td><CopyableCode code="members" /></td>
    <td><code>object</code></td>
    <td>__Read-only__ A mapping between IP addresses and strings designating them as `primary` or `failover`.</td>
</tr>
<tr>
    <td><CopyableCode code="oldest_restore_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ The oldest time to which a database can be restored. (example: 2024-10-03 20:48:05)</td>
</tr>
<tr>
    <td><CopyableCode code="platform" /></td>
    <td><code>string</code></td>
    <td>__Filterable__, __Read-only__ The back-end platform for relational databases used by the service. (example: rdbms-default)</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The access port for this Managed Database.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The [Region](https://techdocs.akamai.com/linode-api/reference/get-regions) ID for the Managed Database. (example: us-east)</td>
</tr>
<tr>
    <td><CopyableCode code="ssl_connection" /></td>
    <td><code>boolean</code></td>
    <td>Currently required to be `true`. Whether to require SSL credentials to establish a connection to the Managed Database. Run the [Get managed MySQL database credentials](https://techdocs.akamai.com/linode-api/reference/get-databases-mysql-instance-credentials) operation for access information.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>__Filterable__, __Read-only__ The operating status of the Managed Database. (example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="total_disk_size_gb" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The total disk size of the database, in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The Linode Instance type used by the Managed Database for its nodes. (example: g6-dedicated-2)</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When this Managed Database was last updated. (example: 2022-01-01T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="updates" /></td>
    <td><code>object</code></td>
    <td>Configuration settings for automated patch update maintenance for the Managed Database.</td>
</tr>
<tr>
    <td><CopyableCode code="used_disk_size_gb" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The amount of space currently in use in the database, in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The Managed Database engine version. (example: 8.0.26)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_databases_mysql_instances">

Returns a paginated list of all accessible MySQL Managed Databases on your account.

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
    <td>__Read-only__ A unique ID that can be used to identify and reference the Managed Database.</td>
</tr>
<tr>
    <td><CopyableCode code="allow_list" /></td>
    <td><code>array</code></td>
    <td>Controls access to the Managed Database.  - Individually included IP addresses or CIDR ranges can access the Managed Database while all other sources are blocked.  - A standalone value of `0.0.0.0/0` allows all IP addresses access to the Managed Database.  - An empty array (`[]`) blocks all public and private connections to the Managed Database.</td>
</tr>
<tr>
    <td><CopyableCode code="cluster_size" /></td>
    <td><code>integer</code></td>
    <td>The number of Linode instance nodes deployed to the Managed Database.   - Choose `3` nodes to create a high availability cluster that consists of one primary node and two replica nodes.  - A `2` node cluster is only available with a dedicated plan. It consists of one primary node and one replica node.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When this Managed Database was created. (example: 2022-01-01T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="encrypted" /></td>
    <td><code>boolean</code></td>
    <td>__Read-only__ Whether the Managed Databases is encrypted. Currently required to be `true`.</td>
</tr>
<tr>
    <td><CopyableCode code="engine" /></td>
    <td><code>string</code></td>
    <td>__Filterable__, __Read-only__ The Managed Database engine type. (example: mysql)</td>
</tr>
<tr>
    <td><CopyableCode code="engine_config" /></td>
    <td><code>object</code></td>
    <td>Advanced parameters you can apply to a MySQL Managed Database, via our partner [Aiven's specification](https://aiven.io/docs/products/mysql/reference/advanced-params). Only include the objects for parameters you want to set in your database. Omit objects for parameters you don't want to define or change.  &gt; 📘 &gt; &gt; Aiven may offer additional parameters in their specification. Currently, only those listed here are supported for use in a MySQL Managed Database. You can also run the [List MySQL Managed Database advanced parameters](https://techdocs.akamai.com/linode-api/reference/get-databases-mysql-config) operation to see an up-to-date list.</td>
</tr>
<tr>
    <td><CopyableCode code="fork" /></td>
    <td><code>object</code></td>
    <td>Details on the database that was the target of the fork. This only exists if the database was restored by creating a fork from another [MySQL](https://techdocs.akamai.com/linode-api/reference/post-databases-mysql-instances) or [PostgreSQL](https://techdocs.akamai.com/linode-api/reference/post-databases-postgre-sql-instances) database.</td>
</tr>
<tr>
    <td><CopyableCode code="hosts" /></td>
    <td><code>object</code></td>
    <td>__Read-only__ The primary and secondary hosts for the Managed Database. These are assigned after provisioning is complete.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ A unique, user-defined string referring to the Managed Database. This string needs to be unique per Managed Database engine type. (example: example-db)</td>
</tr>
<tr>
    <td><CopyableCode code="members" /></td>
    <td><code>object</code></td>
    <td>__Read-only__ A mapping between IP addresses and strings designating them as `primary` or `failover`.</td>
</tr>
<tr>
    <td><CopyableCode code="oldest_restore_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ The oldest time to which a database can be restored. (example: 2024-10-03 20:48:05)</td>
</tr>
<tr>
    <td><CopyableCode code="platform" /></td>
    <td><code>string</code></td>
    <td>__Filterable__, __Read-only__ The back-end platform for relational databases used by the service. (example: rdbms-default)</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The access port for this Managed Database.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The [Region](https://techdocs.akamai.com/linode-api/reference/get-regions) ID for the Managed Database. (example: us-east)</td>
</tr>
<tr>
    <td><CopyableCode code="ssl_connection" /></td>
    <td><code>boolean</code></td>
    <td>Currently required to be `true`. Whether to require SSL credentials to establish a connection to the Managed Database. Run the [Get managed MySQL database credentials](https://techdocs.akamai.com/linode-api/reference/get-databases-mysql-instance-credentials) operation for access information.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>__Filterable__, __Read-only__ The operating status of the Managed Database. (example: active)</td>
</tr>
<tr>
    <td><CopyableCode code="total_disk_size_gb" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The total disk size of the database, in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The Linode Instance type used by the Managed Database for its nodes. (example: g6-dedicated-2)</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>__Read-only__ When this Managed Database was last updated. (example: 2022-01-01T00:01:01)</td>
</tr>
<tr>
    <td><CopyableCode code="updates" /></td>
    <td><code>object</code></td>
    <td>Configuration settings for automated patch update maintenance for the Managed Database.</td>
</tr>
<tr>
    <td><CopyableCode code="used_disk_size_gb" /></td>
    <td><code>integer</code></td>
    <td>__Read-only__ The amount of space currently in use in the database, in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>__Filterable__ The Managed Database engine version. (example: 8.0.26)</td>
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
    <td><a href="#get_databases_mysql_instance"><CopyableCode code="get_databases_mysql_instance" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Display information for a single, accessible MySQL Managed Database.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#get_databases_mysql_instances"><CopyableCode code="get_databases_mysql_instances" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-page"><code>page</code></a>, <a href="#parameter-page_size"><code>page_size</code></a></td>
    <td>Display all accessible MySQL Managed Databases.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_databases_mysql_instances"><CopyableCode code="post_databases_mysql_instances" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-data__label"><code>data__label</code></a>, <a href="#parameter-data__type"><code>data__type</code></a>, <a href="#parameter-data__engine"><code>data__engine</code></a>, <a href="#parameter-data__region"><code>data__region</code></a></td>
    <td></td>
    <td>**Provision a MySQL Managed Database**<br /><br />Use this operation to create a new MySQL Managed Database.<br /><br />- Restricted users need the `add_databases` [user grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants).<br /><br />- New instances can take 10 to 15 minutes to deploy.<br /><br />- When you create a new MySQL Managed Database, our partner [Aiven](https://aiven.io/docs/platform/concepts/cloud-security#data-encryption) automatically enables disk encryption on each cluster.<br /><br />- All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.<br /><br />- All Managed Databases include automatic updates, which apply security patches to the underlying operating system of the MySQL Managed Database. Configure the maintenance window for these updates with the [Update a managed MySQL database](https://techdocs.akamai.com/linode-api/reference/put-databases-mysql-instance) operation.<br /><br />- If your database cluster is configured with a single node, downtime occurs during maintenance updates. You should adjust the window to match a time that's the least disruptive to your application and users. Also consider upgrading to a [high availability](https://techdocs.akamai.com/cloud-computing/docs/aiven-database-clusters#high-availability) plan to avoid any maintenance downtime.<br /><br />- Major upgrades are optional until the service reaches end of service, and can be done in place.<br /><br />- A successful request triggers a `database_create` [event](https://techdocs.akamai.com/linode-api/reference/get-events).<br /><br />**Restore a MySQL Managed Database**<br /><br />Include the `fork` object in the request to target a backed-up database. Your user needs `read_write` access to the target database and its status can be `active`, `degraded`, or `failed`.<br /><br />&gt; 📘<br />&gt;<br />&gt; Restoring from a backup creates a second running cluster, which incurs billing. Delete the first cluster after the restore is complete, to avoid this billing. __CLI for create operation__.<br /><br />    ```<br />    linode-cli databases mysql-create \<br />  --label example-db1 \<br />  --region us-east \<br />  --type g6-dedicated-2 \<br />  --cluster_size 3 \<br />  --engine mysql/8.0.26 \<br />  --engine_config.binlog_retention_period 60 \<br />  --engine_config.mysql.connect_timeout 10 \<br />  --engine_config.mysql.default_time_zone +03:00 \<br />  --ssl_connection true \<br />  --allow_list 203.0.113.1 \<br />  --allow_list 192.0.1.0/24<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#post_databases_mysql_instance_patch"><CopyableCode code="post_databases_mysql_instance_patch" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td></td>
    <td></td>
    <td>Apply security patches and updates to the underlying operating system of the MySQL Managed Database. This function runs during regular maintenance windows, which you can configure with the [Update a managed MySQL database](https://techdocs.akamai.com/linode-api/reference/put-databases-mysql-instance) operation.<br /><br />- The user needs `read_write` [user grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) access to the database.<br /><br />- The database's status meeds to be `active`.<br /><br />- If your database cluster is configured with a single node, downtime occurs during maintenance updates. Consider upgrading to a [high availability](https://techdocs.akamai.com/cloud-computing/docs/aiven-database-clusters#high-availability) plan to avoid any maintenance downtime.<br /><br />- Major upgrades are optional until the service reaches end of service, and can be done in place.<br /><br />- A successful request triggers a `database_upgrade` [event](https://techdocs.akamai.com/linode-api/reference/get-events).<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#put_databases_mysql_instance"><CopyableCode code="put_databases_mysql_instance" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td></td>
    <td></td>
    <td>Make changes to an existing MySQL Managed Database.<br /><br />- The user needs `read_write` [user grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) access to the database.<br /><br />- The database's status needs to be `active`.<br /><br />- New values set in the `allow_list` overwrite existing values. To keep existing values, run the [List MySQL Managed Databases](https://techdocs.akamai.com/linode-api/reference/get-databases-mysql-instances) operation, store the `allow_list` addresses from the response, and include them with any new addresses in this operation.<br /><br />- Updates to your `allow_list` may take a short time to complete, making this operation inappropriate for rapid successive updates.<br /><br />- Also allows resizing the database cluster to a larger one. Clusters can't be resized to smaller plans.<br /><br />- All Managed Databases include automatic updates, which apply security patches to the underlying operating system of the Managed MySQL Database. Use the `updates` object in this operation to modify the maintenance window for these updates.<br /><br />- If your database cluster is configured with a single node, downtime occurs during maintenance updates. Use the `updates` object to adjust the window to match a time that's the least disruptive to your application and users. Also consider upgrading to a [high availability](https://techdocs.akamai.com/cloud-computing/docs/aiven-database-clusters#high-availability) plan to avoid any maintenance downtime.<br /><br />- Major upgrades are optional until the service reaches end of service, and can be done in place.<br /><br />- You can't update `engine_config` advanced parameter settings for a suspended database. You'll need to [resume](https://techdocs.akamai.com/linode-api/reference/resume-databases-mysql-instance) it first.<br /><br />- A successful request triggers a `database_update` [event](https://techdocs.akamai.com/linode-api/reference/get-events).<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#delete_databases_mysql_instance"><CopyableCode code="delete_databases_mysql_instance" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td></td>
    <td>Remove a MySQL Managed Database from your account.<br /><br />- The user needs `read_write` [user grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) access to the database.<br /><br />- The database's status can be `active`, `failed`, or `degraded`.<br /><br />- Only unrestricted users can access this operation. They have access regardless of the acting token's OAuth scopes.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#resume_databases_mysql_instance"><CopyableCode code="resume_databases_mysql_instance" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Resume a suspended MySQL Managed Database from your account. This resumes billing for the cluster.<br /><br />- The user needs `read_write` [user grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) access to the database.<br /><br />- The database's status needs to be `suspended`.<br /><br />- A successful request triggers a `database_resume` [event](https://techdocs.akamai.com/linode-api/reference/get-events). __OAuth scopes__.<br /><br />    ```<br />    databases:read_write<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
</tr>
<tr>
    <td><a href="#suspend_databases_mysql_instance"><CopyableCode code="suspend_databases_mysql_instance" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Suspend a MySQL Managed Database from your account, releasing idle resources and keeping only necessary data. All service data is lost if there are no backups available. This halts billing for the cluster.<br /><br />- The user needs `read_write` [user grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) access to the database.<br /><br />- The database's status needs to be `active`.<br /><br />- Akamai deletes suspended clusters after 180 days.<br /><br />- A successful request triggers a `database_update` [event](https://techdocs.akamai.com/linode-api/reference/get-events). __OAuth scopes__.<br /><br />    ```<br />    databases:read_write<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)</td>
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
    defaultValue="get_databases_mysql_instance"
    values={[
        { label: 'get_databases_mysql_instance', value: 'get_databases_mysql_instance' },
        { label: 'get_databases_mysql_instances', value: 'get_databases_mysql_instances' }
    ]}
>
<TabItem value="get_databases_mysql_instance">

Display information for a single, accessible MySQL Managed Database.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
allow_list,
cluster_size,
created,
encrypted,
engine,
engine_config,
fork,
hosts,
label,
members,
oldest_restore_time,
platform,
port,
region,
ssl_connection,
status,
total_disk_size_gb,
type,
updated,
updates,
used_disk_size_gb,
version
FROM linode.databases.mysql_instances;
```
</TabItem>
<TabItem value="get_databases_mysql_instances">

Display all accessible MySQL Managed Databases.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
SELECT
id,
allow_list,
cluster_size,
created,
encrypted,
engine,
engine_config,
fork,
hosts,
label,
members,
oldest_restore_time,
platform,
port,
region,
ssl_connection,
status,
total_disk_size_gb,
type,
updated,
updates,
used_disk_size_gb,
version
FROM linode.databases.mysql_instances
WHERE page = '{{ page }}'
AND page_size = '{{ page_size }}';
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="post_databases_mysql_instances"
    values={[
        { label: 'post_databases_mysql_instances', value: 'post_databases_mysql_instances' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="post_databases_mysql_instances">

**Provision a MySQL Managed Database**<br /><br />Use this operation to create a new MySQL Managed Database.<br /><br />- Restricted users need the `add_databases` [user grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants).<br /><br />- New instances can take 10 to 15 minutes to deploy.<br /><br />- When you create a new MySQL Managed Database, our partner [Aiven](https://aiven.io/docs/platform/concepts/cloud-security#data-encryption) automatically enables disk encryption on each cluster.<br /><br />- All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.<br /><br />- All Managed Databases include automatic updates, which apply security patches to the underlying operating system of the MySQL Managed Database. Configure the maintenance window for these updates with the [Update a managed MySQL database](https://techdocs.akamai.com/linode-api/reference/put-databases-mysql-instance) operation.<br /><br />- If your database cluster is configured with a single node, downtime occurs during maintenance updates. You should adjust the window to match a time that's the least disruptive to your application and users. Also consider upgrading to a [high availability](https://techdocs.akamai.com/cloud-computing/docs/aiven-database-clusters#high-availability) plan to avoid any maintenance downtime.<br /><br />- Major upgrades are optional until the service reaches end of service, and can be done in place.<br /><br />- A successful request triggers a `database_create` [event](https://techdocs.akamai.com/linode-api/reference/get-events).<br /><br />**Restore a MySQL Managed Database**<br /><br />Include the `fork` object in the request to target a backed-up database. Your user needs `read_write` access to the target database and its status can be `active`, `degraded`, or `failed`.<br /><br />&gt; 📘<br />&gt;<br />&gt; Restoring from a backup creates a second running cluster, which incurs billing. Delete the first cluster after the restore is complete, to avoid this billing. __CLI for create operation__.<br /><br />    ```<br />    linode-cli databases mysql-create \<br />  --label example-db1 \<br />  --region us-east \<br />  --type g6-dedicated-2 \<br />  --cluster_size 3 \<br />  --engine mysql/8.0.26 \<br />  --engine_config.binlog_retention_period 60 \<br />  --engine_config.mysql.connect_timeout 10 \<br />  --engine_config.mysql.default_time_zone +03:00 \<br />  --ssl_connection true \<br />  --allow_list 203.0.113.1 \<br />  --allow_list 192.0.1.0/24<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
INSERT INTO linode.databases.mysql_instances (
data__allow_list,
data__cluster_size,
data__engine,
data__engine_config,
data__fork,
data__label,
data__region,
data__ssl_connection,
data__type
)
SELECT 
'{{ allow_list }}',
{{ cluster_size }},
'{{ engine }}' --required,
'{{ engine_config }}',
'{{ fork }}',
'{{ label }}' --required,
'{{ region }}' --required,
{{ ssl_connection }},
'{{ type }}' --required
RETURNING
id,
allow_list,
cluster_size,
created,
encrypted,
engine,
engine_config,
fork,
hosts,
label,
members,
oldest_restore_time,
platform,
port,
region,
ssl_connection,
status,
total_disk_size_gb,
type,
updated,
updates,
used_disk_size_gb,
version
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: mysql_instances
  props:
    - name: allow_list
      value: array
      description: >
        Controls access to the Managed Database.

- Individually included IP addresses or CIDR ranges can access the Managed Database while all other sources are blocked.

- A standalone value of `0.0.0.0/0` allows all IP addresses access to the Managed Database.

- An empty array (`[]`) blocks all public and private connections to the Managed Database.
        
    - name: cluster_size
      value: integer
      description: >
        The number of Linode instance nodes deployed to the Managed Database.

 - Choose `3` nodes to create a high availability cluster that consists of one primary node and two replica nodes.

- A `2` node cluster is only available with a dedicated plan. It consists of one primary node and one replica node.
        
      valid_values: ['1', '2', '3']
      default: 1
    - name: engine
      value: string
      description: >
        The Managed Database engine in engine/version format.
        
    - name: engine_config
      value: object
      description: >
        Advanced parameters you can apply to a MySQL Managed Database, via our partner [Aiven's specification](https://aiven.io/docs/products/mysql/reference/advanced-params). Only include the objects for parameters you want to set in your database. Omit objects for parameters you don't want to define or change.

> 📘
>
> Aiven may offer additional parameters in their specification. Currently, only those listed here are supported for use in a MySQL Managed Database. You can also run the [List MySQL Managed Database advanced parameters](https://techdocs.akamai.com/linode-api/reference/get-databases-mysql-config) operation to see an up-to-date list.
        
    - name: fork
      value: object
      description: >
        Include this object to restore a Managed Database by forking from a backup.

- If you include this object, all other fields are optional.

- Don't include this object if you're creating a new Managed Database.
        
    - name: label
      value: string
      description: >
        __Filterable__ A unique, user-defined string referring to the Managed Database. This string needs to be unique per Managed Database engine type.
        
    - name: region
      value: string
      description: >
        __Filterable__ The [Region](https://techdocs.akamai.com/linode-api/reference/get-regions) ID for the Managed Database.
        
    - name: ssl_connection
      value: boolean
      description: >
        Currently required to be `true`. Whether to require SSL credentials to establish a connection to the Managed Database. Run the [Get managed MySQL database credentials](https://techdocs.akamai.com/linode-api/reference/get-databases-mysql-instance-credentials) operation for access information.
        
      default: true
    - name: type
      value: string
      description: >
        __Filterable__ The Linode Instance type used by the Managed Database for its nodes.
        
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="post_databases_mysql_instance_patch"
    values={[
        { label: 'post_databases_mysql_instance_patch', value: 'post_databases_mysql_instance_patch' }
    ]}
>
<TabItem value="post_databases_mysql_instance_patch">

Apply security patches and updates to the underlying operating system of the MySQL Managed Database. This function runs during regular maintenance windows, which you can configure with the [Update a managed MySQL database](https://techdocs.akamai.com/linode-api/reference/put-databases-mysql-instance) operation.<br /><br />- The user needs `read_write` [user grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) access to the database.<br /><br />- The database's status meeds to be `active`.<br /><br />- If your database cluster is configured with a single node, downtime occurs during maintenance updates. Consider upgrading to a [high availability](https://techdocs.akamai.com/cloud-computing/docs/aiven-database-clusters#high-availability) plan to avoid any maintenance downtime.<br /><br />- Major upgrades are optional until the service reaches end of service, and can be done in place.<br /><br />- A successful request triggers a `database_upgrade` [event](https://techdocs.akamai.com/linode-api/reference/get-events).<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
UPDATE linode.databases.mysql_instances
SET 
-- No updatable properties
WHERE 
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="put_databases_mysql_instance"
    values={[
        { label: 'put_databases_mysql_instance', value: 'put_databases_mysql_instance' }
    ]}
>
<TabItem value="put_databases_mysql_instance">

Make changes to an existing MySQL Managed Database.<br /><br />- The user needs `read_write` [user grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) access to the database.<br /><br />- The database's status needs to be `active`.<br /><br />- New values set in the `allow_list` overwrite existing values. To keep existing values, run the [List MySQL Managed Databases](https://techdocs.akamai.com/linode-api/reference/get-databases-mysql-instances) operation, store the `allow_list` addresses from the response, and include them with any new addresses in this operation.<br /><br />- Updates to your `allow_list` may take a short time to complete, making this operation inappropriate for rapid successive updates.<br /><br />- Also allows resizing the database cluster to a larger one. Clusters can't be resized to smaller plans.<br /><br />- All Managed Databases include automatic updates, which apply security patches to the underlying operating system of the Managed MySQL Database. Use the `updates` object in this operation to modify the maintenance window for these updates.<br /><br />- If your database cluster is configured with a single node, downtime occurs during maintenance updates. Use the `updates` object to adjust the window to match a time that's the least disruptive to your application and users. Also consider upgrading to a [high availability](https://techdocs.akamai.com/cloud-computing/docs/aiven-database-clusters#high-availability) plan to avoid any maintenance downtime.<br /><br />- Major upgrades are optional until the service reaches end of service, and can be done in place.<br /><br />- You can't update `engine_config` advanced parameter settings for a suspended database. You'll need to [resume](https://techdocs.akamai.com/linode-api/reference/resume-databases-mysql-instance) it first.<br /><br />- A successful request triggers a `database_update` [event](https://techdocs.akamai.com/linode-api/reference/get-events).<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
REPLACE linode.databases.mysql_instances
SET 
data__allow_list = '{{ allow_list }}',
data__engine_config = '{{ engine_config }}',
data__label = '{{ label }}',
data__type = '{{ type }}',
data__updates = '{{ updates }}',
data__version = '{{ version }}'
WHERE 

RETURNING
id,
allow_list,
cluster_size,
created,
encrypted,
engine,
engine_config,
fork,
hosts,
label,
members,
oldest_restore_time,
platform,
port,
region,
ssl_connection,
status,
total_disk_size_gb,
type,
updated,
updates,
used_disk_size_gb,
version;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_databases_mysql_instance"
    values={[
        { label: 'delete_databases_mysql_instance', value: 'delete_databases_mysql_instance' }
    ]}
>
<TabItem value="delete_databases_mysql_instance">

Remove a MySQL Managed Database from your account.<br /><br />- The user needs `read_write` [user grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) access to the database.<br /><br />- The database's status can be `active`, `failed`, or `degraded`.<br /><br />- Only unrestricted users can access this operation. They have access regardless of the acting token's OAuth scopes.<br /><br />[Learn more...](https://techdocs.akamai.com/cloud-computing/docs/getting-started-with-the-linode-cli)<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
DELETE FROM linode.databases.mysql_instances;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="resume_databases_mysql_instance"
    values={[
        { label: 'resume_databases_mysql_instance', value: 'resume_databases_mysql_instance' },
        { label: 'suspend_databases_mysql_instance', value: 'suspend_databases_mysql_instance' }
    ]}
>
<TabItem value="resume_databases_mysql_instance">

Resume a suspended MySQL Managed Database from your account. This resumes billing for the cluster.<br /><br />- The user needs `read_write` [user grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) access to the database.<br /><br />- The database's status needs to be `suspended`.<br /><br />- A successful request triggers a `database_resume` [event](https://techdocs.akamai.com/linode-api/reference/get-events). __OAuth scopes__.<br /><br />    ```<br />    databases:read_write<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.databases.mysql_instances.resume_databases_mysql_instance 
;
```
</TabItem>
<TabItem value="suspend_databases_mysql_instance">

Suspend a MySQL Managed Database from your account, releasing idle resources and keeping only necessary data. All service data is lost if there are no backups available. This halts billing for the cluster.<br /><br />- The user needs `read_write` [user grant](https://techdocs.akamai.com/linode-api/reference/get-user-grants) access to the database.<br /><br />- The database's status needs to be `active`.<br /><br />- Akamai deletes suspended clusters after 180 days.<br /><br />- A successful request triggers a `database_update` [event](https://techdocs.akamai.com/linode-api/reference/get-events). __OAuth scopes__.<br /><br />    ```<br />    databases:read_write<br />    ```<br /><br />[Learn more...](https://techdocs.akamai.com/linode-api/reference/get-started#oauth)

```sql
EXEC linode.databases.mysql_instances.suspend_databases_mysql_instance 
;
```
</TabItem>
</Tabs>
