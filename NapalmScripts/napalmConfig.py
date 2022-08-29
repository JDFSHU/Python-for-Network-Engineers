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
iou1.commit_config()  # committing the file lines as configurations
print(f"{device} configured, closing connection")
iou1.close()  # closing connection
