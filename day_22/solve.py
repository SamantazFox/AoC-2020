#!/usr/bin/python3

import os, sys
import re, copy
import math


lines = []
with open("input.txt", 'r') as fd:
	for line in fd:
		tmp = line.strip("\r\n")
		lines.append( tmp )


empty = ''
lines.append(empty)


player=0
decks = {}
tmp = []

for l in lines:
	if   l == 'Player 1:': player = 1
	elif l == 'Player 2:': player = 2

	elif l == '':
		decks[player] = tmp
		tmp = []

	else: tmp.append(int(l))



#
# Part 1
#

print("\nPart 1:")


winner = 0
rnd = 0

#while True:
#	a = decks[1].pop(0) # P1
#	b = decks[2].pop(0) # P2
#
#	if a > b:
#		decks[1].append(a)
#		decks[1].append(b)
#
#	elif b > a:
#		decks[2].append(b)
#		decks[2].append(a)
#
#	else:
#		print('error')
#
#
#	print('Round', rnd)
#	print(decks[1])
#	print(decks[2])
#	print('')
#
#
#	if decks[1] == []:
#		winner = 2
#		break
#
#	if decks[2] == []:
#		winner = 1
#		break
#
#	rnd += 1


res = 0
#j = 0
#for i in range(len(decks[winner])-1, -1, -1):
#	j +=1
#	res += decks[winner][i] * j

print("Result = {}" .format(res))


#
# Part 2
#

print("\nPart 2:")

global game
game = 1

def recursive(d1, d2):
	deck_1 = [ x for x in d1 ]
	deck_2 = [ x for x in d2 ]

	global game
	this_game = str(game)
	prev = []

	rnd = 1

	#print('=== Game', this_game, '===')

	while True:
		#print('')
		#print('-- Round', rnd, '(Game', this_game+') --')
		#print('Player 1\'s deck:', ', '.join( [ str(x) for x in deck_1 ] ))
		#print('Player 2\'s deck:', ', '.join( [ str(x) for x in deck_2 ] ))
		#print('Player 1 plays:', a[0])
		#print('Player 2 plays:', b[0])


		current_config = ( tuple(deck_1), tuple(deck_2) )

		if current_config in prev:
			#print('Player 1 wins round', rnd, 'of game', this_game+'!')
			#print('The winner of game', this_game, 'is player 1!')
			return (1, deck_1)

		prev.append( current_config )


		a = deck_1.pop(0) # P1
		b = deck_2.pop(0) # P2


		if len(deck_1) >= a and len(deck_2) >= b:
			#print('Playing a sub-game to determine the winner...')
			#print('')

			game += 1
			round_winner, _none = recursive(deck_1[:a], deck_2[:b])

			#print('')
			#print('...anyway, back to game', this_game+'.')

		else:
			if   a > b: round_winner = 1
			elif b > a: round_winner = 2


		if round_winner == 1:
			deck_1.append(a)
			deck_1.append(b)

		elif round_winner == 2:
			deck_2.append(b)
			deck_2.append(a)

		else:
			print('error')


		#print('Player', round_winner, 'wins round', rnd, 'of game', this_game+'!')


		if deck_1 == []:
			#print('The winner of game', this_game, 'is player 2!')
			return (2, deck_2)
		if deck_2 == []:
			#print('The winner of game', this_game, 'is player 1!')
			return (1, deck_1)

		rnd += 1



winner, win_deck = recursive(decks[1], decks[2])


res = 0
j = 0
for i in range(len(win_deck)-1, -1, -1):
	j +=1
	res += win_deck[i] * j


print("Result = {}" .format(res))




# Newline for sublime text
print('')
