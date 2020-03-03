
import re

def isPangram(str):
	NUM_OF_LETTER_IN_ABC = 26

	str = str.lower()
	regex = re.compile('[^a-z]')
	str = regex.sub('', str)
	str = list(set(str))

	if len(str) == NUM_OF_LETTER_IN_ABC:
		return 'pangram'
	return 'not pangram'
	

print isPangram(raw_input())
