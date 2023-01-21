# first-missing-positive

https://leetcode.com/problems/first-missing-positive

## Intuition

We have two crucial constrains, $$O(n)$$ time complexity and no extra space allowed.
Without the two constrains, this problem will be easy.
That lead me to think on how I can use limited space or use the exisiting space. For time complexity, I will need to go over the array a constant amount of times.

## Approach

- we know that in a list of size N, the missing number will be from 1 to N + 1, no other option.
- for finding the first missing positive, we can ignore negatives and zeros, so lets zero all of them.
- Now lets run through the loop and mark the cells that have a corresponding item with a negative value
- for each item, we check if its 0, is so, keep on going
- if it has a value, get the absolute value (as it can be negative)
- calculate the actual position in the array `(NUM - 1) === idx`
- mark the index with negative value 
- negative values means the item that suppose to be in this position, exists in the list
- in case the value in the position is 0, we can't set it to -0
- so we set it to negative value of its number for that position
- Now let's loop for the last time, and in the first occurance where the value is bigger or equal to one, return the idx plus one
- if none found, return the last possible missing item

## Complexity

- Time complexity:
- $$O(n)$$
- we fully loop the array 3 times, but that still means liner complexisty

- Space complexity:
- $$O(1)$$
- as we are not using any new memory
- but reusing the existing memory we have

## Code

```
from typing import Counter, List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # zero negative numbers or too big numbers
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
            if nums[i] > len(nums):
                nums[i] = 0
        
        # mark found numbers as negatives by positions
        for i in range(len(nums)):
            cur = nums[i]
            if cur == 0:
                continue
            real_pos = abs(cur) - 1
            if nums[real_pos] > 0:
                nums[real_pos] *= -1
            elif nums[real_pos] == 0:
                nums[real_pos] = -(real_pos + 1)
            nums[real_pos] = nums[real_pos] if nums[real_pos] < 0 else -nums[real_pos]

        # find the missing one
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1

        return len(nums) + 1

```
