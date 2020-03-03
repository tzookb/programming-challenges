#it has some problems, need to find them

def findPath(stones, stepA, stepB):
	steps = stones -1
	sols = []
	for i in xrange(stones):
		sols.append( stepA*i + stepB*(steps-i) )
	sols.sort()
	return sols

def printSol(arr):
	for item in arr:
		print item,
	print ""


printSol(findPath(58,69,24))

if (0):
	tests = int(raw_input())

	for i in xrange(tests):
		stones = int(raw_input())
		stepA = int(raw_input())
		stepB = int(raw_input())
		sol = findPath(stones, stepA, stepB)
		printSol(sol)

1368 1413 1458 1503 1548 1593 1638 1683 1728 1773 1818 1863 1908 1953 1998 2043 2088 2133 2178 2223 2268 2313 2358 2403 2448 2493 2538 2583 2628 2673 2718 2763 2808 2853 2898 2943