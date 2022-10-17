import sys
import os
import struct
import subprocess

def checkParity(datastr):
	result = subprocess.check_output(['python3','a3a.py', datastr])
	out = []
	for i in range(len(result)):
		if(result[i] == 49 or result[i] == 48):
			out.append(result[i]-48)
	return out


def numError(parity,strParity):
	countError = 0
	for i in range(len(parity)):
		if(int(parity[i]) != strParity[i]):
			countError = countError + 1
	return countError


def strToBit(string):
	res = ''.join(format(i, '08b') for i in bytearray(string, encoding ='ascii'))
	return res



def createH(bitarr):
	dataLength = len(bitarr)
	numberParity = 1
	indexDatabit = 0
	newbitarr = []

	while indexDatabit < dataLength:
		newbitarr.append("p")#set each p the default 0
		templength = 2**(numberParity-1)-1
		for j in range(templength):
			if(indexDatabit+j == dataLength):
				break
			newbitarr.append(bitarr[indexDatabit+j])
		numberParity = numberParity + 1
		indexDatabit = indexDatabit + templength
	return newbitarr


def binaryInt(x):
	binx = format(x, "b")
	return binx

def createM(H,i):
	M = []
	for k in range(H+1):
		if(len(binaryInt(k)) >= i):
			if(binaryInt(k)[-i] == "1"):
				M.append(k)
	return M

def createAllM(numberParity,H):
	mat = []
	for i in range(numberParity):
		mat.append(createM(H,i+1))
	return mat


def calpi(i,mat,newbitarr):
	p1 = 0
	for j in mat[i][1:]:
		p1 = p1 ^ int(newbitarr[j-1])
	return p1

def outputParity(mat,numberParity,newbitarr):
	parity = []
	for i in range(numberParity):
		parity.append(calpi(i,mat,newbitarr))
	return parity

def bitstoparity(bitarr):
	newbitarr = createH(bitarr)
	lengthH = len(newbitarr)
	numberParity = lengthH - len(bitarr)
	mat = createAllM(numberParity,lengthH)
	return outputParity(mat,numberParity,newbitarr)


def checkTwoParity(parity1,parity2):
	flag = True
	for i in range(len(parity)):
		if(int(parity1[i]) != int(parity2[i])):
			flag = False
	return flag

def allstringS(altDataBit):
	#print("the length of altDataBit is",len(altDataBit))
	for j in range(len(altDataBit)):
		s = ''.join(altDataBit[j])
		correct_string = ''
		for i in range(int(len(s)/8)):
			correct_string = correct_string + "".join([chr(int(s[8*i:8*i+8], 2))])
		print(parity)
		print(correct_string)


inputstr = sys.argv[2]
parity = sys.argv[1]
strParity = checkParity(inputstr)
numoferror = numError(parity,strParity)

if(numoferror==0):
	print(parity)
	print(inputstr)
if(numoferror==1):
	correct_parity = ''
	for i in range(len(strParity)):
		correct_parity = correct_parity + str(strParity[i])
	print(correct_parity)
	print(inputstr)

if(numoferror>1):
	inputbit = strToBit(inputstr)

	newinputbit = list(inputbit)
     
	altDataBit = []
	for i in range(len(inputbit)):
		newinputbit = list(inputbit)
		newinputbit[i] = str(int(inputbit[i])^ 1)

		if(checkTwoParity(bitstoparity(''.join(newinputbit)),parity) == True):
			altDataBit.append(newinputbit)

		
	
	s = ''.join(altDataBit[0])

	correct_string = ''
	for i in range(int(len(s)/8)):
		correct_string = correct_string + "".join([chr(int(s[8*i:8*i+8], 2))])


	allstringS(altDataBit)








