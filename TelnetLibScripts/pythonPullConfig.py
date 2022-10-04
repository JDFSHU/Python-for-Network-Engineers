from asyncore import read
import telnetlib
import getpass
from datetime import date
# telnetlib documentation https://docs.python.org/3/library/telnetlib.html

HOST = "10.0.0.1"
user = input("Enter Username: ")
password = getpass.getpass()
today = date.today()

tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode("ascii") + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")

tn.write(b"enable\n")
tn.write(password + b"\n")
tn.write(b"terminal length 0\n")
tn.write(b"show run\n")
tn.write(b"exit\n")

readOutput = tn.read_all()
saveOutput = open(f"{HOST} Running Config {today}", "w")
saveOutput.write(readOutput.decode("ascii"))
saveOutput.write("\n")
saveOutput.close
