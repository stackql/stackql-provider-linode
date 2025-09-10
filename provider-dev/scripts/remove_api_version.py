#!/usr/bin/env python3
import json
import re
import os

# Input and output file paths
input_file = 'provider-dev/downloaded/openapi.json'
output_file = 'provider-dev/downloaded/openapi_api_version_removed.json'

# Load the OpenAPI spec
with open(input_file, 'r') as f:
    openapi_spec = json.load(f)

# Process paths
new_paths = {}
for path, path_item in openapi_spec['paths'].items():

    print(f"Processing path: {path}")
    print("==========")
    # Remove {apiVersion} from path
    new_path = path.replace('/{apiVersion}', '')
    
    # Process each operation in the path
    for verb, operation in path_item.items():
        if verb != 'parameters':
            if 'description' in operation:
                description = operation['description']
                description = re.sub(r'\n\n\n<<LB>>\n\n---\n\n\n-', '', description)
                description = re.sub(r'__CLI__\.\n\n\s*```[\s\S]*?```\n\n', '', description)
                description = re.sub(r'\n\n- __OAuth scopes__\.\n\n\s*```[\s\S]*?```\n\n', '', description)
                description = re.sub(r'\s*\[Learn more\.\.\.\]', r'\n\n[Learn more...]', description)
                operation['description'] = description

        if verb == 'parameters':
            for param in operation:
                if param["name"] == "apiVersion" and param["in"] == "path":
                    print(f"Removing apiVersion parameter from path item parameters")
                    operation.remove(param)

    new_paths[new_path] = path_item

# Replace the paths in the spec
openapi_spec['paths'] = new_paths

# Remove apiVersion from components.parameters if it exists
if 'components' in openapi_spec and 'parameters' in openapi_spec['components']:
    if 'api-version-path' in openapi_spec['components']['parameters']:
        del openapi_spec['components']['parameters']['api-version-path']

with open(output_file, 'w') as f:
    json.dump(openapi_spec, f, indent=2)

print(f"Processed OpenAPI spec saved to {output_file}")