

def getDivisableDigits(n):
	stringN = str(n)
	sumOfDividerDigits = 0

	for digit in stringN:
		digitVal = int(digit)
		if (digitVal == 0): continue
		if ( n % digitVal == 0):
			sumOfDividerDigits += 1

	return sumOfDividerDigits
		
	
amountOfTests = int(raw_input())
i = 0
while i < amountOfTests:
	i += 1
	n = int(raw_input())	
	res = getDivisableDigits(n)
	print res