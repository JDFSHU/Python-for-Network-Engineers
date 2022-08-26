from netmiko import ConnectHandler
# netmiko documentation https://github.com/ktbyers/netmiko/blob/develop/EXAMPLES.md

asw1 = {
    "device_type": "cisco_ios",
    "ip": "10.0.0.1",
    "username": "jacob",
    "password": "cisco"
}

asw2 = {
    "device_type": "cisco_ios",
    "ip": "10.0.0.2",
    "username": "jacob",
    "password": "cisco"
}

asw3 = {
    "device_type": "cisco_ios",
    "ip": "10.0.0.3",
    "username": "jacob",
    "password": "cisco"
}

dist1 = {
    "device_type": "cisco_ios",
    "ip": "10.0.0.11",
    "username": "jacob",
    "password": "cisco"
}

dist2 = {
    "device_type": "cisco_ios",
    "ip": "10.0.0.12",
    "username": "jacob",
    "password": "cisco"
}

# General configs for switches on the entire network, applied to all switches
with open("allSwitchesConfig") as f:
    lines = f.read().splitlines()

all_devices = [asw1, asw2, asw3, dist1, dist2]

for devices in all_devices:
    netmiko_connect = ConnectHandler(**devices)
    output = netmiko_connect.send_config_set(lines)
    print(output)

# Configuration commands specifically applied to access layer switches only
with open("accessSwitchConfig") as f:
    lines = f.read().splitlines()

access_layer_switches = [asw1, asw2, asw3]

for devices in access_layer_switches:
    netmiko_connect = ConnectHandler(**devices)
    output = netmiko_connect.send_config_set(lines)
    print(output)

# Config commands specifically applied to distribution layer swiches only
with open("distSwitchConfigs") as f:
    lines = f.read().splitlines()

dist_switches = [dist1, dist2]

for devices in dist_switches:
    netmiko_connect = ConnectHandler(**devices)
    output = netmiko_connect.send_config_set(lines)
    print(output)
