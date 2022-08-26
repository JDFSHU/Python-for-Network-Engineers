import json
from napalm import get_network_driver
# napalm documentation https://napalm.readthedocs.io/en/latest/

driver = get_network_driver("ios")
device = "192.168.122.205"
iou1 = driver(device, "jacob", "cisco")
iou1.open()

print(f"Accessing {device}")
# loading a file a configurations
iou1.load_merge_candidate(filename="ACL1.cfg")

# comparing file contents with the configuration on the device, if there are any differences, dump the contents into variable "differences"
differences = iou1.compare_config()
if len(differences) > 0:  # if the differences variable has any contents "greater than 0" then execute the below code
    print(differences)  # print the differences(the missing configurations)
    iou1.commit_config()  # commit the differences as configurations on the device
    print(f"Committing changes on {device}")
else:
    # else if there are no differences, print the following fString
    print(f"No changes required on {device}, closing connection")
    iou1.discard_config()  # discard configurations
iou1.close()  # close connection
