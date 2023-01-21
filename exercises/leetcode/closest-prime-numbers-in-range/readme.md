# closest-prime-numbers-in-range

https://leetcode.com/problems/closest-prime-numbers-in-range

## brief

- create a helper function for checking if a number is prime
- create variable that will contain the min diff (starts with max int)
- create a variable that will contain the no result pair
- create a variable that will contain the prev prime number, will start with infinity
- run through the range
  - if not prime, continue
  - get the absulute diff between the current number and the prev prime number
  - compare with the min diff, if bigger continue
  - update the min diff
  - update the pair
  - if diff is smaller than 2, return the pair early
  - update prev to current
- return the pair you found
