device1 = {
    "device_type": "cisco_ios",
    "host": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
}

from netmiko import ConnectHandler

net = ConnectHandler(**device1)

config_commands = [
    "interface loopback100",
    "ip address 100.100.100.1 255.255.255.255",
    "description Configured_by_Netmiko"
]

net.send_config_set(config_commands)
net.disconnect()
