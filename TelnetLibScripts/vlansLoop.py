import telnetlib
import getpass
# telnetlib documentation https://docs.python.org/3/library/telnetlib.html

HOST = "10.0.0.2"
user = input("Enter username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")

# loop to create vlans 2 - 10 on a switch and name them
for n in range(2, 11):
    tn.write(b"vlan " + str(n).encode("ascii") + b"\n")
    # writing vlan + value of n as a string
    tn.write(b"name python_VLAN_" + str(n).encode("ascii") + b"\n")
    # naming vlan by adding name + n as a string at the end
tn.write(b"end\n")
tn.write(b"write\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
