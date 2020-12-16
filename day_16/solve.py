#!/usr/bin/python3

import os, sys
import re, copy
import math


tickets = []
with open("input.txt", 'r') as fd:
	for line in fd:
		tmp = line.strip("\r\n")
		tickets.append( tmp )


rules = {
	'departure_location': [ (25, 863), (882, 957) ],
	'departure_station':  [ (50, 673), (690, 972) ],
	'departure_platform': [ (25, 312), (321, 959) ],
	'departure_track':    [ (48, 337), (358, 971) ],
	'departure_date':     [ (31, 458), (476, 957) ],
	'departure_time':     [ (32, 800), (821, 973) ],
	'arrival_location': [ (34, 502), (528, 951) ],
	'arrival_station':  [ (30, 650), (662, 957) ],
	'arrival_platform': [ (50, 148), (160, 966) ],
	'arrival_track':    [ (27, 572), (587, 969) ],
	'class':    [ (46, 893), (913, 964) ],
	'duration': [ (36, 161), (179, 962) ],
	'price': [ (38, 294), (311, 965) ],
	'route': [ (26, 391), (397, 962) ],
	'row':   [ (28, 111), (122, 967) ],
	'seat':  [ (48,  65), ( 84, 973) ],
	'train': [ (33, 827), (839, 960) ],
	'type':  [ (47, 436), (454, 959) ],
	'wagon': [ (45, 136), (147, 959) ],
	'zone':  [ (36, 252), (275, 957) ]
}

your_ticket = [
179,101,223,107,127,211,191,61,199,193,181,131,89,109,197,59,227,53,103,97
]

fields_count = len(your_ticket)


#
# Part 1
#

print("\nPart 1:")

not_valid = []
tickets_vld = []


def isValidAny(x):
	for r in rules:
		r0 = rules[r][0][0]
		r1 = rules[r][0][1]
		r2 = rules[r][1][0]
		r3 = rules[r][1][1]

		if (x >= r0 and x <= r1) or (x >= r2 and x <= r3):
			return True

	return False

for i,t in enumerate(tickets):
	lst = [ int(x) for x in t.split(',') ]

	vld = True
	for f in lst:
		if not isValidAny(f):
			vld = False
			not_valid.append(f)

	if vld: tickets_vld.append(lst)


res = 0
for i in not_valid: res += i

print("Result = {}" .format(res))


#
# Part 2
#

print("\nPart 2:")

tickets_count = len(tickets_vld)


# General positions
positions = {}
for r in rules: positions[r] = -1


# Def to check single item + rule
def isValidSingle(r, x):
	r0 = rules[r][0][0]
	r1 = rules[r][0][1]
	r2 = rules[r][1][0]
	r3 = rules[r][1][1]

	if (x >= r0 and x <= r1) or (x >= r2 and x <= r3):
		return True

	return False


# Compute positions
posssible = {}

for r in rules:
	posssible[r] = {}

	for i,lst in enumerate(tickets_vld):
		poss_i = []

		for j,x in enumerate(lst):
			# Store indices of valid fields, according to r
			if isValidSingle(r, x): poss_i.append(j)

		posssible[r][i] = poss_i


	posssible[r]['total'] = []

	for i in range(0, fields_count):
		cnt = 0

		for j in range(0, tickets_count):
			if i in posssible[r][j]: cnt += 1

		if cnt == tickets_count:
			posssible[r]['total'].append(i)


# Reorganise / sort data
temp = [ {} for i in range(fields_count) ]
for r in rules:
	lst = posssible[r]['total']
	temp[len(lst) - 1] = { 'rule': r, 'list': lst }


# Assign numbers
known = []
for i in temp:
	r   = i['rule']
	lst = i['list']

	for x in known: lst.remove(x)
	positions[r] = lst[0]
	known.append(lst[0])



res  = 1
res *= your_ticket[positions['departure_location']]
res *= your_ticket[positions['departure_station']]
res *= your_ticket[positions['departure_platform']]
res *= your_ticket[positions['departure_track']]
res *= your_ticket[positions['departure_date']]
res *= your_ticket[positions['departure_time']]

print("Result = {}" .format(res))




# Newline for sublime text
print('')

