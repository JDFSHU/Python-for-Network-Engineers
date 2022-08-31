from simplecrypt import encrypt, decrypt
from pprint import pprint
from netmiko import ConnectHandler
import json
from time import time
import threading


def read_devices(device_filename):
    # for reference the contents of the file is as follows
    # 192.168.122.205, cisco-ios, IOU1
    # 192.168.122.207, cisco-ios, IOU3
    # 192.168.122.206, cisco-ios, IOU2

    devices = {}  # dictionary to store device information
    with open(device_filename) as devices_file:
        for device_line in devices_file:
            device_info = device_line.strip().split(
                ",")  # stripping and splitting out commas

            # placing contents of the file into dictionary by slicing
            device = {
                "ipaddr": device_info[0],
                "type": device_info[1],
                "name": device_info[2]
            }
            devices[device["ipaddr"]] = device
    return devices

# function to open a file and decrypt it using a key


def read_device_creds(device_creds_filename, key):

    print("\nGetting Credentials\n")
    with open(device_creds_filename, "rb") as device_creds_file:
        device_creds_json = decrypt(key, device_creds_file.read())

    device_creds_list = json.loads(device_creds_json.decode("utf-8"))
    device_creds = {dev[0]: dev for dev in device_creds_list}
    return device_creds

# function to check for type of device and input show run/show config commands


def config_worker(device, creds):
    if device["type"] == "cisco-ios":
        device_type = "cisco_ios"
    elif device["type"] == "junos-srx":
        device_type = "juniper"
    elif device["type"] == "cisco-xr":
        device_type = "cisco_xr"
    else:
        device_type = "cisco_ios"

    session = ConnectHandler(
        device_type=device_type, ip=device["ipaddr"], username=creds[1], password=creds[2])
    if device_type == "juniper":
        # ---- Use CLI command to get configuration data from device
        print("---- Getting configuration from device")
        session.send_command("configure terminal")
        config_data = session.send_command("show configuration")

    if device_type == "cisco_ios":
        # ---- Use CLI command to get configuration data from device
        print("---- Getting configuration from device")
        config_data = session.send_command("show run")

    if device_type == "cisco_xr":
        # ---- Use CLI command to get configuration data from device
        print("---- Getting configuration from device")
        config_data = session.send_command("show configuration running-config")

    # ---- Write out configuration information to file
    # Important - create unique configuration file name
    config_filename = "config-" + device["ipaddr"]

    print("---- Writing configuration: ", config_filename)
    with open(config_filename, "w") as config_out:
        config_out.write(config_data)

    session.disconnect()
    return


# Main program
devices = read_devices("device_filename")  # file to be read for devices
creds = read_device_creds("encrypted_device_creds",
                          "cisco")  # filename, decryption key

starting_time = time()  # using time to count how long program takes to run

config_threads_list = []

for ipaddr, device in devices.items():
    print('Creating thread for: ', device)
    config_threads_list.append(threading.Thread(
        target=config_worker, args=(device, creds[ipaddr])))

for config_thread in config_threads_list:
    config_thread.start()

for config_thread in config_threads_list:
    config_thread.join()
# calculating time taken
print(
    f"End of Configuration Threading completed, elapsed time: {time()-starting_time}")
