import os
import subprocess

address = "192.168.86."

# Below we are:
#	Using check_output to execute the host command. Host info is returned in byte format
#	Using decode to decode byte format into UTF-8
#	Using split to split the text at "pointer"
#	Using [1] to get the second element of the split
#	Using replace to remove the end of the split value
#	Using strip to trim spaces

hostname = (subprocess.check_output(["host",address]).decode("UTF-8").split("pointer"))[1].replace('.lan.\n',"").strip()

print("Checking if "  + hostname + " is online...")

# Below we use the netcat command to check the host on UDP port 80

response = os.system("nc -vnzu " + address + " 80 > /dev/null 2>&1")
if response == 0:
	strState = hostname + " is online!"
else:
	strState =  hostname + " is offline."
print(strState)