import getpass
import telnetlib
# telnetlib documentation https://docs.python.org/3/library/telnetlib.html

HOST = "10.0.0.1"
user = input("Enter username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"ccna\n")
tn.write(b"conf t\n")
tn.write(b"int e0/1\n")
tn.write(b"ip address dhcp\n")
tn.write(b"no shut\n")
tn.write(b"ip nat outside\n")
tn.write(b"int e0/0\n")
tn.write(b"ip nat inside\n")
tn.write(b"exit\n")
tn.write(b"access-list 1 permit 10.0.0.0 0.0.0.255 \n")
tn.write(b"ip nat inside source list 1 interface e0/1 overload \n")
tn.write(b"ip dhcp excluded-address 10.0.0.0 10.0.0.10\n")
tn.write(b"ip dhcp pool DHCP \n")
tn.write(b"network 10.0.0.0 255.255.255.0\n")
tn.write(b"dns-server 8.8.8.8\n")
tn.write(b"default-router 10.0.0.1\n")
tn.write(b"end\n")
tn.write(b"write\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
