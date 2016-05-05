def getBeforeItemInList(list, index, default):
	extra = 0
	if (index > 0):
		extra = list[index-1]
	return extra


def checkArr(arr):
	leftToRight = []
	rightToLeft = []

	for index, value in enumerate(arr):
		leftToRight.append(arr[index]+getBeforeItemInList(leftToRight, index, 0));
		rightToLeft.append(arr[len(arr)-1-index]+getBeforeItemInList(rightToLeft, index, 0));
		
	rightToLeft.reverse()


	for index, value in enumerate(leftToRight):
		if (leftToRight[index] == rightToLeft[index]):
			return 'YES'

	return 'NO'
		


for test in xrange(int(raw_input())):
	sizeOfArray = raw_input()
	theArray = map(int, raw_input().split())
	print checkArr(theArray)