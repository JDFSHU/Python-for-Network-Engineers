from getpass import getpass
from netmiko import NetmikoAuthenticationException
from paramiko import SSHException
from netmiko import NetmikoTimeoutException
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
# exception handling common errors that might occur when ssh'ing to a device
    try:  # try to connect to device using netmiko's ConnectHandler
        netmiko_connect = ConnectHandler(**node_template)
    except (NetmikoAuthenticationException):
        print(f"Authentication failure: {ip_address_of_device}")
        continue
    except (NetmikoTimeoutException):
        print(f"Connection Timeout: {ip_address_of_device}")
        continue
    except (EOFError):
        print(f"End of file while attempting device: {ip_address_of_device}")
        continue
    except (SSHException):
        print(f"SSH FAILED. Is SSH enabled on {ip_address_of_device}")
    except Exception as unknown_error:
        print(f"Unkown Error: " + str(unknown_error))
        continue

    output = netmiko_connect.send_config_set(commands)
    print(output)
