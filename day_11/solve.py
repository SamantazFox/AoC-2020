#!/usr/bin/python3

import re, copy, os, sys

lines = []

with open("input.txt", 'r') as fd:
	for line in fd:
		tmp = line.strip("\r\n")
		lines.append( '.' + tmp + '.' )


empty = lines[0].replace('#','.').replace('L','.')
lines.insert(0, empty)
lines.append(empty)


#
# Part 1
#

print("\nPart 1:")

def isFree(x):
	if x == "L" or x == ".": return True
	return False


def round(lst):
	out = [l for l in lst]

	for i in range( 1, len(lst)-1 ):

		newrow = ""

		for j in range( 1, len(lst[i])-1 ):

			if lst[i][j] == '.':
				newrow += '.'
				continue

			#occupied?
			free = 0

			# TL
			if isFree( lst[i-1][j-1] ): free += 1
			# TM
			if isFree( lst[i-1][j] ): free += 1
			# TR
			if isFree( lst[i-1][j+1] ): free += 1

			# LM
			if isFree( lst[i][j-1] ): free += 1
			# RM
			if isFree( lst[i][j+1] ): free += 1


			# BL
			if isFree( lst[i+1][j-1] ): free += 1
			# BM
			if isFree( lst[i+1][j] ): free += 1
			# BR
			if isFree( lst[i+1][j+1] ): free += 1


			if lst[i][j] == "L":
				if free == 8: newrow += "#"
				else: newrow += 'L'

			elif lst[i][j] == "#":
				if free < 5: newrow += "L"
				else: newrow += '#'


		out[i] = '.' + newrow + '.'


	#for l in out: print(l)
	return out



prev = lines

while True:
	x = round(prev)
	if x == prev:
		break
	else:
		prev = [ l for l in x ]

c = 0
for l in prev:
	for i in range(len(l)):
		if l[i] == '#': c += 1


res = c
print("Result = {}" .format(res))


#
# Part 2
#

print("\nPart 2:")


def isOccup(lst, x, y, dx, dy):

	pos_x = x
	pos_y = y

	while pos_x>0 and pos_y>0 and pos_x<(len(lst)-1) and pos_y<(len(lst[0])-1):
		pos_x += dx
		pos_y += dy

		if lst[pos_x][pos_y] == '#':
			return True
		elif lst[pos_x][pos_y] == 'L':
			return False

	return False


def round2(lst):
	out = [l for l in lst]

	for i in range( 1, len(lst)-1 ):

		newrow = ""

		for j in range( 1, len(lst[i])-1 ):

			if lst[i][j] == '.':
				newrow += '.'
				continue

			#occupied?
			ocp = 0

			if isOccup(lst, i, j, -1, -1): ocp += 1 # TL
			if isOccup(lst, i, j, -1,  0): ocp += 1 # TM
			if isOccup(lst, i, j, -1, +1): ocp += 1 # TR

			if isOccup(lst, i, j, 0, -1): ocp += 1 # LM
			if isOccup(lst, i, j, 0, +1): ocp += 1 # RM

			if isOccup(lst, i, j, +1, -1): ocp += 1 # BL
			if isOccup(lst, i, j, +1,  0): ocp += 1 # BM
			if isOccup(lst, i, j, +1, +1): ocp += 1 # BR


			if lst[i][j] == "L":
				if ocp == 0: newrow += "#"
				else: newrow += 'L'

			elif lst[i][j] == "#":
				if ocp >= 5: newrow += "L"
				else: newrow += '#'


		out[i] = '.' + newrow + '.'


	#for l in out: print(l)
	return out


prev2 = lines
while True:
	x2 = round2(prev2)
	if x2 == prev2:
		break
	else:
		prev2 = [ l for l in x2 ]

c2 = 0
for l in prev2:
	for i in range(len(l)):
		if l[i] == '#': c2 += 1



res = c2
print("Result = {}" .format(res))




# Newline for sublime text
print('')
