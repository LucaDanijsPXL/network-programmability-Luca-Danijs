device1 = {
    "device_type": "cisco_ios",
    "host": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
}

from netmiko import ConnectHandler

def backup_device(net):
    config = net.send_command("show run")
    with open("backup.cfg", "w") as f:
        f.write(config)

net = ConnectHandler(**device1)
backup_device(net)
net.disconnect()
