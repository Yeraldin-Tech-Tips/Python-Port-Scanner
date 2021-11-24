import sys
import socket
from datetime import datetime

#Define target 
if len(sys.argv) == 2:

    #translate hostname to IPV4

    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid arguements")

print(f"Scanning Target {target}")
print(f" Scanning Started at: {datetime.now()}")

#loop through all ports
for port in range(1,65535):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    #Scan target
    results = scanner.connect_ex((target,port))

    if results == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is close")
    scanner.close()