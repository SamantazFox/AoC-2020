#!/usr/bin/python3

lines = []
with open("input.txt", 'r') as fd:
	for line in fd:
		lines.append( line.strip("\r\n") )

total = 0
for l in lines:
	x = l.split(' ')
	tmp = x[0].split('-')
	r_one = int(tmp[0]) -1
	r_two = int(tmp[1]) -1
	letter = x[1][0]
	pwd = x[2]

	numok = 0
	if pwd[r_one] == letter: numok += 1
	if pwd[r_two] == letter: numok += 1

	if numok == 1:
		total += 1

print(str(total))
