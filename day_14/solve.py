#!/usr/bin/python3

import os, sys
import re, copy
import math


lines = []
with open("input.txt", 'r') as fd:
	for line in fd:
		tmp = line.strip("\r\n")
		lines.append( tmp )


#
# Part 1
#

print("\nPart 1:")


memory = {}
mask = ""

for l in lines:
	tmp = l.replace(' = ','=').split('=')

	code = tmp[0]
	data = tmp[1]

	if code == "mask":
		mask = data

	else:
		if code[0:3] == "mem":
			loc = int(code[4:-1])
			x = "{:036b}".format(int(data))
			#print('a  ', c, mask, len(mask))

			if mask == "":
				print("Error!")

			elif len(mask) != len(x):
				print(len(mask), len(x))
				print(' ')
				quit()


			else:
				for i in range(len(mask)):

					if mask[i] == '0' or mask[i] == '1':
						if   i ==  0: y = mask[i] + x[1:]
						elif i == 35: y = x[:-1] + mask[i]
						else:         y = x[:i] + mask[i] + x[i+1:]
						x = y
					else:
						pass
						#print("OOps ?")

			memory[loc] = x

		else:
			print("OOps ?")


total = 0
for i in memory:
	total += int('0b' + memory[i], 2)


res = total
print("Result = {}" .format(res))


#
# Part 2
#

print("\nPart 2:")

def incrementBuf(buf):
	i = len(buf) - 1
	while i >= 0:
		if i == len(buf) - 1: buf[i] += 1

		if buf[i] == 2 and (i-1) >= 0:
			buf[i-1] += 1
			buf[i] = 0

		i -= 1
	return buf

def replaceBits(var, buf):
	#print(var)
	#print(buf)

	x = len(buf) - 1
	for i in range(len(var)-1, -1, -1):
		if var[i] == 'X':
			n = '1' if buf[x] else '0'

			if   i ==  0: y = n + var[1:]
			elif i == 35: y = var[:-1] + n
			else:         y = var[:i] + n + var[i+1:]

			var = y
			x -= 1

	return var


def genAllStuff(var):
	out = []
	xes = 0

	for i in range(len(var)):
		if var[i] == 'X': xes += 1

	# bits buffer
	buf = [ 0 for x in range(xes) ]

	while 0 in buf:
		out.append( replaceBits(var, buf) )
		buf = incrementBuf(buf)

	out.append( replaceBits(var, buf) )
	return out



memory2 = {}
mask2 = ""

for l in lines:
	tmp = l.replace(' = ','=').split('=')

	code = tmp[0]
	data = tmp[1]

	if code == "mask":
		mask2 = data

	else:
		if code[0:3] == "mem":
			loc = "{:036b}".format(int(code[4:-1]))
			x = int(data)

			if mask2 == "":
				print("Error!")
			else:
				for i in range(len(mask2)):
					if mask2[i] == 'X' or mask2[i] == '1':
						if   i ==  0: y = mask2[i] + loc[1:]
						elif i == 35: y = loc[:-1] + mask2[i]
						else:         y = loc[:i] + mask2[i] + loc[i+1:]
						loc = y

			for n in genAllStuff(loc):
				addr = int('0b' + n, 2)
				memory2[addr] = x

		else:
			print("OOps ?")


total2 = 0
for m in memory2:
	total2 += memory2[m]


#print(memory2)

res = total2
print("Result = {}" .format(res))




# Newline for sublime text
print('')

