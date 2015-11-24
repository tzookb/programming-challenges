def getDescentNumber(n):
	# f = num of fives
	# t = num of threes
	# n = f + t
	# we want the most 5's we can in a number
	
	threes = 0
	fives = 0
	digits = n

	while (digits > 0):
		if (digits % 3 == 0):
			fives = digits
			break
		digits -= 5
    
	threes = n - digits

	if (digits < 0 or threes % 5 != 0):
		return "-1"
    
	return "5"*fives + "3"*threes


res = getDescentNumber(14)

amountOfTests = int(raw_input())

i = 0

while i < amountOfTests:
	i += 1
	n = int(raw_input())	
	result = getDescentNumber(n)
	if result != -1 : 
		print result