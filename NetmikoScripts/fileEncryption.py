from simplecrypt import encrypt, decrypt
from pprint import pprint
import csv
import json

file_to_encrypt = "device_creds"
key = "cisco"

with open(file_to_encrypt, "r") as dc_in:
    device_creds_reader = csv.reader(dc_in)
    device_creds_list = [device for device in device_creds_reader]

print(device_creds_list)

# Encrypting the device credentials using key
encrypted_file = "encrypted_device_creds"
with open(encrypted_file, "wb") as dc_out:
    dc_out.write(encrypt(key, json.dumps(device_creds_list)))
print("file encrypted successfully")

print("\n Getting Credentials \n")
with open(encrypted_file, "rb") as device_creds_file:
    device_creds_json = decrypt(key, device_creds_file.read())

device_creds_list = json.loads(device_creds_json.decode("utf-8"))
print(device_creds_list)

print("\n ConfirmL device_creds json in ")

device_creds = {dev[0]: dev for dev in device_creds_list}
pprint(device_creds)
