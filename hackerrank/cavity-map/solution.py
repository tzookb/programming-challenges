import sys

def shouldSkipBecauseEdges(x, y, n):
	"""
	if we are on the edges of the map, 
	so this could not be a cavity so skip it
	"""
	if x == 0 or x == n-1 or y == 0 or y == n-1 :
		return True
	return False


def isCavity(x, y, arr):
	"""
	simply checks all the neighbours: above, below, left, right
	if someone is equal or bigger so it is not a cavity
	"""
	cellVal = arr[y][x]

	if cellVal > arr[y-1][x] and cellVal > arr[y+1][x] and cellVal > arr[y][x-1] and cellVal > arr[y][x+1]:
		return True
	return False


def outputArrAsMap(arr):
	for row in arr:

		for cell in row:
			sys.stdout.write(str(cell))

		print ""


def markCavities(arr):
	n = len(arr)
	tempArr = arr

	for y in xrange(n):
			
		for x in xrange(n):
			if shouldSkipBecauseEdges(x, y, n):
				continue
			if isCavity(x, y, arr):
				tempArr[y][x] = 'X'

	return tempArr


nSize = int(raw_input())
arr = []

for i in xrange(nSize):
	row = raw_input()
	row = list(row)
	arr.append(row)


outputArrAsMap( markCavities(arr) )