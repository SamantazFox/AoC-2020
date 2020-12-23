#!/usr/bin/python3

import os, sys
import re, copy
import math
from array import array
import time


lines = []
with open("input.txt", 'r') as fd:
	for line in fd:
		tmp = line.strip("\r\n")
		lines.append( tmp )


#cups = [3,8,9,1,2,5,4,6,7] # test
cups = [ int(l) for l in lines[0] ]
mini = min(cups)
maxi = max(cups)


#
# Part 1
#

print("\nPart 1:")


def move(cups_list, source):
	idx = cups_list.index(source)
	dest = source - 1


	if len(cups_list) in [idx+1, idx+2, idx+3]:
		tmp = idx+4 - len(cups_list)
		a,b,c = cups_list[idx+1:] + cups_list[:tmp]
	else:
		a,b,c = cups_list[idx+1:idx+4]

	#print(a,b,c)
	cups_list.remove(a)
	cups_list.remove(b)
	cups_list.remove(c)
	#print(cups)


	new_idx = idx+1
	if new_idx >= len(cups_list): new_idx = 0
	out = cups_list[new_idx]


	while dest not in cups_list:
		dest -= 1
		if dest < mini: dest = maxi

	#print('destination:', dest)

	idx2 = cups_list.index(dest)
	cups_list.insert(idx2+1, c)
	cups_list.insert(idx2+1, b)
	cups_list.insert(idx2+1, a)


	return out


cups_copy = [ x for x in cups ]

start = cups_copy[0]
for i in range(100):
	x = move(cups_copy, start)
	start = x


idx_out = cups_copy.index(1)
tmp = cups_copy[idx_out+1:] + cups_copy[:idx_out]

res = ''
for x in tmp: res += str(x)

print("Result = {}" .format(res))


#
# Part 2
#

print("\nPart 2:")


class Cup:
	num = -1
	nxt = -1

	def __init__(self, _num, _next):
		self.num = _num
		self.nxt = _next

	def __repr__(self):
		return "Cup()"

	def __str__(self):
		return "({},{})".format(self.num, self.nxt)


# too much zeroes, I'm doing mistakes D:
one_million = 1000000
ten_million = 10000000


# shenanigans for later on
cups_tmp = cups + [ x for x in range(maxi+1, one_million+1)]

# Craft the list of Cups
my_list = { cups_tmp[i]: Cup(cups_tmp[i], cups_tmp[i+1]) for i in range(len(cups_tmp) - 1) }
my_list[one_million] = Cup(one_million, cups_tmp[0])



t1 = time.time()

start = cups[0]

for i in range(1, ten_million+1):

	# display where we are
	if i%100000 == 0: print('\033[1A\033[K{}'.format(i))

	# Get data
	source = my_list[start]
	a = my_list[source.nxt]
	b = my_list[a.nxt]
	c = my_list[b.nxt]

	# We can do that,we will always hit the while loop below.
	dest_num = source.num

	while dest_num in [source.num, a.num, b.num, c.num]:
		dest_num -= 1
		if dest_num < 1: dest_num = one_million

	dest = my_list[dest_num]


	# Update "pointers"
	# before: SRC -> A -> B -> C -> foo  /  DST -> bar
	# after:  SRC -> foo                 /  DST -> A -> B -> C -> bar
	foo = c.nxt
	bar = dest.nxt

	dest.nxt = source.nxt # i.e: A
	source.nxt = foo
	c.nxt = bar

	start = source.nxt


t2 = time.time()

print('')
print('TIME:', t2-t1, 's')
print('')



nxt1 = my_list[1].nxt
nxt2 = my_list[nxt1].nxt

num1 = my_list[nxt1].num
num2 = my_list[nxt2].num

res = num1 * num2
print("Result = {}" .format(res))




# Newline for sublime text
print('')

