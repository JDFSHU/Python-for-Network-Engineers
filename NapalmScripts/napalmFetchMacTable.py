import json
from napalm import get_network_driver
# napalm documentation https://napalm.readthedocs.io/en/latest/

driver = get_network_driver("ios")
iou1 = driver("192.168.122.205", "jacob", "cisco")
iou1.open()

iou1_output = iou1.get_mac_address_table()
print(json.dumps(iou1_output, indent=4))

iou1_output = iou1.get_arp_table()
print(json.dumps(iou1_output, indent=4))
