#!/usr/bin/python3

import os, sys
import re, copy
import math


lines = {}
n = 0
with open("input.txt", 'r') as fd:
	for line in fd:
		tmp = line.strip("\r\n")

		lines[n] = {}
		for i in range(len(tmp)):
			lines[n][i] = { 0: tmp[i] }

		n += 1


#
# Part 1
#

print("\nPart 1:")

# Init / first copy
dimensions = lines


def printCube(cube):
	print('{')
	#for x in cube:
	#	print('	{',x,':',)
	#	for y in cube[x]:
	#		print('		{',y,':', cube[x][y],'}')

	for z in cube[0][0]:
		print('	{',z,':')
		for x in cube:
			print('		{',x,': { ', end='')
			for y in cube[x]:
				print("{}:'{}', ".format(y,cube[x][y][z]), end='')
			print(' }')
		print('	}')
	print('}')


def copyExpand(arr):
	out = {}

	min_x,max_x = min(arr      ) - 1, max(arr      ) + 1
	min_y,max_y = min(arr[0]   ) - 1, max(arr[0]   ) + 1
	min_z,max_z = min(arr[0][0]) - 1, max(arr[0][0]) + 1

	for x in range(min_x,max_x+1):
		if x not in out: out[x] = {}

		for y in range(min_y,max_y+1):
			if y not in out[x]: out[x][y] = {}

			for z in range(min_z,max_z+1):
				if (x in arr) and (y in arr[x]) and (z in arr[x][y]):
					out[x][y][z] = arr[x][y][z]
				else:
					out[x][y][z] = '.'

	return out


def countNeighbors(arr, x,y,z):
	total = 0

	for i in [x-1, x, x+1]:
		if i in arr:

			for j in [y-1, y, y+1]:
				if j in arr[i]:

					for k in [z-1, z, z+1]:
						if k in arr[i][j]:

							if (i == x) and (j == y) and (k == z): continue
							if arr[i][j][k] == '#': total += 1

	return total


def cycle(dim):
	out = copyExpand(dim)

	for x in out:
		for y in out[x]:
			for z in out[x][y]:

				n = countNeighbors(dim, x,y,z)
				if (x in dim) and (y in dim[x]) and (z in dim[x][y]):
					c = dim[x][y][z]
				else:
					c = '.'

				#print(x,y,z, '  ',c,n)

				if c == '#':   #active
					if (n == 2) or (n == 3): out[x][y][z] = '#'
					else: out[x][y][z] = '.'

				elif c == '.': #inactive
					if n == 3: out[x][y][z] = '#'
					else: out[x][y][z] = '.'

				else:
					print("Ooops!!")

	return out

#dimensions2 = cycle(dimensions)
#dimensions3 = cycle(dimensions2)
#dimensions4 = cycle(dimensions3)
#dimensions5 = cycle(dimensions4)
#dimensions6 = cycle(dimensions5)
#dimensions7 = cycle(dimensions6)

#printCube(dimensions7)



for c in lines:
	pass


res = 0
print("Result = {}" .format(res))


#
# Part 2
#

print("\nPart 2:")


# Init / first copy
four_d = lines
for x in four_d:
	for y in four_d[x]:
		for z in four_d[x][y]:
			tmp = four_d[x][y][z]
			four_d[x][y][z] = { 0: tmp }



def printCube4(cube):
	print('{')

	for z in cube[0][0]:
		for w in cube[0][0][0]:

			print('	{ z=',z,'/ w=',w,':')
			for x in cube:
				print('		{',x,': { ', end='')
				for y in cube[x]:
					print("{}:'{}', ".format(y,cube[x][y][z][w]), end='')
				print(' }')
			print('	}')

	print('}')


def copyExpand4(arr):
	out = {}

	min_x,max_x = min(arr         ) - 1, max(arr         ) + 1
	min_y,max_y = min(arr[0]      ) - 1, max(arr[0]      ) + 1
	min_z,max_z = min(arr[0][0]   ) - 1, max(arr[0][0]   ) + 1
	min_w,max_w = min(arr[0][0][0]) - 1, max(arr[0][0][0]) + 1

	for x in range(min_x,max_x+1):
		if x not in out: out[x] = {}

		for y in range(min_y,max_y+1):
			if y not in out[x]: out[x][y] = {}

			for z in range(min_z,max_z+1):
				if z not in out[x][y]: out[x][y][z] = {}

				for w in range(min_w,max_w+1):

					if (x in arr) and (y in arr[x]) and (z in arr[x][y]) and (w in arr[x][y][z]):
						out[x][y][z][w] = arr[x][y][z][w]
					else:
						out[x][y][z][w] = '.'

	return out


def countNeighbors4(arr, x,y,z,w):
	total = 0

	for i in [x-1, x, x+1]:
		if i in arr:

			for j in [y-1, y, y+1]:
				if j in arr[i]:

					for k in [z-1, z, z+1]:
						if k in arr[i][j]:

							for l in [w-1, w, w+1]:
								if l in arr[i][j][k]:

									if (i == x) and (j == y) and (k == z) and (l == w):
										continue

									if arr[i][j][k][l] == '#':
										total += 1

	return total


def cycle4(dim):
	out = copyExpand4(dim)

	for x in out:
		for y in out[x]:
			for z in out[x][y]:
				for w in out[x][y][z]:

					n = countNeighbors4(dim, x,y,z,w)
					if (x in dim) and (y in dim[x]) and (z in dim[x][y]) and (w in dim[x][y][z]):
						c = dim[x][y][z][w]
					else:
						c = '.'

					#print(x,y,z, '  ',c,n)

					if c == '#':   #active
						if (n == 2) or (n == 3): out[x][y][z][w] = '#'
						else: out[x][y][z][w] = '.'

					elif c == '.': #inactive
						if n == 3: out[x][y][z][w] = '#'
						else: out[x][y][z][w] = '.'

					else:
						print("Ooops!!")

	return out

four_d2 = cycle4(four_d)
four_d3 = cycle4(four_d2)
four_d4 = cycle4(four_d3)
four_d5 = cycle4(four_d4)
four_d6 = cycle4(four_d5)
four_d7 = cycle4(four_d6)

printCube4(four_d7)



for c in lines:
	pass


res = 0
print("Result = {}" .format(res))




# Newline for sublime text
print('')

