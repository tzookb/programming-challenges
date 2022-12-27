# sort-list

https://leetcode.com/problems/sort-list

## brief

- we will implement merge sort but with a linked list
- create helper functions:
  - splitList: will split a list into two in the middle, will return start of the two lists. Important to cut the left list end from the right list.
  - mergeLists: will take two sorted lists and return a single sorted list
- create a helper recursion func
  - return the node if its None or a single element list
  - split the list into two lists
  - mergeSort each side recursively
  - merge the results and return the result