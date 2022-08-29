from netmiko import ConnectHandler
# netmiko documentation https://github.com/ktbyers/netmiko/blob/develop/EXAMPLES.md

sw1 = {
    "device_type": "cisco_ios",
    "ip": "10.0.0.2",
    "username": "jacob",
    "password": "cisco"
}

sw5 = {
    "device_type": "cisco_ios",
    "ip": "10.0.0.5",
    "username": "jacob",
    "password": "cisco"
}

all_devices = [sw1, sw5]

for devices in all_devices:
    netmiko_connect = ConnectHandler(**devices)
    for n in range(2, 11):
        print("Creating VLAN " + str(n))
        config_commands = ["Vlan " + str(n), "name Python_VLAN " + str(n)]
        output = netmiko_connect.send_config_set(config_commands)
        print(output)
