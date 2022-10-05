from asyncore import read
import telnetlib
import getpass
from datetime import date
# telnetlib documentation https://docs.python.org/3/library/telnetlib.html

today = date.today()
HOST = "192.168.122.122"  # Device IP address goes here

# will prompt upon script being ran, enter local username and passwords to access device via telnet
user = input("Enter Username: ")
password = input("Enter Password: ")

# telnet library connecting to host
tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode("ascii") + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")

# each tn.write line will write the command in quotes to the device. * must be prepended with a b to specify bytes type.
tn.write(b"enable\n")
tn.write(b"cisco\n")  # put your enable mode password in here
# enables the device to print the full running config to the terminal without paging
tn.write(b"terminal length 0\n")
tn.write(b"show run\n")
tn.write(b"exit\n")

readOutput = tn.read_all()  # reads everything the script has output
# saves to file consisting of (IP) Running Config (Todays Date)
saveOutput = open(f"{HOST} Running Config {today}", "w")
saveOutput.write(readOutput.decode("ascii"))
saveOutput.write("\n")
saveOutput.close
