# `linode` provider for [`stackql`](https://github.com/stackql/stackql)

This repository is used to generate and document the `linode` provider for StackQL, allowing you to query and manipulate Linode resources using SQL-like syntax. The provider is built using the `@stackql/provider-utils` package, which provides tools for converting OpenAPI specifications into StackQL-compatible provider schemas.

## Prerequisites

To use the Linode provider with StackQL, you'll need:

1. A Linode account with appropriate API credentials
2. A Linode API token with sufficient permissions for the resources you want to access
3. StackQL CLI installed on your system (see [StackQL](https://github.com/stackql/stackql))

## 1. Download the Open API Specification

First, download the Linode API OpenAPI specification:

```bash
rm provider-dev/downloaded/*
curl -L https://github.com/linode/linode-api-docs/raw/refs/heads/development/openapi.json \
  -o provider-dev/downloaded/openapi.json

# pre process the spec to remove the apiVersion path param
python3 provider-dev/scripts/remove_api_version.py
```

## 2. Split into Service Specs

Next, split the monolithic OpenAPI specification into service-specific files:

```bash
rm -rf provider-dev/source/*
npm run split -- \
  --provider-name linode \
  --api-doc provider-dev/downloaded/openapi_api_version_removed.json \
  --svc-discriminator path \
  --output-dir provider-dev/source \
  --overwrite \
  --svc-name-overrides "$(cat <<EOF
{
  "network_transfer": "networking"
}
EOF
)"    
```

## 3. Generate Mappings

Generate the mapping configuration that connects OpenAPI operations to StackQL resources:

```bash
npm run generate-mappings -- \
  --provider-name linode \
  --input-dir provider-dev/source \
  --output-dir provider-dev/config
```

Update the resultant `provider-dev/config/all_services.csv` to add the `stackql_resource_name`, `stackql_method_name`, `stackql_verb` values for each operation.

## 4. Generate Provider

This step transforms the split OpenAPI service specs into a fully-functional StackQL provider by applying the resource and method mappings defined in your CSV file.

```bash
rm -rf provider-dev/openapi/*
npm run generate-provider -- \
  --provider-name linode \
  --input-dir provider-dev/source \
  --output-dir provider-dev/openapi/src/linode \
  --config-path provider-dev/config/all_services.csv \
  --servers '[{"url": "https://api.linode.com/v4"}]' \
  --provider-config '{"auth": {"credentialsenvvar": "LINODE_TOKEN","type": "bearer"}}' \
  --overwrite
```

Make necessary updates to the output docs:

```bash
python3 provider-dev/scripts/update_linode_interfaces.py
python3 provider-dev/scripts/update_managed_stats.py
```

## 5. Test Provider

### Starting the StackQL Server

Before running tests, start a StackQL server with your provider:

```bash
PROVIDER_REGISTRY_ROOT_DIR="$(pwd)/provider-dev/openapi"
npm run start-server -- --provider linode --registry $PROVIDER_REGISTRY_ROOT_DIR
```

### Test Meta Routes

Test all metadata routes (services, resources, methods) in the provider:

```bash
npm run test-meta-routes -- linode --verbose
```

When you're done testing, stop the StackQL server:

```bash
npm run stop-server
```

Use this command to view the server status:

```bash
npm run server-status
```

### Run test queries

Run some test queries against the provider using the `stackql shell`:

```bash
PROVIDER_REGISTRY_ROOT_DIR="$(pwd)/provider-dev/openapi"
REG_STR='{"url": "file://'${PROVIDER_REGISTRY_ROOT_DIR}'", "localDocRoot": "'${PROVIDER_REGISTRY_ROOT_DIR}'", "verifyConfig": {"nopVerify": true}}'
./stackql shell --registry="${REG_STR}"
```

Example queries to try:

```sql
-- Get account information
SELECT 
company,
country,
balance,
balance_uninvoiced,
active_since
FROM linode.account.account;

--- List Database Engines
SELECT
id,
engine,
version
FROM linode.databases.engines;

-- Show Region Availability
SELECT
available,
plan,
region
FROM linode.regions.availability;

-- List all Linode instances
SELECT
id,
created,
disk_encryption,
group,
has_user_data,
hypervisor,
ipv4,
ipv6,
label,
region,
status,
tags,
type,
updated,
watchdog_enabled
FROM linode.linode.instances;
```

## 6. Publish the provider

To publish the provider push the `linode` dir to `providers/src` in a feature branch of the [`stackql-provider-registry`](https://github.com/stackql/stackql-provider-registry). Follow the [registry release flow](https://github.com/stackql/stackql-provider-registry/blob/dev/docs/build-and-deployment.md).  

Launch the StackQL shell:

```bash
export DEV_REG="{ \"url\": \"https://registry-dev.stackql.app/providers\" }"
./stackql --registry="${DEV_REG}" shell
```

pull the latest dev `linode` provider:

```sql
registry pull linode;
```

Run some test queries to verify the provider works as expected.

## 7. Generate web docs

Provider doc microsites are built using Docusaurus and published using GitHub Pages.  

a. Update `headerContent1.txt` and `headerContent2.txt` accordingly in `provider-dev/docgen/provider-data/`  

b. Update the following in `website/docusaurus.config.js`:  

```js
// Provider configuration - change these for different providers
const providerName = "linode";
const providerTitle = "Linode Provider";
```

c. Then generate docs using...

```bash
npm run generate-docs -- \
  --provider-name linode \
  --provider-dir ./provider-dev/openapi/src/linode/v00.00.00000 \
  --output-dir ./website \
  --provider-data-dir ./provider-dev/docgen/provider-data
```  

## 8. Test web docs locally

```bash
cd website
# test build
yarn build

# run local dev server
yarn start
```

## 9. Publish web docs to GitHub Pages

Under __Pages__ in the repository, in the __Build and deployment__ section select __GitHub Actions__ as the __Source__. In Netlify DNS create the following records:

| Source Domain | Record Type  | Target |
|---------------|--------------|--------|
| linode-provider.stackql.io | CNAME | stackql.github.io. |

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.