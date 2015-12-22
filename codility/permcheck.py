
def solution(arr):
	size = len(arr)
	sum = 0
	index = 1
	valsFound = {}

	for item in arr:
		if item<1 or item>size:
			return 0
		if item in valsFound:
			return 0

		valsFound[item] = True

		sum += item - index

		index += 1

	if sum == 0:
		return 1
	return 0


res = solution([4,1,3,2])    
print res