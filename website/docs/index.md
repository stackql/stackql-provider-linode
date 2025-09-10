---
title: linode
hide_title: false
hide_table_of_contents: false
keywords:
  - linode
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/stackql-linode-provider-featured-image.png
id: 'provider-intro'
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Cloud hosting platform that provides virtual private servers, Kubernetes, managed databases, and other cloud infrastructure services.

:::info[Provider Summary] 

total services: __20__  
total resources: __156__  

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `linode` provider, run the following command:  

```bash
REGISTRY PULL linode;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

The following system environment variables are used for authentication by default:  

- <CopyableCode code="LINODE_TOKEN" /> - Linode API token (see <a href="https://www.linode.com/docs/products/tools/api/guides/manage-api-tokens/#create-an-api-token">How to Create a Linode API Token</a>)
  
These variables are sourced at runtime (from the local machine or as CI variables/secrets).  

<details>

<summary>Using different environment variables</summary>

To use different environment variables (instead of the defaults), use the `--auth` flag of the `stackql` program.  For example:  

```bash

AUTH='{ "linode": { "type": "bearer",  "credentialsenvvar": "YOUR_LINODE_TOKEN_VAR" }}'
stackql shell --auth="${AUTH}"

```
or using PowerShell:  

```powershell

$Auth = "{ 'linode': { 'type': 'bearer',  'credentialsenvvar': 'YOUR_LINODE_TOKEN_VAR' }}"
stackql.exe shell --auth=$Auth

```
</details>

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/services/account/">account</a><br />
<a href="/services/betas/">betas</a><br />
<a href="/services/databases/">databases</a><br />
<a href="/services/domains/">domains</a><br />
<a href="/services/images/">images</a><br />
<a href="/services/linode/">linode</a><br />
<a href="/services/lke/">lke</a><br />
<a href="/services/longview/">longview</a><br />
<a href="/services/managed/">managed</a><br />
<a href="/services/monitor/">monitor</a><br />
</div>
<div class="providerDocColumn">
<a href="/services/networking/">networking</a><br />
<a href="/services/nodebalancers/">nodebalancers</a><br />
<a href="/services/object_storage/">object_storage</a><br />
<a href="/services/placement/">placement</a><br />
<a href="/services/profile/">profile</a><br />
<a href="/services/regions/">regions</a><br />
<a href="/services/support/">support</a><br />
<a href="/services/tags/">tags</a><br />
<a href="/services/volumes/">volumes</a><br />
<a href="/services/vpcs/">vpcs</a><br />
</div>
</div>
