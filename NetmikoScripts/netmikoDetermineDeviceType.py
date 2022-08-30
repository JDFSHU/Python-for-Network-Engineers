from netmiko import ConnectHandler
from getpass import getpass
from netmiko import NetmikoAuthenticationException
from netmiko import NetmikoTimeoutException
from paramiko import SSHException
# netmiko documentation https://github.com/ktbyers/netmiko/blob/develop/EXAMPLES.md

username = input("Enter Username: ")
password = getpass()

with open("commands_file_switch") as f:
    switch_commands = f.read().splitlines()

with open("commands_file_router") as f:
    router_commands = f.read().splitlines()

with open("devices_file") as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    print(f"Connecting to {devices}")
    ip_address_of_device = devices
    node_template = {
        "device_type": "cisco_ios",
        "ip": ip_address_of_device,
        "username": username,
        "password": password
    }

    try:
        netmiko_connect = ConnectHandler(**node_template)
    except (NetmikoAuthenticationException):
        print(f"Authentication failure: {ip_address_of_device}")
        continue
    except (NetmikoTimeoutException):
        print(f"Timeout to device: {ip_address_of_device}")
        continue
    except (EOFError):
        print(f"End of file while attempting device {ip_address_of_device}")
        continue
    except (SSHException):
        print(
            f"SSH Issue. Are you sure SSH is enabled? {ip_address_of_device}")
        continue
    except Exception as unknown_error:
        print(f"Some other error: {str(unknown_error)}")
        continue

    # list of ios versions
    ios_versions = [
        "I86BI_LINUXL2-IPBASEK9-M",
        "I86BI_LINUX-ADVENTERPRISEK9-M)"
    ]

    # for loop to check devices software versions
    for version in ios_versions:
        print(f"Checking for {version}")
        checker = netmiko_connect.send_command("show version")
        int_version = 0
        # checks for version and places in variable
        int_version = checker.find(version)
        if int_version > 0:  # if variable has a version then a matching version has been found
            print(f"Software version found: {version}")
            break
        else:
            print(f"Did not find: {version}")

    # based on what IOS version is found, different commands are applied
    if version == "I86BI_LINUXL2-IPBASEK9-M":  # if this L2 switch version is found, switch commands are applied
        print(f"Running {version} commands")
        output = netmiko_connect.send_config_set(switch_commands)
    # if this L3 Router version is found, router commands are applied
    elif version == "I86BI_LINUX-ADVENTERPRISEK9-M)":
        print(f"Running {version} commands")
        output = netmiko_connect.send_config_set(router_commands)
    print(output)
