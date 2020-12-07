#!/usr/bin/python3

import re, sys, os

lines = []
with open("input.txt", 'r') as fd:
	for line in fd:
		lines.append( line.strip("\r\n") )

#
# Part 1
#

print("\nPart 1:")

look = [64,32,16,8,4,2,1]
idents = []

for l in lines:
	# Code
	row = 0
	col = 0
	rng1 = [0, 127]
	rng2 = [0, 7]
	pas1 = 0
	pas2 = 4

	for i in range(0,len(l)):
		x = l[i]
		if x == 'F':
			rng1[1] -= look[pas1]
			pas1 += 1
		elif x == 'B':
			rng1[0] += look[pas1]
			pas1 += 1

		elif x == 'L':
			rng2[1] -= look[pas2]
			pas2 += 1
		elif x == 'R':
			rng2[0] += look[pas2]
			pas2 += 1

	row = rng1[0]
	col = rng2[0]


	idt = row*8 + col
	idents.append(idt)
	print("row = {} / col = {} / idt = {}".format(row, col, idt))


print("Result = {}" .format(
	max(idents)
	))


#
# Part 2
#

print("\nPart 2:")

for i in range(1, 126):
	for j in range(0, 8):
		idtst = i*8 + j

		if idtst in idents: continue
		else: print(idtst)
