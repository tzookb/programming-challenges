# partition-string-into-substrings-with-values-at-most-k

https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k

## brief

- this will be a greedy approach
- we start from the left and keep adding chars to the current substring
- we will try to add chars until we reach the max value
- if we surpass the max value, we will start a new substring, and add a counter