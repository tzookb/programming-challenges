import re

def findThedHackerrank(phrase):
	res = re.findall( r'<a [^>]*\s*>(<[^>]*>)*([^<]*)(<\/[^>]+>)*', phrase)

	if res:
		results = []
		for item in res:
			results.append(item[1])
		return results
	
	return []

		
	


print findThedHackerrank('<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p><div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>')