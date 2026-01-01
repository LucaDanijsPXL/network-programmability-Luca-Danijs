device1 = {
    "device_type": "cisco_ios",
    "host": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
}

from netmiko import ConnectHandler

net = ConnectHandler(**device1)
net.send_config_from_file("config.txt")
net.disconnect()
