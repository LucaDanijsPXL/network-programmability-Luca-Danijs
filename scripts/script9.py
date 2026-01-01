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

from netmiko import ConnectHandler

devices = [device1, device2]

for device in devices:
    net = ConnectHandler(**device)
    print(net.send_command("show ip route"))
    net.disconnect()
