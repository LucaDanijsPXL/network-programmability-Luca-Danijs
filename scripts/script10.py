device1 = {
    "device_type": "cisco_ios",
    "host": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
}

device2 = {
    "device_type": "cisco_ios",
    "host": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
}

devices = [device1, device2]

from netmiko import ConnectHandler

for device in devices:
    net = ConnectHandler(**device)
    net.send_config_set(["ntp server 10.10.10.10"])
    net.disconnect()
