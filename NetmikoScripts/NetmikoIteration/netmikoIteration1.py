from netmiko import ConnectHandler
# netmiko documentation https://github.com/ktbyers/netmiko/blob/develop/EXAMPLES.md

# dictionary containing device information
node = {
    "device_type": "cisco_ios",
    "ip": "192.168.122.207",
    "username": "jacob",
    "password": "cisco"
}

# add commands to a file to have simple script apply commands automatically
with open("commands_file") as f:  # with open closes the file when operation complete, meaning we dont need to write code to close the file manually
    # read lines, split the lines and place each line in variable commands
    commands = f.read().splitlines()

# creating a list of devices, to add more devices to the list we can create additional dictionaries of devices and append them into the list
all_devices = [node]

# for loop will iterate through all_devices list, netmiko will connect to each device and apply configurations from commands_file and then print the output
for device in all_devices:
    netmiko_connect = ConnectHandler(**device)
    output = netmiko_connect.send_config_set(commands)
    print(output)
