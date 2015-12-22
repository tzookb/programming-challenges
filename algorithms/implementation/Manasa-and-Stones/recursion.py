###
#this works good, but fails on big numbers as this is to slow

def findPath(stones, stepA, stepB, sum):
	if stones == 0:
		return [sum];

	final = []
	final = final + (findPath(stones-1, stepA, stepB, sum+stepA))
	final = final + (findPath(stones-1, stepA, stepB, sum+stepB))
	sol = list(set(final))
	sol.sort()
	return sol



tests = int(raw_input())

for i in xrange(tests):
	stones = int(raw_input())
	stepA = int(raw_input())
	stepB = int(raw_input())
	sol = findPath(stones-1, stepA, stepB, 0)
	for item in sol:
		print item,
	print ""
