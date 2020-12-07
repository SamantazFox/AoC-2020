#!/usr/bin/python3

lines = []
with open("input.txt", 'r') as fd:
	for line in fd:
		lines.append( line.strip("\r\n") )

total = 0
for l in lines:
	x = l.split(' ')
	tmp = x[0].split('-')
	mini = int(tmp[0])
	maxi = int(tmp[1])
	letter = x[1][0]
	pwd = x[2]

	numok = 0
	for i in range(len(pwd)):
		if pwd[i] == letter:
			numok += 1
	if numok >= mini and numok <= maxi:
		total += 1

print(str(total))
