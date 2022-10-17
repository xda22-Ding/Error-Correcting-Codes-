import sys
import os
import struct
import subprocess



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

inp = sys.argv[1]
bitarr = strToBit(inp)
parity = bitstoparity(bitarr)
correct_parity = ''
for i in range(len(parity)):
		correct_parity = correct_parity + str(parity[i])
print(correct_parity)
