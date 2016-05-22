import re

Test_String = """// this is a single line comment

x = 1; // a single line comment after code

/* This is one way of* w**riting comments */ 

/* This is a multiline 
   comment. These can often
**
   be useful*/"""

Regex_Pattern = r"(\/\*([^*\/]|[*]|[\r\n])*\*\/+)|(\/\/.+)"

matches = re.findall(Regex_Pattern, Test_String)

for match in matches:
	print match