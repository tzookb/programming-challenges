
import re

def fitToLiked(str):
	deletions = 0
	length = len(str)
	futureLikedStr = []

	
	#for i in xrange(length):
	
	for char in str:

		if not futureLikedStr:
			futureLikedStr.append(char)
		else:
			lastCharInNewStr = futureLikedStr[-1]
			if char != lastCharInNewStr:
				futureLikedStr.append(char)

	return len(str) - len(futureLikedStr)
	

amountOfTest = int(raw_input())

for i in xrange(amountOfTest):
	print fitToLiked(raw_input())