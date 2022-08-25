import json
from napalm import get_network_driver
# napalm documentation https://napalm.readthedocs.io/en/latest/


# Use the appropriate network driver to connect to the device, in this case Cisco IOS
driver = get_network_driver("ios")
# Connect using hostname, username, password: optional arguments are possible such as port numbers
iou1 = driver("192.168.122.205", "jacob", "cisco")
iou1.open()  # opening connection

# applying napalm command to sw1 and then dumping the ouput into a variable
# get facts is one of many napalm commands, shows basic device information
iou1_output = iou1.get_facts()
# indent value allows the output to be formatted nicely for easier readability
print(json.dumps(iou1_output, indent=4))

# get interfaces shows interface information such as mac address, enabled, up/down status, MTU, speed etc
iou1_output = iou1.get_interfaces()
# sort_keys = True tells the encoder to return the JSON object keys in a sorted order for easier readability
print(json.dumps(iou1_output, sort_keys=True, indent=4))

# get interfaces counters shows traffic information such as broadcasts, multicasts, errors etc
iou1_output = iou1.get_interfaces_counters()
print(json.dumps(iou1_output, indent=4))

# get interfaces ip shows interfaces with IP addresses
iou1_output = iou1.get_interfaces_ip()
print(json.dumps(iou1_output, indent=4))

# for key, value in iou1_output.items(): # prints out the output of the get_facts() command line by line instead of a jumbled mess
#    print(key, ":", value)
