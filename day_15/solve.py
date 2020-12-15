#!/usr/bin/python3

import os, sys
import re, copy


numbers = [0,13,1,8,6,15]


#
# Part 1
#

print("\nPart 1:")

# Examples
#nums = [0,3,6] # 436
#nums = [1,3,2] # 1
#nums = [2,1,3] # 10
#nums = [1,2,3] # 27
#nums = [2,3,1] # 78
#nums = [3,2,1] # 438
#nums = [3,1,2] # 1836

def speak(nums, maxi):
	rem = {}
	spok = 0

	for i in range(0,len(nums)):
		rem[nums[i]] = []
		rem[nums[i]].append(i+1)

	for i in range(len(nums),maxi):
		spok = 0
		last = nums[i-1]

		#print("last = ", last)

		if last in rem:
			if len(rem[last]) > 1:
				diff = rem[last][-1] - rem[last][-2]
				spok = diff

			elif len(rem[last]) > 4:
				rem[spok].pop(0)


		if not spok in rem: rem[spok] = []
		rem[spok].append(i+1)
		nums.append(spok)

		#print("spoken = ", spok)
		#print('')

	return spok

res = speak(numbers, 2020)
print("Result = {}" .format(res))


#
# Part 2
#

print("\nPart 2:")



res = speak(numbers, 30000000)
print("Result = {}" .format(res))




# Newline for sublime text
print('')

