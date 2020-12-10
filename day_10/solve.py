#!/usr/bin/python3

import re, copy, os, sys

lines = []
with open("input.txt", 'r') as fd:
	for line in fd:
		x = line.strip("\r\n")
		lines.append( int(x) )

#
# Part 1
#

print("\nPart 1:")

device = max(lines) + 3
lst = sorted(lines)

spaces = [0,0,0,0,0,0,0,0,0]


for i in range(1,len(lst)):
	n = lst[i] - lst[i-1]
	spaces[n] += 1


spaces[1] += 1
spaces[3] += 1

res = spaces[1] * spaces[3]
print("Result = {}" .format(res))


#
# Part 2
#

print("\nPart 2:")

#first = max(lines)
last = max(lines)

total = 0
known = [-1 for i in range(max(lst) +1)]

def branch(begin, r):
	ways = 0

	#print(' '*r + '- ' + str(begin))

	if known[begin] != -1:
		#print(' '*r + str(begin) + '=' + str(known[begin]) + ' [LOAD]')
		return known[begin]

	if (begin == last):
		#print(' '*r + str(begin) + ' [END]')
		ways += 1


	if (begin+1 in lst): ways += branch(begin+1, r+1)
	if (begin+2 in lst): ways += branch(begin+2, r+1)
	if (begin+3 in lst): ways += branch(begin+3, r+1)


	#print(' '*r + str(begin) + '=' + str(ways) + ' [SAVE]')
	known[begin] = ways

	return ways


res = branch(0,0)
print("Result = {}" .format(res))



# Newline for Sublime text
print('')
