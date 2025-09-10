import yaml
import os

# Define the path to the file
file_path = 'provider-dev/openapi/src/linode/v00.00.00000/services/managed.yaml'

# Define the new schema
new_schema = {
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "cpu": {
          "description": "CPU usage stats from the last 24 hours.",
          "items": {
            "description": "A stat data point.",
            "properties": {
              "x": {
                "description": "**Read-only** A stats graph data point.",
                "example": 11513761600000,
                "readOnly": True,
                "type": "integer"
              },
              "y": {
                "description": "**Read-only** A stats graph data point.",
                "example": 29.94,
                "readOnly": True,
                "type": "integer"
              }
            },
            "type": "object"
          },
          "type": "array"
        },
        "disk": {
          "description": "Disk usage stats from the last 24 hours.",
          "items": {
            "description": "A stat data point.",
            "properties": {
              "x": {
                "description": "**Read-only** A stats graph data point.",
                "example": 11513761600000,
                "readOnly": True,
                "type": "integer"
              },
              "y": {
                "description": "**Read-only** A stats graph data point.",
                "example": 29.94,
                "readOnly": True,
                "type": "integer"
              }
            },
            "type": "object"
          },
          "type": "array"
        },
        "net_in": {
          "description": "Inbound network traffic stats from the last 24 hours.",
          "items": {
            "description": "A stat data point.",
            "properties": {
              "x": {
                "description": "**Read-only** A stats graph data point.",
                "example": 11513761600000,
                "readOnly": True,
                "type": "integer"
              },
              "y": {
                "description": "**Read-only** A stats graph data point.",
                "example": 29.94,
                "readOnly": True,
                "type": "integer"
              }
            },
            "type": "object"
          },
          "type": "array"
        },
        "net_out": {
          "description": "Outbound network traffic stats from the last 24 hours.",
          "items": {
            "description": "A stat data point.",
            "properties": {
              "x": {
                "description": "**Read-only** A stats graph data point.",
                "example": 11513761600000,
                "readOnly": True,
                "type": "integer"
              },
              "y": {
                "description": "**Read-only** A stats graph data point.",
                "example": 29.94,
                "readOnly": True,
                "type": "integer"
              }
            },
            "type": "object"
          },
          "type": "array"
        },
        "swap": {
          "description": "Swap usage stats from the last 24 hours.",
          "items": {
            "description": "A stat data point.",
            "properties": {
              "x": {
                "description": "**Read-only** A stats graph data point.",
                "example": 11513761600000,
                "readOnly": True,
                "type": "integer"
              },
              "y": {
                "description": "**Read-only** A stats graph data point.",
                "example": 29.94,
                "readOnly": True,
                "type": "integer"
              }
            },
            "type": "object"
          },
          "type": "array"
        },
        "0": {
          "example": "Graphs are not yet available.",
          "type": "string"
        },
        "1": {
          "example": "Graphs are not yet available.",
          "type": "string"
        },
        "2": {
          "example": "Graphs are not yet available.",
          "type": "string"
        }
      },
      "description": "Stats data that can either be detailed metrics or error messages if unavailable."
    }
  },
  "type": "object"
}

def update_managed_stats():
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Error: File not found at {file_path}")
            return False
            
        # Read the YAML file
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)

        for path, path_data in data.get('paths', {}).items():
            if path == '/managed/stats':
                get_operation = path_data.get('get', {})
                responses = get_operation.get('responses', {})
                response_200 = responses.get('200', {})
                content = response_200.get('content', {})
                app_json = content.get('application/json', {})
                
                if app_json:
                    app_json['schema'] = new_schema
                    
                    # Write the updated data back to the file
                    with open(file_path, 'w') as file:
                        yaml.dump(data, file, default_flow_style=False, sort_keys=False)
                            
                    print(f"Successfully updated schema in {file_path}")
                    return True
                else:
                    print("Error: 'application/json' not found in the 200 response content")
                    return False
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    update_managed_stats()