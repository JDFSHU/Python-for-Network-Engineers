from netmiko import ConnectHandler
# netmiko documentation https://github.com/ktbyers/netmiko/blob/develop/EXAMPLES.md

# opening commands_file splittings lines and placing into commands variable
with open("commands_file") as f:
    commands = f.read().splitlines()

# opening devices_file splittings lines and placing into nodes variable
with open("devices_file") as f:
    nodes = f.read().splitlines()

# for loop iterates through each entry in nodes variable
for device in nodes:
    print(f"Connecting to device {device}")
    ip_address_of_device = device  # placing each device into ip address variable
    # placing ip address into a template for netmiko connection
    node_template = {
        "device_type": "cisco_ios",
        "ip": ip_address_of_device,
        "username": "jacob",
        "password": "cisco"
    }
    netmiko_connect = ConnectHandler(
        **node_template)  # connecting to node_template
    # sending commands collected originally from file
    output = netmiko_connect.send_config_set(commands)
    print(output)
