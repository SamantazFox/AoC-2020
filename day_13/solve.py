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

ts = int(lines[0])
bus = lines[1].split(',')
lin = []

for b in bus:
	x = 0

	if b == 'x':
		lin.append(999999999)
		continue

	while x < ts:
		x += int(b)

	lin.append(x)


mini = min(lin)
idx = 0

for i,l in enumerate(lin):
	if l == mini:
		idx = bus[i]
		break


res = (mini - ts) * int(idx)
print("Result = {}" .format(res))


#
# Part 2
#

print("\nPart 2:")


#busses = "17,x,13,19"         # 3417
#busses = "67,7,59,61"         # 754018
#busses = "67,x,7,59,61"       # 779210
#busses = "67,7,x,59,61"       # 1261476
#busses = "1789,37,47,1889"    # 1202161486
busses = lines[1]             # ????


busses = busses.split(',')
offsets = {}

for off, bus in enumerate(busses):
	if bus != 'x':
		offsets[int(bus)] = off

print(offsets)


# Start with the largest ID
bus_id = max(offsets)

# Compute t (noted ts2) from its relative offset
# compute increment (bus ID)
ts2 = bus_id - offsets[bus_id]
inc = bus_id

# Remove this bus ID from the list, we don't need it anymore
del offsets[bus_id]


# For each remaining bus lines
while offsets:
	# Get the new maximum bus ID and its own timestamp
	bus_id = max(offsets)
	bus_ts = ts2 + offsets[bus_id]

	# If modulo 0, we've matched a part of the pattern
	# So we know that this pattern won't change between the busses
	# we already have removed from the list and the current one
	# Otherwise, continue to increment
	if (bus_ts % bus_id) == 0:
		inc *= bus_id
		del offsets[bus_id]
	else:
		ts2 += inc


res = ts2
print("Result = {}" .format(res))




# Newline for sublime text
print('')
