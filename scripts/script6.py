device1 = {
    "device_type": "cisco_ios",
    "host": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
}

from netmiko import ConnectHandler

interfaces = ["GigabitEthernet1", "GigabitEthernet2"]

net = ConnectHandler(**device1)

for intf in interfaces:
    net.send_config_set([
        f"interface {intf}",
        "description Configured_by_Script",
        "no shutdown"
    ])

net.disconnect()
