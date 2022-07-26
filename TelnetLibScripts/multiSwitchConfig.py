import telnetlib
import getpass
# telnetlib documentation https://docs.python.org/3/library/telnetlib.html

HOST = "localhost"
user = input("Enter your username: ")
password = getpass.getpass()

f = open("switches")

for IP in f:
    IP = IP.strip()
    print("Configuring Switch " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"conf t\n")
    for n in range(2, 9):
        tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
        tn.write(b"name python_VLAN_" + str(n).encode('ascii') + b"\n")
    tn.write(b"end\n")
    tn.write(b"write\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))
