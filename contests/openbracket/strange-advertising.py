import math

def shares(days):
	i = 1
	todayVisitors = 5
	likers = 0

	while i <= days:
		newLikers = math.floor(todayVisitors/2)
		todayVisitors = newLikers*3
		likers += newLikers
		i += 1
	return likers

print int(shares(int(raw_input())))