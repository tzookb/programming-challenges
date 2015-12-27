import math

def fibMod(first, second, nSpot):
	if (nSpot == 2):
		return second 
	elif (nSpot == 1):
		return first 
	elif (nSpot == 0):
		return 0

	return (long)(math.pow(fibMod(first, second, nSpot-1), 2) + fibMod(first, second, nSpot-2))

first, second, nspot = map(long, raw_input().split(" "))
res = fibMod(first, second, nspot)

print res