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

passports = []
curr = {}

for l in lines:
	if l == '':
		#curr['valid'] = True

		req = 0
		if 'byr' in curr: req += 1 # curr['valid'] = False
		if 'iyr' in curr: req += 1 # curr['valid'] = False
		if 'eyr' in curr: req += 1 # curr['valid'] = False
		if 'hgt' in curr: req += 1 # curr['valid'] = False
		if 'hcl' in curr: req += 1 # curr['valid'] = False
		if 'ecl' in curr: req += 1 # curr['valid'] = False
		if 'pid' in curr: req += 1 # curr['valid'] = False
		if 'cid' in curr: req += 1 # curr['valid'] = False

		if req == 8 or (req == 7 and 'cid' not in curr):
			curr['valid'] = True
		else:
			curr['valid'] = False

		passports.append(curr)
		curr = {}

	else:
		for a in l.split(' '):
			b = a.split(':')
			curr[b[0]] = b[1]


vld = 0
for p in passports:
	if p['valid']: vld += 1

print("Result = {}" .format(vld))


#
# Part 2
#

print("\nPart 2:")

vld = 0
for p in passports:
	if not p['valid']: continue


	if p['byr'].isdecimal():
		p['byr'] = int(p['byr'])
		if not (p['byr'] >= 1920 and p['byr'] <= 2002):
			p['valid'] = False
	else:
		p['valid'] = False


	if p['iyr'].isdecimal():
		p['iyr'] = int(p['iyr'])
		if not (p['iyr'] >= 2010 and p['iyr'] <= 2020):
			p['valid'] = False
	else:
		p['valid'] = False


	if p['eyr'].isdecimal():
		p['eyr'] = int(p['eyr'])
		if not (p['eyr'] >= 2020 and p['eyr'] <= 2030):
			p['valid'] = False
	else:
		p['valid'] = False


	if p['hgt'][0:-2].isdecimal() and p['hgt'].endswith('cm'):
		if not (int(p['hgt'][0:-2]) >= 150 and int(p['hgt'][0:-2]) <= 193):
			p['valid'] = False

	elif p['hgt'][0:-2].isdecimal() and p['hgt'].endswith('in'):
		if not (int(p['hgt'][0:-2]) >= 59 and int(p['hgt'][0:-2]) <= 76):
			p['valid'] = False

	else:
		p['valid'] = False


	if not re.search("^\#[0-9a-f]{6}$", p['hcl']):
		p['valid'] = False

	if p['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
		p['valid'] = False

	if not (len(p['pid']) == 9 and p['pid'].isdecimal()):
		p['valid'] = False


vld = 0
for p in passports:
	if p['valid']: vld += 1

print("Result = {}" .format(vld))
