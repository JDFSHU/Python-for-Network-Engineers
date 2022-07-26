from asyncore import read
import telnetlib
import getpass
# telnetlib documentation https://docs.python.org/3/library/telnetlib.html

user = input("Enter Username: ")
password = getpass.getpass()

f = open("switches")

for IP in f:
    IP = IP.strip()
    print("Backing up Switch: " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode("ascii") + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")

    readOutput = tn.read_all()
    saveOutput = open("Backup Config Switch: " + HOST, "w")
    saveOutput.write(readOutput.decode("ascii"))
    saveOutput.write("\n")
    saveOutput.close
