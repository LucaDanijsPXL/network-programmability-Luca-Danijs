device1 = {
    "device_type": "cisco_ios",
    "host": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
}

from netmiko import ConnectHandler

net = ConnectHandler(**device1)
backup = net.send_command("show running-config")

with open("router_backup.cfg", "w") as f:
    f.write(backup)

net.disconnect()
