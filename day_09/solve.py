#!/usr/bin/python3

import re, copy, os, sys

lines = []
with open("input.txt", 'r') as fd:
	for line in fd:
		lines.append( line.strip("\r\n") )

#
# Part 1
#

print("\nPart 1:")

data = []
toto = 0

for l in lines:
	data.append( int(l) )


for i in range(25,len(data)):
	x = data[i]
	avail = []

	for j in range(i-25,i):
		for k in range(j,i):
			avail.append( data[j] + data[k] )

	if not x in avail:
		toto = x
		break


print("Result = {}" .format(toto))


#
# Part 2
#

print("\nPart 2:")

toto2 = 0
cnt = 0

for i in range(0,len(data)-1):
	chain = []
	cnt = 0

	for j in range(i,len(data)):
		cnt += data[j]
		chain.append(data[j])

		if cnt < toto: continue
		else: break

	if cnt == toto:
		a = min(chain)
		b = max(chain)
		#print(chain)
		#print("{} {} {}".format(a,b,a+b))
		toto2 = a + b
		break


print("Result = {}" .format(toto2))
