
def isFunny(str):
	reversed = str[::-1]
	length = len(str)

	for i in xrange(1, length):
		if abs(ord(str[i]) - ord(str[i-1])) != abs(ord(reversed[i]) - ord(reversed[i-1])):
			return 'Not Funny'
	return 'Funny'



numOfTest = int(raw_input())

for i in xrange(numOfTest):
	print isFunny(raw_input())