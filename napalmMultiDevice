import json
from napalm import get_network_driver
# napalm documentation https://napalm.readthedocs.io/en/latest/

# list of device IP addresses, can be extended as required
devices = ["192.168.122.205", "192.168.122.206"]

for ip_address in devices:  # for loop to iterate through list of devices
    # simple print statement identifying device connecting too
    print("Connecting to device " + str(ip_address))
    # telling napalm what version of operating system we are using, CISCO IOS in this instance
    driver = get_network_driver("ios")
    # device, username, password for connection parameters
    connect = driver(ip_address, "jacob", "cisco")
    connect.open()  # open the connection

    # apply napalm get_arp_table command to fetch arp tables
    print("\nFetching Arp Tables")
    output = connect.get_arp_table()  # print out arp table in a human readable format
    print(json.dumps(output, indent=4))

    print("\nFetching Interface IP's")
    output = connect.get_interfaces_ip()
    print(json.dumps(output, indent=4))
