#!/usr/bin/python3

import os, sys
import re, copy

lines = []
with open("input.txt", 'r') as fd:
	for line in fd:
		tmp = line.strip("\r\n")
		lines.append( tmp )


#empty = ''
#lines.insert(0, empty)
#lines.append(empty)


#
# Part 1
#

print("\nPart 1:")

ns = 0
ew = 0

# 0=E / 1=S / 2=W / 3=N
facing = 0

for l in lines:
	i = l[0]
	x = int(l[1:])

	if   i == "N": ns += x
	elif i == "S": ns -= x
	elif i == "E": ew += x
	elif i == "W": ew -= x
	elif i == "L":
		if   x ==  90: facing -= 1
		elif x == 180: facing -= 2
		elif x == 270: facing -= 3
		else: print("Oops")
	elif i == "R":
		if   x ==  90: facing += 1
		elif x == 180: facing += 2
		elif x == 270: facing += 3
		else: print("Oops")
	elif i == "F":
		if   facing == 0: ew += x
		elif facing == 1: ns -= x
		elif facing == 2: ew -= x
		elif facing == 3: ns += x

	if   facing < 0: facing += 4
	elif facing > 3: facing -= 4


res = abs(ns) + abs(ew)
print("Result = {}" .format(res))


#
# Part 2
#

print("\nPart 2:")

ns = 0
ew = 0
global wpt_ns
global wpt_ew
wpt_ns = 1
wpt_ew = 10

# 0=E / 1=S / 2=W / 3=N
facing = 0

def rotateLeft90():
	global wpt_ns
	global wpt_ew

	if wpt_ew >= 0:
		# NE -> NW
		if wpt_ns >= 0:
			tmp = wpt_ew
			wpt_ew = -wpt_ns
			wpt_ns = tmp

		# SE -> NE
		elif wpt_ns < 0:
			tmp = wpt_ns
			wpt_ns = wpt_ew
			wpt_ew = -tmp

	elif wpt_ew < 0:
		# NW -> SW
		if wpt_ns >= 0:
			tmp = wpt_ew
			wpt_ew = -wpt_ns
			wpt_ns = tmp
		# SW -> SE
		elif wpt_ns < 0:
			tmp = wpt_ew
			wpt_ew = -wpt_ns
			wpt_ns = tmp


#print("{:3d} {:+02d} {:+02d}".format(0, wpt_ns,wpt_ew))
#
#rotateLeft90()
#print("{:3d} {:+02d} {:+02d}".format(90, wpt_ns,wpt_ew))
#
#rotateLeft90()
#print("{:3d} {:+02d} {:+02d}".format(180, wpt_ns,wpt_ew))
#
#rotateLeft90()
#print("{:3d} {:+02d} {:+02d}".format(270, wpt_ns,wpt_ew))
#
#rotateLeft90()
#print("{:3d} {:+02d} {:+02d}".format(360,wpt_ns,wpt_ew))
#
#if wpt_ns !=  1: print("Error NS")
#if wpt_ew != 10: print("Error EW")
#
#quit()


for l in lines:
	i = l[0]
	x = int(l[1:])

	if   i == "N": wpt_ns += x
	elif i == "S": wpt_ns -= x
	elif i == "E": wpt_ew += x
	elif i == "W": wpt_ew -= x

	elif i == "L":
		if x == 90:
			rotateLeft90()
		elif x == 180:
			wpt_ns = -wpt_ns
			wpt_ew = -wpt_ew
		elif x == 270:
			rotateLeft90()
			rotateLeft90()
			rotateLeft90()
		else:
			print("Oops")

	elif i == "R":
		if   x ==  90:
			rotateLeft90()
			rotateLeft90()
			rotateLeft90()
		elif x == 180:
			wpt_ns = -wpt_ns
			wpt_ew = -wpt_ew
		elif x == 270:
			rotateLeft90()
		else:
			print("Oops")

	elif i == "F":
		for n in range(x):
			ns += wpt_ns
			ew += wpt_ew

	if   facing < 0: facing += 4
	elif facing > 3: facing -= 4



for l in lines:
	pass


res = abs(ns) + abs(ew)
print("Result = {}" .format(res))




# Newline for sublime text
print('')
