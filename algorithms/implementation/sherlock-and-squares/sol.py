import math

def countSquares(min, max):
	counts = 0
	minSqrt = int(math.ceil(math.sqrt(min)))
	maxSqrt = int(math.floor(math.sqrt(max)))

	for x in xrange(minSqrt, maxSqrt+1):
		powed = math.pow(x, 2)
		if powed >=min and powed <= max:
			counts += 1

	return counts

for test in xrange(int(raw_input())):
	min, max = map(int, raw_input().split(" "))
	print countSquares(min, max)