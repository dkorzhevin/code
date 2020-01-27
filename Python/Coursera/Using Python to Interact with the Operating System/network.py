#!/usr/bin/env python3

import requests
import socket

def check_localhost():
	localhost = socket.gethostbyname('localhost')
	if not localhost == '127.0.0.1':
        	#print("False")
		return False
	else:
        	#print("True")
		return True

def check_connectivity():
	request = requests.get("http://www.google.com")
	if not request.status_code == 200:
		#print("False")
		return False
	else:
		#print("True")
		return True

#check_localhost()
#check_connectivity()
