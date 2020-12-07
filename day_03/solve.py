#!/usr/bin/python3

lines = []
with open("input.txt", 'r') as fd:
	for line in fd:
		lines.append( line.strip("\r\n") )

#
# Part 1
#

print("\nPart 1:")

i = 0
n = 0

for j, l in enumerate(lines):
	# Code
	if j == 0: continue
	i+=3
	if i >= len(l): i -= len(l)
	if l[i] == '#': n += 1

result = n
print("Result = {}" .format(result))


#
# Part 2
#

print("\nPart 2:")


def slope(right, dwn):
	i = 0
	n = 0

	for j, l in enumerate(lines):
		# Code
		if j == 0: continue
		if (j%dwn) != 0: continue
		i+=right
		if i >= len(l): i -= len(l)
		if l[i] == '#': n += 1

	print("Result ({}, {}) = {}" .format(right, dwn, n))
	return n



a = slope(1,1)
b = slope(3,1)
c = slope(5,1)
d = slope(7,1)
e = slope(1,2)


result = a*b*c*d*e
print("Result = {}" .format(result))
