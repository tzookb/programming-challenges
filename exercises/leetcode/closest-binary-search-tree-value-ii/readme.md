# closest-binary-search-tree-value-ii

https://leetcode.com/problems/closest-binary-search-tree-value-ii

## brief

- create a max heap that will store max K items
- go through the tree one by one
- get diff from current node value and target
- check if diff is smaller then our head in the heap
- if so, pop the heap, and insert the current diff and its value
- return only the values
