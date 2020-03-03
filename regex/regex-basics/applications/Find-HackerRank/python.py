import re

def findThedHackerrank(phrase):
	sol = -1

	if re.match( r'hackerrank (.*) hackerrank$', phrase) or phrase == 'hackerrank':
		sol = 0
	elif re.match( r'hackerrank (.*)', phrase):
		sol = 1
	elif re.match( r'(.*) hackerrank$', phrase):
		sol = 2

	return sol


numOfTest = int(raw_input())

for i in xrange(numOfTest):
	print findThedHackerrank(raw_input())