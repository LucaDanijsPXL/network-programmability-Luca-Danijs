device1 = {
    "device_type": "cisco_ios",
    "host": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
}

from netmiko import ConnectHandler

net = ConnectHandler(**device1)
version = net.send_command("show version")

if "IOS-XE" in version:
    print("IOS-XE Device Detected")
else:
    print("Unknown Device")

net.disconnect()
