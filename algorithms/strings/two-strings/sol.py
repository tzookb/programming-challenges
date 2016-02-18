def intersected(st1, st2):
	st1 = list(st1)
	st2 = list(st2)
	uniques = set(st1+st2)
	return len(set(st1))+len(set(st2))>len(uniques)

tests = int(raw_input())

for i in xrange(tests):
	
	if intersected(raw_input(), raw_input()):
		print 'YES'
	else:
		print 'NO'
