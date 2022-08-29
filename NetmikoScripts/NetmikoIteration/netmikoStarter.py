from netmiko import ConnectHandler
# netmiko documentation https://github.com/ktbyers/netmiko/blob/develop/EXAMPLES.md

# dictionary containing device information
node = {
    "device_type": "cisco_ios",
    "ip": "192.168.122.205",
    "username": "jacob",
    "password": "cisco"
}

# using connecthandler to connect to the device information contained within the device dictionary
netmiko_connect = ConnectHandler(**node)
# sending command "show ip interface brief" to device and saving output to a variable
output = netmiko_connect.send_command("show ip interface brief")
print(output)  # printing the output of the command entered
