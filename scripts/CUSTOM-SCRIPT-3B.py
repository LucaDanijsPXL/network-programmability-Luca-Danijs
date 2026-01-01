from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.56.101",  # Replace with your router IP
    "username": "cisco",
    "password": "cisco123!"
}

# VLANs and subnets
vlans = {
    10: {"name": "Management", "subnet": "172.16.1.0", "ip": "172.16.1.1"},
    20: {"name": "VM-Hosts", "subnet": "172.16.1.16", "ip": "172.16.1.17"},
    30: {"name": "Appliance-Servers", "subnet": "172.16.1.32", "ip": "172.16.1.33"},
    40: {"name": "Data-Users", "subnet": "172.16.1.48", "ip": "172.16.1.49"},
    99: {"name": "Native-VLAN", "subnet": None, "ip": None}
}

# Connect to device
net = ConnectHandler(**device)

# Create VLANs
for vlan_id, vlan_info in vlans.items():
    net.send_config_set([
        f"vlan {vlan_id}",
        f"name {vlan_info['name']}"
    ])

# Configure VLAN interfaces with IPs
for vlan_id, vlan_info in vlans.items():
    if vlan_info["ip"]:
        commands = [
            f"interface vlan {vlan_id}",
            f"ip address {vlan_info['ip']} 255.255.255.240",  # /28 subnet
            "no shutdown"
        ]
        net.send_config_set(commands)

net.disconnect()
print("VLANs and subnets configured successfully.")
