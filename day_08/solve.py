#!/usr/bin/python3

import re, sys, os

lines = []
with open("input.txt", 'r') as fd:
	for line in fd:
		x = line.strip("\r\n").split(' ')
		y = { 'opcode': x[0], 'data': int(x[1]) }
		lines.append(y)

y = { 'opcode': 'end', 'data': '0' }
lines.append(y)


#
# Part 1
#

print("\nPart 1:")

accumulator = 0
old_addr = []
pointer = 0

while True:
	x = lines[pointer]

	if x['opcode'] == "acc":
		accumulator += x['data']
		old_addr.append(pointer)
		pointer += 1

	elif x['opcode'] == "jmp":
		old_addr.append(pointer)
		pointer += x['data']

	elif x['opcode'] == "nop":
		old_addr.append(pointer)
		pointer += 1


	if pointer in old_addr: break


print("Result = {}" .format(accumulator))


#
# Part 2
#

print("\nPart 2:")

def run_it(program, to_replace):
	accumulator = 0
	old_addr = []
	pointer = 0

	while pointer < len(program):
		x = program[pointer]
		old_addr.append(pointer)

		if x['opcode'] == "acc":
				accumulator += x['data']
				pointer += 1

		elif x['opcode'] == "jmp":
			if pointer == to_replace:
				# Replaced by nop
				pointer += 1

			else:
				# Normal jmp
				pointer += x['data']
				if pointer in old_addr:
					return old_addr[-1] # fail

		elif x['opcode'] == "nop":
			if pointer == to_replace:
				# Replaced by jmp
				pointer += x['data']
				if pointer in old_addr:
					return old_addr[-1] # fail

			else:
				# Normal nop
				pointer += 1


		elif x['opcode'] == "end":
			print("Result = {}" .format(accumulator))
			return -1 # success

	return -2 # oops?


# Brute force all swaps
for i in range(0, len(lines) - 1):
	prog = lines[:]

	if   prog[i]['opcode'] == "nop": pass # Swap is done at exec time
	elif prog[i]['opcode'] == "jmp": pass # Swap is done at exec time
	else: continue # not swappable


	ret = run_it(prog, i)
	if ret == -1: break
	if ret == -2:
		print("WTF?")
		break
