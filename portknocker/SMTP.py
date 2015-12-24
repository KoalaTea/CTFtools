#!/usr/bin/python

import socket


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('104.236.16.36', 3060))

#Connect to the now opened ssh port provide password, seed, and brute force for correct number
print(s.recv(1000))
s.send(b'HELO sb1.cyberskyline.com')
print(s.recv(1000))
s.send(b'MAIL FROM:<user4271@hacker.test>')
print(s.recv(1000))
s.send(b'RCPT TO:<daniel@hacker.test>')
print(s.recv(1000))
s.send(b'DATA')
print(s.recv(1000))
s.send(b'')
s.send(b'')
s.send(b'Subject: -I have the latest exploit-')
print(s.recv(1000))
s.send(b'.')
s.send(b'.')
s.send(b'.')
s.send(b'.')
s.send(b'.')
print(s.recv(1000))
s.send(b'QUIT')
print(s.recv(1000))
print(s.recv(1000))
print(s.recv(1000))
