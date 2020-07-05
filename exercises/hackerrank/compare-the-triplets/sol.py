def calc(A, B):
	alice = bob = 0
	for index in range(3):
		if A[index] > B[index]: bob += 1
		elif A[index] < B[index]: alice += 1
	print bob, alice	

# res = calc(map(int, raw_input().split(" ")), map(int, raw_input().split(" ")))

print (1-3)%4