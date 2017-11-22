import random
import os
import re
import socket
import sys
import netmiko
import time
from getpass import getpass



	
def read_doc (file_name):

	for line in open(file_name, 'r').readlines():
		line = remove_return(line)
		temp_ip = get_ip (line)
		for ip in temp_ip:
			ip = ip	
		line = line.split(',')
		ios = line[2]
		
		device = [ip,ios]
		devices.append(device)	
devices = []

def get_ip (input):
	return(re.findall(r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', input))

def remove_return(entry):
	return entry.rstrip('\n')
def remove_bracket(entry):
	entry =  entry.strip(']')
	return entry.strip('[')

def to_doc(file_name, varable):
	f=open(file_name, 'a')
	f.write(varable)
	f.write('\n')
	f.close()	

read_doc("IPs.csv")
your_user_name = input("Username: ")
your_password = getpass()	

for device in devices:
	ip = device[0]
	ios = device[1]

	try:
		net_connect = netmiko.ConnectHandler(device_type='cisco_ios', ip=ip, username=your_user_name, password=your_password)
		command = "show ver | i .bin"
		output = net_connect.send_command_expect(command)
		ios_start = output.find(":")
		output = output[ios_start+1:]
		if device[1] in output:
			print (ip + " " + ios+" in output SUCCESS!")
			doc_out_success = ip +","+ "SUCCESS"+","+ 'Running'+","+ output+","+"should have"+","+ios+"\n"
			to_doc('results.csv', doc_out_success)
		else:
			print (ip + " " +  output + " doesn't have "+ios+ " in it... FAIL!!!")
			doc_out_fail = ip +","+ "FAIL"+","+ 'Running'+","+ output+","+"should have"+","+ios+"\n"
			to_doc('results.csv', doc_out_fail)
	except:
		cant_ssh = ip + ",FAIL, I can't SSH to " + ip+"\n"
		print (cant_ssh)
		to_doc('results.csv', cant_ssh)
		
	