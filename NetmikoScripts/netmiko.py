from distutils.command.config import config
from netmiko import ConnectHandler
# netmiko documentation https://github.com/ktbyers/netmiko/blob/develop/EXAMPLES.md


# switch information stored in a dictionary to be called later
iou_l2 = {
    "device_type": "cisco_ios",
    "ip": "10.0.0.2",
    "username": "jacob",
    "password": "cisco",
}

# Establish an SSH connection to the device by passing in the device dictionary.
net_connect = ConnectHandler(**iou_l2)
output = net_connect.send_command("show ip int brief")
print(output)

# Execute configuration change commands (will automatically enter into config mode)
config_commands = ["int loop 0", "ip address 1.1.1.1 255.255.255.0"]
# sending config commands to output variable so they can be printed as they are entered
output = net_connect.send_config_set(config_commands)
print(output)

for n in range(2, 21):
    print("Creating VLAN " + str(n))
    config_commands = ["vlan " + str(n), "name Python_VLAN " + str(n)]
    # sending config commands to output variable so they can be printed as they are entered
    output = net_connect.send_config_set(config_commands)
    print(output)
