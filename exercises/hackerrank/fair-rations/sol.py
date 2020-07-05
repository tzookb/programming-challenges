
def fairRations(B):
	rations = 0
	i = 0
	while i < len(B):
		cur = B[i]
		if cur%2 == 0:
			i += 1
			continue
		B[i] += 1
		if i == len(B)-1:
			# we are in the end so not possible to ration
			return "NO"
		B[i+1] += 1
		rations += 2
		i += 1
	return rations

res = fairRations([2,3,4,5,6])
print(res)