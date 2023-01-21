# target-sum

https://leetcode.com/problems/target-sum

## brief

- dynamic programming route
- start with the empty option, only option is sum 0, and one way to get to it
- now loop over each number
- each number will take our dp to the next step
- for each number loop over the current dp sums
- for each dp sum, add and sub the current item
- set the above sums to the next dp, and increase the ways of doing it
- return the sums for the target