from asyncore import read
import telnetlib
from datetime import date
# telnetlib documentation https://docs.python.org/3/library/telnetlib.html

# guide to use python3 scripts in linux
# step 1: navigate to a memorable folder where you will store the script (good examples would be home directory or /usr/local/bin)
# step 2: create a new text file by using command touch filename.py e.g touch script.py
# step 3: change the permisions on the file so that it is able to be executed with command sudo chmod +x script.py
# step 4: copy and paste the below script into the file by using nano or vi/vim depending on what text editor you have installed on your server (right click inside the window to paste)
# step 5: ensure the HOST and tn.write(b"cisco\n") lines 15 and 32 match your switch/lab
# step 6: run script by using command python3 script.py

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
