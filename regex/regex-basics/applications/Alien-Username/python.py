import re

def findThedHackerrank(phrase):

	res = re.match( r'^[\._]{1}[0-9]+[A-Za-z]*[_]{0,1}$', phrase)

	if res:
		return 'VALID'
	
	return 'INVALID'

		
	


numOfTest = int(raw_input())

for i in xrange(numOfTest):
	print findThedHackerrank(raw_input())