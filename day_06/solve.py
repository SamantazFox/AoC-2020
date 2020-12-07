#!/usr/bin/python3

import re, os, sys

lines = []
with open("input.txt", 'r') as fd:
	for line in fd:
		lines.append( line.strip("\r\n") )

lines.append('')


#
# Part 1
#

print("\nPart 1:")

groups = []
replies = 0
peeps = 0
current = {}

for l in lines:
	# Code
	if l == '':
		tmp = {}
		tmp['data'] = current
		tmp['count'] = len(current)
		tmp['pers'] = peeps

		replies += tmp['count']
		groups.append(tmp)

		current = {}
		peeps = 0

	else:
		peeps += 1
		for i in range(0,len(l)):
			n = l[i]
			if n not in current: current[n] = 0
			current[n] += 1


print("Result = {}" .format(replies))


#
# Part 2
#

print("\nPart 2:")

total = 0
for g in groups:
	count = 0
	for field in g['data']:
		if g['data'][field] == g['pers']:
			count += 1
	total += count

print("Result = {}" .format(total))
