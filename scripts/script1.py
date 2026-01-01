device1 = {
    "device_type": "cisco_ios",
    "host": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
}

from netmiko import ConnectHandler

net = ConnectHandler(**device1)
output = net.send_command("show ip interface brief")
print(output)
net.disconnect()

