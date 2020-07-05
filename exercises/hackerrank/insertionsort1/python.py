def printArr(arr):
	for item in arr:
		print item,
	print ""

def insertSearch(arr):
	size = len(arr)
	subject = arr[-1]

	i = size-2
	
	while i >= 0:
		nextSpot = arr[i+1]
		currentSpot = arr[i]

		if currentSpot > subject:
			arr[i+1] = currentSpot
		else:
			arr[i+1] = subject
			break

		printArr(arr)

		i -= 1

	if i == -1:
		arr[0] = subject

	printArr(arr)
 

raw_input()

desired_array = [int(numeric_string) for numeric_string in raw_input().split(" ")]

insertSearch(desired_array)