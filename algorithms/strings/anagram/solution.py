def checkAnagram(str):
	if len(str)%2 == 1:
		return -1

	firstpart = list(str[:len(str)/2])
	secondpart = list(str[len(str)/2:])

	needToChangeCounter = 0

	for charInFirst in firstpart:
		try:
			secondpart.remove(charInFirst)
		except ValueError:
			needToChangeCounter += 1
	
	return needToChangeCounter	

numOfTests = int(raw_input())
i = 0
while i < numOfTests:
	i += 1
	print checkAnagram(raw_input())