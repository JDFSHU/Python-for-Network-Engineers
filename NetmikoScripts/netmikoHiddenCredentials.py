from getpass import getpass
from netmiko import ConnectHandler
# netmiko documentation https://github.com/ktbyers/netmiko/blob/develop/EXAMPLES.md

# promting user to enter credentials and placing credentials into variables
username = input("Enter Username: ")
password = getpass()


with open("commands_file") as f:
    commands = f.read().splitlines()

with open("devices_file") as f:
    nodes = f.read().splitlines()

# for loop iterates through each entry in nodes variable
for device in nodes:
    print(f"Connecting to {device}")
    ip_address_of_device = device  # placing each device into ip address variable
    # placing ip address into a template for netmiko connection with username and password
    node_template = {
        "device_type": "cisco_ios",
        "ip": ip_address_of_device,
        "username": username,
        "password": password
    }
    netmiko_connect = ConnectHandler(**node_template)
    # sending commands collected originally from file
    output = netmiko_connect.send_config_set(commands)
    print(output)
