#!/usr/bin/python3

import os, sys
import re, copy
import math


lines = []
with open("input.txt", 'r') as fd:
	for line in fd:
		tmp = line.strip("\r\n")
		lines.append( tmp )

lines.append('')


tiles = {}
idx = 0
for l in lines:
	if l == '': continue
	elif '#' in l or '.' in l:
		tiles[idx].append(l)
	else:
		m = re.match(r'^Tile (\d+)\:$', l)
		idx = m[1]
		tiles[idx] = []


#for t in tiles: print(t, ':', tiles[t])


#
# Part 1
#

print("\nPart 1:")


def invertStr(string):
	out = ''
	for i in range(len(string)-1,-1,-1):
		out += string[i]
	return out


def borders(tile):
	borders = {}

	borders['top'] = tile[0]
	borders['bot'] = tile[-1]
	borders['lft'] = ''.join([ x[ 0] for x in tile ])
	borders['rgt'] = ''.join([ x[-1] for x in tile ])

	return borders


def hasMatch(tile):
	brd_nor = borders(tiles[tile])
	brd_inv = dict([ (brd,invertStr(brd_nor[brd])) for brd in brd_nor ])

	matches = { 'top': [], 'bot': [], 'lft': [], 'rgt': [] }

	for t in tiles:
		if t == tile: continue

		to_check = borders(tiles[t])

		for brd2 in to_check:
			# normal check
			for brd in brd_nor:
				if brd_nor[brd] == to_check[brd2]:
					#print('N:', t, b, b2, x[b])
					matches[brd].append( (t, brd2, False) )

			# invert check
			for brd in brd_inv:
				if brd_inv[brd] == to_check[brd2]:
					#print('I:', t, b, b2, y[b])
					matches[brd].append( (t, brd2, True) )

	return matches


res = 1
for t in tiles:
	tmp = hasMatch(t)

	if (tmp['top'] == [] or tmp['bot'] == []) and (tmp['lft'] == [] or tmp['rgt'] == []):
		#print(t, ':', tmp)
		res *= int(t)

print("Result = {}" .format(res))


#
# Part 2
#

print("\nPart 2:")



def tileMatch(me, tile):
	out = {}

	brd = borders(tile)
	out['top'] = bool(brd['bot'] == me['top'])
	out['bot'] = bool(brd['top'] == me['bot'])
	out['lft'] = bool(brd['rgt'] == me['lft'])
	out['rgt'] = bool(brd['lft'] == me['rgt'])

	return out


def Hflip(tile): return [ invertStr(l) for l in tile ]
def Vflip(tile): return [ tile[i] for i in range(len(tile)-1,-1,-1) ]

def rotate90L(tile):
	out = []
	for i in range(len(tile[0])-1,-1,-1):
		out.append( ''.join([ x[i] for x in tile ]) )
	return out

def rotate90R(tile):
	out = []
	for i in range(len(tile[0])):
		out.append( ''.join([ x[i] for x in tile ]) )
	return out

def rotate180(tile): return rotate90L(rotate90L(tile))


#def nearby(tile):
#	# For each edge, get a list of:
#	#  (tile_id, Hflip, Vflip, Rotate)
#	out = {
#		'top':[], 'bot':[],
#		'lft':[], 'rgt':[]
#	}
#
#	my = borders(tiles[tile])
#
#	for tile_id in tiles:
#		# Skip ourselves
#		if tile_id == tile: continue
#
#		# Get that tile's borders
#		b = borders(tiles[tile_id])
#
#
#		# Simple cases: no rotations/flips
#		# 	Direct tile match on any edges
#		#print(tileMatch(my, tiles[tile_id] ))
#		for edge,val in tileMatch(my, tiles[tile_id] ).items():
#			if val: out[edge].append( (tile_id, False, False, 0) )
#
#
#		# Medium cases: Horizontal flips
#		# 	Horizontally flipped tile match on any edges
#		#print(tileMatch(my, Hflip(tiles[tile_id]) ))
#		for edge,val in tileMatch(my, Hflip(tiles[tile_id]) ).items():
#			if val: out[edge].append( (tile_id, True, False, 0) )
#
#		# Medium cases: Vertical flips
#		# 	Vertically flipped tile match on any edges
#		#print(tileMatch(my, Vflip(tiles[tile_id]) ))
#		for edge,val in tileMatch(my, Vflip(tiles[tile_id]) ).items():
#			if val: out[edge].append( (tile_id, False, True, 0) )
#
#
#		# Hard cases 1: 90° rotate left
#		#print(tileMatch(my, rotate90L(tiles[tile_id]) ))
#		for edge,val in tileMatch(my, rotate90L(tiles[tile_id]) ).items():
#			if val: out[edge].append( (tile_id, False, False, -90) )
#
#		# Hard cases 2: 90° rotate right
#		#print(tileMatch(my, rotate90R(tiles[tile_id]) ))
#		for edge,val in tileMatch(my, rotate90R(tiles[tile_id]) ).items():
#			if val: out[edge].append( (tile_id, False, False,  90) )
#
#		# Hard cases 3: 180 rotate
#		#print(tileMatch(my, rotate180(tiles[tile_id]) ))
#		for edge,val in tileMatch(my, rotate180(tiles[tile_id]) ).items():
#			if val: out[edge].append( (tile_id, False, False, 180) )
#
#
#		# Hardcore cases: flip with rotation combined
#		#   We need to only flip once, either H or V.
#		#   Hflip & 90° L is the same as Vflip & 90° R
#		tmp1 = Hflip(tiles[tile_id])
#		#print(tileMatch(my, rotate90L(tmp1) ))
#		for edge,val in tileMatch(my, rotate90L(tmp1) ).items():
#			if val: out[edge].append( (tile_id, True, False, -90) )
#
#		#print(tileMatch(my, rotate90R(tmp1) ))
#		for edge,val in tileMatch(my, rotate90R(tmp1) ).items():
#			if val: out[edge].append( (tile_id, True, False,  90) )
#
#
#		#print('')
#
#	#print(out)
#	return out


edge_size = int( math.sqrt(len(tiles)) )
matches   = dict([ (t,hasMatch(t)) for t in tiles ])

# Empty edge_size by edge_size array
image = [[0 for i in range(edge_size)] for i in range(edge_size) ]


# List the known tiles

corner = {}
border = {}
middle = {}

for t in tiles:
	tmp = hasMatch(t)

	# Corners tiles
	if (tmp['top'] == [] or tmp['bot'] == []) and (tmp['lft'] == [] or tmp['rgt'] == []):
		corner[t] = tmp

	# Edges/border tiles
	elif tmp['top'] == [] or tmp['bot'] == [] or tmp['lft'] == [] or tmp['rgt'] == []:
		border[t] = tmp

	# center tiles
	else: middle[t] = tmp


# Fun times !!

# Take the corner with no rotated neighbors as a start point
start = ''
for c in corner:
	total = 0

	for x in corner[c]:
		if corner[c][x] and corner[c][x][0][2]: total += 1

	if total == 0: start = c


if matches[start]['top'] == []:
	if matches[start]['lft'] == []: image[]
	if matches[start]['rgt'] == []:

if matches[start]['bot'] == []:
	if matches[start]['lft'] == []:
	if matches[start]['rgt'] == []:



while True:



for tiles in border:
	if True: pass




#print('')
#for x in image: print(x)



res = 0
print("Result = {}" .format(res))




# Newline for sublime text
print('')

