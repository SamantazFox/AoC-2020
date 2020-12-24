#!/usr/bin/python3

import os, sys
import re, copy
import math


lines = []
with open("input.txt", 'r') as fd:
	for line in fd:
		tmp = line.strip("\r\n")
		lines.append( tmp )

paths = []

for l in lines:
	x = re.finditer(r'(e|se|sw|w|nw|ne)', l)
	if not x: print("Error:", l)

	tmp = [ y.expand(r'\1') for y in x ]
	paths.append(tmp)


#
# Part 1
#

print("\nPart 1:")

tiles = {}

for p in paths:
	x = 0
	y = 0

	for way in p:
		# N is y- / S is y+
		# W is x- / E is x+
		if   way ==  'e': x,y = x+2, y
		elif way ==  'w': x,y = x-2, y
		elif way == 'se': x,y = x+1, y+1
		elif way == 'sw': x,y = x-1, y+1
		elif way == 'ne': x,y = x+1, y-1
		elif way == 'nw': x,y = x-1, y-1

	if (x,y) not in tiles: tiles[(x,y)] = 1
	else: tiles[(x,y)] += 1


res = 0
for t in tiles:
	#print(t, ':', tiles[t])
	if tiles[t]%2 == 1: res += 1

print("Result = {}" .format(res))


#
# Part 2
#

print("\nPart 2:")

#tiles = {}


def neightbors_to_add(lst, x,y):
	pos_e  = (x+2, y  )
	pos_w  = (x-2, y  )
	pos_se = (x+1, y+1)
	pos_sw = (x-1, y+1)
	pos_ne = (x+1, y-1)
	pos_nw = (x-1, y-1)

	out = []
	for n in [pos_e,pos_w,pos_se,pos_sw,pos_ne,pos_nw]:
		if n not in lst:
			out.append(n)

	return out


def neightbors(lst, x,y):
	pos_e  = (x+2, y  )
	pos_w  = (x-2, y  )
	pos_se = (x+1, y+1)
	pos_sw = (x-1, y+1)
	pos_ne = (x+1, y-1)
	pos_nw = (x-1, y-1)

	count = 0
	if pos_e  in lst and (lst[pos_e]%2)  == 1: count += 1
	if pos_w  in lst and (lst[pos_w]%2)  == 1: count += 1
	if pos_se in lst and (lst[pos_se]%2) == 1: count += 1
	if pos_sw in lst and (lst[pos_sw]%2) == 1: count += 1
	if pos_ne in lst and (lst[pos_ne]%2) == 1: count += 1
	if pos_nw in lst and (lst[pos_nw]%2) == 1: count += 1
	return count


def must_flip(lst, pos):
	# Black => Flipped an odd number of times
	isblack = bool( pos in lst and (lst[pos]%2) == 1 )
	iswhite = bool( not isblack )

	black_nb = neightbors(tiles_list, pos[0], pos[1])

	if isblack and (black_nb == 0 or black_nb > 2):
		return True

	elif iswhite and black_nb == 2:
		return True

	else:
		return False



def day(tiles_list):
	new_list = {}

	for pos in tiles_list:


		# Flip or keep current value
		if must_flip(tiles_list, pos): new_list[pos] = tiles_list[pos] + 1
		else: new_list[pos] = tiles_list[pos]

		# Make sure to check white neightbors not in list, too
		not_in_list = neightbors_to_add(tiles_list, pos[0], pos[1])

		if not_in_list != []:
			for n in not_in_list:
				if must_flip(tiles_list, n):
					if n not in new_list:
						new_list[n] = 1

	return new_list



def print_tile(tiles_list):
	pattern_1 = ' \\'
	pattern_2 = ' |'
	pattern_3 = ' /'

	for x in range (-13,14): print(' /\\ ', end='')
	print()

	for y in range (-9,11):

		offset  = bool((y+9) % 2 == 1)

		if offset: print(pattern_1, end='')
		for x in range (-13,14):
			if (x,y) in tiles_list and (tiles_list[(x,y)]%2) == 1:
				if x == 0 and y == 0:
					print('/0 \\', end='')
				else:
					print('/  \\', end='')
			else:
				if x == 0 and y == 0:
					print('/0#\\', end='')
				else:
					print('/##\\', end='')
		print()

		if offset: print(pattern_2, end='')
		for x in range (-13,14):
			if (x,y) in tiles_list and (tiles_list[(x,y)]%2) == 1:
				if x == 0 and y == 0:
					print('| 0|', end='')
				else:
					print('|  |', end='')
			else:
				if x == 0 and y == 0:
					print('|#0|' , end='')
				else:
					print('|##|' , end='')
		print()

		if offset: print(pattern_3, end='')
		for x in range (-13,14):
			if (x,y) in tiles_list and (tiles_list[(x,y)]%2) == 1:
				if x == 0 and y == 0:
					print('\\0 /', end='')
				else:
					print('\\  /', end='')
			else:
				if x == 0 and y == 0:
					print('\\0#/', end='')
				else:
					print('\\##/', end='')
		print()



#print('Day 0: {}'.format(tiles))
#print_tile(tiles)
#print()

tiles_list = tiles


for d in range(1, 101):
	new_list = day(tiles_list)
	tiles_list = new_list
	# print ('Day {}: {}'.format(d, tiles_list))

	res_day = 0
	for t in tiles_list:
		isblack = (tiles_list[t]%2) == 1
		if isblack: res_day += 1

	#print_tile(new_list)
	#print('Day {}: total = {}'.format(d, res_day))
	#print()



res = 0
for t in tiles_list:
	#print(t, ':', tiles[t])
	if (tiles_list[t]%2) == 1: res += 1


print("Result = {}" .format(res))




# Newline for sublime text
print('')

