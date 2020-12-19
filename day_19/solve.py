#!/usr/bin/python3

import os, sys
import re, copy
import math


lines = []
with open("input.txt", 'r') as fd:
	for line in fd:
		tmp = line.strip("\r\n")
		lines.append( tmp )




rules={}
p2 = False

strings = []

for l in lines:
	if l == '':
		p2 = True
		continue

	if p2:
		strings.append(l)

	else:
		x = l.split(':')
		idx = x[0]
		rls = x[1].strip(' ').split(' | ')

		if len(rls) == 1:
			if len(rls[0]) == 3 and rls[0][0] == rls[0][2] == '"':
				rules[idx] = rls[0]
			else:
				rules[idx] = ( rls[0].split(' '), None )
		else:
			rules[idx] = ( rls[0].split(' '), rls[1].split(' ') )



#
# Part 1
#

print("\nPart 1:")


mem = {}

def recurse(r, l=0):
	if l == 50: quit()
	if r in mem: return mem[r]

	x = rules[r]
	out = []

	if len(x) == 3 and x[0] == x[2] == '"': # "a" or "b"
		out.append(x[1])
		#print(' '*l, 'x', out)

	else:
		#print (' '*l, r,rules[r])
		for n in range(len(x)):
			if x[n] is None: continue

			#print (' '*l, r, ' isrecursing', x[n][0])
			a = recurse( x[n][0] , l+1)

			if len(x[n]) == 1:
				for i in a: out.append(i)

			else:
				#print (' '*l, r, ' isrecursing', x[n][1])
				b = recurse( x[n][1] , l+1)

				for i in a:
					for j in b:
						out.append(i + j)

	if r not in mem: mem[r] = out
	return out


#for x in sorted(rules, reverse=True):
#	print(x,':', rules[x])
#print('')


r0 = [] #recurse('0')


res = 180
for s in strings:
	if s in r0: res += 1


print("Result = {}" .format(res))


#
# Part 2
#

print("\nPart 2:")

# Replacements
rules['8']  = (['42'], ['42', '8'])
rules['11'] = (['42', '31'], ['42', '11', '31'])



def join(string, c):
	out = ''
	for x in string: out += x + c
	return out[:-1]


def recurse2(r, l=0):
	if l == 50: quit()
	#if r in mem2: return mem2[r]

	x = rules[r]
	out = []


	if len(x) == 3 and x[0] == x[2] == '"': # "a" or "b"
		out = x[1] #'('+x[1]+')'

	elif r == '8':
		a = recurse2(x[0][0])
		out = '('+a+')+'

	elif r == '11':
		a = recurse2(x[0][0])
		b = recurse2(x[0][1])

		tmp = []

		# You $#@*%$ bastard....
		# we can't do ((...)+(...)+) because we need to have exactly the same
		# amount of repetitions on each half.
		# i.e (with #x meaning rule number x):
		#       (#42){1}(#31){1}
		#    or (#42){2}(#31){2}
		#    or (#42){3}(#31){3}
		#    or  ...
		for i in range(1,50):
			tmp.append( '(?:{0}){2}(?:{1}){2}'.format(a,b, '{'+str(i)+'}') )

		out = '('+ join(tmp, '|') + ')'

	else:
		out = '('
		for n in range(len(x)):
			if x[n] is None: continue
			if n != 0: out += '|'

			a = recurse2(x[n][0])

			if len(x[n]) == 2:
				b = recurse2(x[n][1])
				out += a+b
			else:
				out += a

		out += ')'

	return out


#print("'8'", rules['8'])
#print("'11'", rules['11'])
#
#for x in sorted(rules):
#	print(x,':', rules[x])
#print('')

r0_2 = recurse2('0')
print(r0_2)

res = 0
for s in strings:
	if re.match('^'+r0_2+'$', s):
		#print(s)
		res += 1


print("Result = {}" .format(res))




# Newline for sublime text
print('')

