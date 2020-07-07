---
title: LeetCode - remove element challenge solution
author: tzookb
type: post
date: 2020-07-06T13:50:08+00:00
url: /leetcode/remove-element
desc: leetcode remove element exercise
source: https://leetcode.com/problems/remove-element/
---

This question is relatively easy but you need to think of it a bit before you solve it. When I solved it by myself I went with the approach of switching a "found" element with the end. The end index will move back in case it switched.

My code wasnt that nice, but it worked.
After making sure my solution passes I looked at the docs on the proposed solution. The idea was exactly like mine but the implemented code was much cleaner.

## Switch with the end

```
def removeElement(nums, val):
    i = 0
    j = len(nums)
    while i < j:
        if nums[i] == val:
            nums[i] = nums[j-1]
            j -= 1
        else:
            i += 1
    return j
```

As you can see we start from the first element, and the "replace" element starts from the end. When ever the current element equals to our unwanted value, we switch it with the end idx. When switched we decrement the end idx by one.

If the value is different we just move forward to the next item.

## 2 pointers switch

```
def removeElement(nums, val):
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i
```

The above code was the second option mentioned, and this does is switching element each time we find the "bad" value. So if the value is in the beginning like:
`[X, 1, 2, 3, ...n]`
We will do a switch for each element after X.
