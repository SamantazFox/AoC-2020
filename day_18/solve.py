#!/usr/bin/python3

import os, sys
import re, copy
import math


lines = []
with open("input.txt", 'r') as fd:
	for line in fd:
		tmp = line.strip("\r\n").replace(' ', '')
		lines.append( tmp )


#
# Part 1
#

print("\nPart 1:")


def parenthesis(eq):
	start = -1
	stop  = -1

	parenthesisCount = 0;
	for i in range(0, len(eq)):
		if eq[i] == '(':
			parenthesisCount += 1

			if parenthesisCount == 1 and start == -1:
				start = i

		if eq[i] == ')':
			parenthesisCount -= 1
			if parenthesisCount == 0 and start != -1:
				stop = i
				break;

	return (start, stop)


def findOP(eq):
	p = eq.find('+')
	m = eq.find('-')
	d = eq.find('/')
	t = eq.find('*')

	lst = []
	for n in [p,m,d,t]:
		if n != -1: lst.append(n)

	if not lst:
		return -1
	else:
		return min(lst)


def compute(eq):
	pos = findOP(eq)
	x = int(eq[:pos])

	pos2 = pos+1 + findOP(eq[pos+1:])
	
	if pos2 == -1 or pos2 == pos:
		y = int(eq[pos+1:])
		tmp = eq[:]
	else:
		y = int(eq[pos+1:pos2])
		tmp = eq[:pos2]


	if eq[pos] == '+': res = x + y
	if eq[pos] == '-': res = x - y
	if eq[pos] == '/': res = x / y
	if eq[pos] == '*': res = x * y

	out = str(res) + eq[len(tmp):]

	if not out.isdecimal():
		return compute(out)
	else:
		return int(out)


def parse(eq):

	while parenthesis(eq) != (-1,-1):
		tmp = parenthesis(eq)
		sub = eq[tmp[0] : tmp[1]+1]
		eq2 = parse( sub[1:-1] )
		eq = eq.replace(sub, str(eq2))

	x = compute(eq)
	return x


tests = [
	( '1 + 2 * 3 + 4 * 5 + 6',                              71),
	( '1 + (2 * 3) + (4 * (5 + 6))',                        51),
	( '2 * 3 + (4 * 5)',                                    26),
	( '5 + (8 * 3 + 9 + 3 * 4 * 3)',                       437),
	( '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',       12240),
	( '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632),
]

#print('Tests:')
#for x in tests:
#	print(parse(x[0].replace(' ','')) == x[1])
#print('')


total = 0
for l in lines:
	#print(parse(l))
	total += parse(l)

res = total
print("Result = {}" .format(res))


#
# Part 2
#

print("\nPart 2:")

def compute2(eq):
	eq = eq.split('*')

	res = 1
	for e in eq:
		x = 0
		for f in e.split('+'): x += int(f)
		res *= x

	return res


def parse2(eq):

	while parenthesis(eq) != (-1,-1):
		tmp = parenthesis(eq)
		sub = eq[tmp[0] : tmp[1]+1]
		eq2 = parse2( sub[1:-1] )
		eq = eq.replace(sub, str(eq2))

	x = compute2(eq)
	return x


tests = [
	( '1 + 2 * 3 + 4 * 5 + 6',                              231),
	( '1 + (2 * 3) + (4 * (5 + 6))',                         51),
	( '2 * 3 + (4 * 5)',                                     46),
	( '5 + (8 * 3 + 9 + 3 * 4 * 3)',                       1445),
	( '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',       669060),
	( '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2',  23340),
]

#print('Tests:')
#for x in tests:
#	print(parse2(x[0].replace(' ','')) == x[1])
#print('')


total2 = 0
for l in lines:
	print(parse2(l))
	total2 += parse2(l)

res = total2
print("Result = {}" .format(res))




# Newline for sublime text
print('')

