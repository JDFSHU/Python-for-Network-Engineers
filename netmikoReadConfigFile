from netmiko import ConnectHandler
# netmiko documentation https://github.com/ktbyers/netmiko/blob/develop/EXAMPLES.md

# dictionaries contain information on devices
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

with open("documentName") as f:  # opening the file "document name" replace this with the file name
    # reads each line in the file and places it in variable "lines"
    lines = f.read().splitlines()
print(lines)  # prints a list of the commands about to be applied

# list that holds the dictionaries which contain information about each device
all_devices = [sw1, sw5]

for devices in all_devices:  # for loop that iterates through the list and for each item or "device" it will perform below actions
    # netmiko ConnectHandler used to connect to the device being iterated through
    netmiko_connect = ConnectHandler(**devices)
    # each line of the file represents a configuration, send_config_set is sending each line of the file to the device
    output = netmiko_connect.send_config_set(lines)
    print(output)  # printing output of commands so we can see whats happening
