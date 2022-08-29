import json
from napalm import get_network_driver
# napalm documentation https://napalm.readthedocs.io/en/latest/

devices = ["192.168.122.205", "192.168.122.207"]

for ip_address in devices:
    print(f"Connecting to device {ip_address}")
    driver = get_network_driver("ios")
    iosv = driver(ip_address, "jacob", "cisco")
    iosv.open()
    iosv.load_merge_candidate(filename="ACL1.cfg")
    # comparing file contents with the configuration on the device, if there are any differences, dump the contents into variable "differences"
    differences = iosv.compare_config()
    if len(differences) > 0:  # if the differences variable has any contents "greater than 0" then execute the below code
        print(differences)  # print the differences(the missing configurations)
        iosv.commit_config()  # commit the differences as configurations on the device
        print(f"Committing ACL changes on {ip_address}")
    else:
        # else if there are no differences, print the following fString
        print(f"No ACL changes required on {ip_address}")
        iosv.discard_config()  # discard configurations

    iosv.load_merge_candidate(filename="ospf1.cfg")
    # comparing file contents with the configuration on the device, if there are any differences, dump the contents into variable "differences"
    differences = iosv.compare_config()

    if len(differences) > 0:  # if the differences variable has any contents "greater than 0" then execute the below code
        print(differences)  # print the differences(the missing configurations)
        iosv.commit_config()  # commit the differences as configurations on the device
        print(f"Committing OSPF changes on {ip_address}")
    else:
        # else if there are no differences, print the following fString
        print(f"No OSPF changes required on {ip_address}, closing connection")
        iosv.discard_config()  # discard configurations
    iosv.close()  # close connection
