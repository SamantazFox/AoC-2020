#!/usr/bin/python3

lines = []

with open("input.txt", 'r') as fd:
	for line in fd:
		lines.append( int(line.strip("\r\n")) )

#x = 0
#for line in lines:
#	print(str(x) + ' ' + str(line))
#	x = x+1

def toto(ia,ib,ic):
	a = lines[ia]
	b = lines[ib]
	c = lines[ic]

	tmp = a + b + c
	if tmp == 2020:
		tmp2 = a * b * c
		print("{} + {} + {} = 2020".format(a,b,c))
		print("{} * {} * {} = {}"  .format(a,b,c,tmp2))


for i in range(0,len(lines) - 1):
	for j in range(i,len(lines) - 1):
		for k in range(0,len(lines)):
			toto(i,j,k)
