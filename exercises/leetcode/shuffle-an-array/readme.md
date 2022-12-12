# shuffle-an-array

https://leetcode.com/problems/shuffle-an-array

## brief

- "reset" is easy, we just make sure to have the original stored and never touched to be returned
- "shuffle" logic is:
  - copy original array
  - run a loop n times with i position
  - generate a random index in the array
  - replace the random_idx value with i value
  - return the updated array
