# construct-string-with-repeat-limit

https://leetcode.com/problems/construct-string-with-repeat-limit

- count characters
- create a max heap with (char, count)
	- the char will be the comparator, as we need "z" to pop earlier than "a"
- create a "final" string builder for you final result
- loop while the heap is not empty
	-  get the max item
	-  check if it eqauls the final last added item
		-  if not:
			-  add the current char up to the repeat limit or the count it has (min between them)
			-  subsctract the added count from the char count, if its bigger than 0
				-  add the char back to the heap, with the reduced count
		-  if the match:
			-  check if heap is empty, if so break, as we cant add more chars to final
			-  if not empty, pop the last item again
				-  now add a a single occurance of this char, as we want to add more of the initial char, because its lexicographically bigger
				-  if the sec char count reduced by one is not zero, push it back to the heap
				-  push back the initial char to the heap without changing its count