import re

def findThedHackerrank(phrase):

	res = re.findall( r'([^_]foo[^_])', phrase)

	if res:
		print len(res)
	else:
		print 'not found'

		
	



print findThedHackerrank("foo bar (foo) bar foo-bar foo_bar foo'bar bar-foo bar, foo.")