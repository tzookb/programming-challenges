---
title: LeetCode - search insert position challenge solution
author: tzookb
type: post
date: 2020-07-06T13:50:08+00:00
url: /leetcode/search-insert-position
desc: leetcode search-insert-position exercise
source: https://leetcode.com/problems/search-insert-position/
---

This exercise was super simple to solve. It was so straightforward as I started doubting myself as I'm totally off.

The solution I did is iterating through all the elements in the worst case, as it goes one by one over n items.

I'm sure there is another solution that will may imporve the runtime.
Just because we know the list is sorted so instead of starting from the beginning we can start from the middle and then jump to the right or left middle depends on our value. Just like binary search algorithm.

```
def searchInsert(nums, target):
    idx = 0
    while idx < len(nums):
        cur = nums[idx]
        if target <= cur:
            return idx
        idx += 1
    return idx
```

As you can see we start from the beginning, and if the current value is bigger or equal from our target, we return the current index.
If we got to the end of the loop, that means our target is bigger then all the values in the array so we return the end of the array index.
