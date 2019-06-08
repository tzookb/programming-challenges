def solution(arr , k):
	arrLen = len(arr)
	if arrLen == 0:
		return arr
	moves = k % arrLen
	return arr[arrLen-moves:arrLen] + arr[0:arrLen-1]

arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3
res = solution(arr, k)
print(res)