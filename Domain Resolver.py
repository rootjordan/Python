import socket
import sys

"""
Need python 2.7
"""

if len(sys.argv) != 1:
	print "[#] Usage: python [filename.py]"
	sys.exit()
try:
	print "[#] Creating Socket"
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print "[#] Unable to open socket, please try again"
	sys.exit()

print "[#] Socket created"
print "[#] Loading shell"
print "[#] Commands"
print "[#] Exit = exit"
print "[#] Resolver ip = [Hostname]"

while True:
	shell = raw_input("Enter Host > ")
	if shell == "exit":
		sys.exit()
	if len(shell) > 50:
		print "[#] Please enter vaild hostname"
	try:
		GrabIp = socket.gethostbyname(shell)
	except socket.gaierror:
		print "\n[#] Unable to get ip address please try again.\n"
		continue
	print "\nHostname: " + shell + "\nIp: " + GrabIp
