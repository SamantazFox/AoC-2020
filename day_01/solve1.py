#!/usr/bin/python3

lines = []

with open("input.txt", 'r') as fd:
	for line in fd:
		lines.append( int(line.strip("\r\n")) )

#x = 0
#for line in lines:
#	print(str(x) + ' ' + str(line))
#	x = x+1

for i in range(0,len(lines) - 1):
	for j in range(i,len(lines) - 1):
		tmp = lines[i] + lines[j]
		if tmp == 2020:
			print("{} + {} = 2020".format(lines[i], lines[j]))
			print("{} * {} = {}".format(lines[i], lines[j], lines[i]*lines[j]))
