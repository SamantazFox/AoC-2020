#!/usr/bin/python3

import os, sys
import re, copy
import math


lines = []
with open("input.txt", 'r') as fd:
	for line in fd:
		tmp = line.strip("\r\n")
		lines.append( tmp )



ingredients = {}
allergens   = {}

i = 0

for l in lines:
	tmp = re.search(r' \(contains ([\w\s,]+)\)$', l)

	if tmp:
		allergens[i] = tmp[1].split(', ')
		ingredients[i] = l.replace(tmp[0],'').split(' ')

	else:
		allergens[i] = []
		ingredients[i] = l.split(' ')

	i += 1


#
# Part 1
#

print("\nPart 1:")


allergens_lst = {}

for i in allergens:
	for a in allergens[i]:
		# Ex: allergenss_list['soy'] = [1,2,3]
		if a not in allergens_lst:
			allergens_lst[a] = [i]
		else:
			allergens_lst[a].append(i)

ingredients_allergenic = {}
ingredients_allergenic_lst = []

for a in allergens_lst:
	lst = allergens_lst[a]
	ingredients_allergenic[a] = []

	for i in ingredients[lst[0]]:
		count = 1
		for j in lst[1:]:
			if i in ingredients[j]: count+=1

		if count == len(lst):
			ingredients_allergenic[a].append(i)

			if i not in ingredients_allergenic_lst:
				ingredients_allergenic_lst.append(i)


res = 0
for idx in ingredients:
	for i in ingredients[idx]:
		if i not in ingredients_allergenic_lst:
			res += 1

print("Result = {}" .format(res))


#
# Part 2
#

print("\nPart 2:")


# Deduce which ingredient contains allergens
contains = {}
dict_copy = dict([ (elem,ingredients_allergenic[elem]) for elem in ingredients_allergenic ])

while dict_copy:
	# compute the length of all lists remaining in dict_copy
	sizes = [ (len(dict_copy[elem]), elem) for elem in dict_copy ]

	# then get the smallest one
	elem = min(sizes)[1]
	lst = [ x for x in dict_copy[elem] ]

	# Save known element and remove it from all other lists
	contains[elem] = lst[0]

	for e in dict_copy:
		if contains[elem] in dict_copy[e]:
			dict_copy[e].remove(contains[elem])

	# Delete items we don't need anymore
	del dict_copy[elem]


out = []
for elem in sorted(contains):
	out.append(contains[elem])


res = ','.join(out)
print("Result = {}" .format(res))




# Newline for sublime text
print('')

