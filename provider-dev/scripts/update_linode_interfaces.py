import yaml
import os

# Define the path to the file
file_path = 'provider-dev/openapi/src/linode/v00.00.00000/services/linode.yaml'

# Define the new schema
new_schema = {
  "description": "Interface type can be VPC, public, or VLAN.",
  "type": "object",
  "properties": {
    "created": {
      "description": "When the interface was created.",
      "example": "2025-01-01T00:01:01",
      "format": "date-time",
      "type": "string",
      "x-linode-cli-display": 3
    },
    "default_route": {
      "description": "Indicates if the interface is used as a default route.",
      "nullable": True,
      "type": "object",
      "properties": {
        "ipv4": {
          "default": False,
          "description": "Indicates if the interface is used for the IPv4 default route. Only one interface per Linode can have the IPv4 default route.",
          "example": True,
          "type": "boolean",
          "x-linode-cli-display": 5
        },
        "ipv6": {
          "default": False,
          "description": "Indicates if the interface is used for the IPv6 default route. Only one interface per Linode can have the IPv6 default route.",
          "example": True,
          "type": "boolean",
          "x-linode-cli-display": 6
        }
      }
    },
    "id": {
      "description": "__Read-only__ The unique ID for this interface. For `dry_run` upgrades, a unique `id` is not generated for the interface and its value is set to 0.",
      "example": 1234,
      "readOnly": True,
      "type": "integer",
      "x-linode-cli-display": 1
    },
    "mac_address": {
      "description": "A 48-bit MAC address used to identify the Linode's interface. The `mac_address` of an interface remains constant and does not change.",
      "example": "22:00:AB:CD:EF:01",
      "maxLength": 64,
      "minLength": 1,
      "pattern": "[a-zA-Z0-9-]+",
      "type": "string",
      "x-linode-cli-display": 2
    },
    "public": {
      "description": "Public interface configuration. Null if not a public interface.",
      "nullable": True,
      "type": "object",
      "properties": {
        "ipv4": {
          "description": "The interface's public IPv4 `addresses`.",
          "type": "object",
          "properties": {
            "addresses": {
              "description": "The public IPv4 addresses and primary settings for this public interface.",
              "items": {
                "type": "object",
                "properties": {
                  "address": {
                    "description": "The public IPv4 address assigned to this interface.",
                    "example": "172.232.100.100",
                    "type": "string",
                    "x-linode-cli-display": 8
                  },
                  "primary": {
                    "description": "Indicates if the public IPv4 address serves as the source address for traffic routing within the Linode.",
                    "example": True,
                    "type": "boolean",
                    "x-linode-cli-display": 9
                  }
                }
              },
              "type": "array"
            },
            "shared": {
              "description": "The IPv4 address assigned to this Linode interface, which is also shared with another Linode.",
              "items": {
                "type": "object",
                "properties": {
                  "address": {
                    "description": "Shared IPv4 address.",
                    "example": "172.222.33.4",
                    "type": "string",
                    "x-linode-cli-display": 10
                  },
                  "linode_id": {
                    "description": "The ID of the Linode this address currently belongs to.",
                    "example": 12345,
                    "type": "string",
                    "x-linode-cli-display": 11
                  }
                }
              },
              "type": "array"
            }
          }
        },
        "ipv6": {
          "description": "The interface's public IPv6 configuration.",
          "type": "object",
          "properties": {
            "ranges": {
              "description": "List of IPv6 ranges assigned to this interface.",
              "items": {
                "type": "object",
                "properties": {
                  "range": {
                    "description": "IPv6 range in CIDR notation (`2600:0db8::1/64`) or prefix-only (`/64`).",
                    "example": "2600:3c09:e001:59::/64",
                    "type": "string",
                    "x-linode-cli-display": 16
                  },
                  "route_target": {
                    "description": "The public IPv6 address that the `range` is routed to.",
                    "example": "2600:3c09::ff:feab:cdef",
                    "type": "string",
                    "x-linode-cli-display": 17
                  }
                }
              },
              "type": "array"
            },
            "shared": {
              "description": "The IPv6 address assigned to this Linode interface, which is also shared with another Linode.",
              "items": {
                "type": "object",
                "properties": {
                  "range": {
                    "description": "The IPv6 address range.",
                    "example": "2600:3c09:e001:2a::/64",
                    "type": "string",
                    "x-linode-cli-display": 14
                  },
                  "route_target": {
                    "description": "The public IPv6 address that the `range` is routed to.",
                    "example": None,
                    "type": "string",
                    "x-linode-cli-display": 15
                  }
                }
              },
              "type": "array"
            },
            "slaac": {
              "description": "The public `slaac` and subnet prefix settings for this public interface.",
              "items": {
                "type": "object",
                "properties": {
                  "address": {
                    "description": "Public IPv6 addresses assigned to this interface.",
                    "example": "2600:3c09::ff:feab:cdef",
                    "type": "string",
                    "x-linode-cli-display": 12
                  },
                  "prefix": {
                    "description": "The prefix length advertised for SLAAC to use.",
                    "example": 64,
                    "type": "integer",
                    "x-linode-cli-display": 13
                  }
                }
              },
              "type": "array"
            }
          }
        }
      }
    },
    "updated": {
      "description": "When the interface was last updated.",
      "example": "2025-01-01T00:01:01",
      "format": "date-time",
      "type": "string",
      "x-linode-cli-display": 4
    },
    "version": {
      "description": "Interface version number that increments when the interface updates.",
      "example": 1,
      "type": "integer",
      "x-linode-cli-display": 7
    },
    "vlan": {
      "description": "VLAN interface configuration. Null if not a VLAN interface.",
      "nullable": True,
      "type": "object",
      "properties": {
        "ipam_address": {
          "description": "This VLAN interface's private IPv4 address in classless inter-domain routing (CIDR) notation.",
          "example": "10.0.0.1/24",
          "format": "ip/netmask",
          "nullable": True,
          "type": "string",
          "x-linode-cli-display": 7
        },
        "vlan_label": {
          "description": "The VLAN's label. VLAN interfaces on the same Linode must have a unique `vlan_label`.",
          "example": "my-vlan",
          "type": "string",
          "x-linode-cli-display": 6
        }
      }
    },
    "vpc": {
      "description": "VPC interface configuration. Null if not a VPC interface.",
      "nullable": True,
      "type": "object",
      "properties": {
        "ipv4": {
          "description": "The interface's IPv4 `addresses` and `ranges` configuration.",
          "type": "object",
          "properties": {
            "addresses": {
              "description": "IPv4 address settings for this VPC interface.",
              "items": {
                "type": "object",
                "properties": {
                  "address": {
                    "description": "The VPC subnet IPv4 address.",
                    "example": "192.168.22.3",
                    "type": "string",
                    "x-linode-cli-display": 9
                  },
                  "nat_1_1_address": {
                    "description": "The 1:1 NAT IPv4 address used to associate a public IPv4 address with the interface's VPC subnet IPv4 address.",
                    "example": None,
                    "nullable": True,
                    "type": "string",
                    "x-linode-cli-display": 11
                  },
                  "primary": {
                    "description": "Indicates if the IPv4 address is used to set up a source address for routes inside the Linode.",
                    "example": True,
                    "type": "boolean",
                    "x-linode-cli-display": 10
                  }
                }
              },
              "type": "array"
            },
            "ranges": {
              "description": "VPC IPv4 ranges.",
              "items": {
                "type": "object",
                "properties": {
                  "range": {
                    "description": "CIDR notation of a range (`1.2.3.4/24`) or prefix only (`/24`).",
                    "example": "192.168.22.16/28",
                    "type": "string",
                    "x-linode-cli-display": 12
                  }
                }
              },
              "type": "array"
            }
          }
        },
        "subnet_id": {
          "description": "VPC subnet's unique identifier.",
          "example": 1234,
          "type": "integer",
          "x-linode-cli-display": 8
        },
        "vpc_id": {
          "description": "VPC's unique identifier.",
          "example": 1234,
          "type": "integer",
          "x-linode-cli-display": 7
        }
      }
    }
  }
}

def update_linode_interfaces():
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Error: File not found at {file_path}")
            return False
            
        # Read the YAML file
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)

        for path in data.get('paths', {}):
            if path == '/linode/instances/{linodeId}/interfaces/{interfaceId}':
                get_operation = data['paths'][path].get('get', {})
                responses = get_operation.get('responses', {})
                response_200 = responses.get('200', {})
                content = response_200.get('content', {})
                app_json = content.get('application/json', {})
                
                if app_json:
                    # Update the schema
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
    update_linode_interfaces()