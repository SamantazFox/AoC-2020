#!/usr/bin/python3

import re

lines = []
with open("input.txt", 'r') as fd:
	for line in fd:
		lines.append( line.strip("\r\n") )

#
# Part 1
#

print("\nPart 1:")

colors = {}

for l in lines:
	# Code
	x = re.match(r"^([\w\s]+) bags contain (.*)$", l)
	src = x[1].replace(' ', '_')
	dst = x[2].strip('.').split(', ')

	if dst[0] == "no other bags":
		colors[src] = None
	else:
		if src not in colors:
			colors[src] = {}

		for x in dst:
			tmp = re.match(r"^(\d+) (\w+ \w+) bags?$", x)
			color = tmp[2].replace(' ','_')
			count = tmp[1]
			colors[src][color] = count


def who_can_contain(color):
	out = []
	c = color.replace(' ', '_')

	for src in colors:
		if colors[src] is None: continue
		for dst in colors[src]:
			if c in dst:
				if src not in out:
					out.append(src)

				x = who_can_contain(src)
				if x != []:
					for n in x:
						if n not in out: out.append(n)

	return out


s = who_can_contain("shiny_gold")
print("Result = {}" .format(len(s)))


#
# Part 2
#

print("\nPart 2:")

def who_much_contain(color):
	c = color.replace(' ', '_')
	if colors[c] is None: return 0

	out = 0

	for nested in colors[c]:
		out += int(colors[c][nested])
		n = who_much_contain(nested)
		out += n * int(colors[c][nested])

	return out


res = who_much_contain("shiny_gold")
print("Result = {}" .format(res))
