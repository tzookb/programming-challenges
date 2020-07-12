---
title: LeetCode - next-greater-element-i challenge solution
author: tzookb
type: post
date: 2020-07-11T09:07:08+00:00
url: /leetcode/next-greater-element-i
desc: leetcode next-greater-element-i exercise
source: https://leetcode.com/problems/next-greater-element-i/
---

This question was quite tricky, I would not take credit on the cool solution as I solved it only with the brute force way.
But after reading the stack solution, I went ahead and implemented it myself.

The exercise here is that you get two arrays A & B.
For each item in A, you need to find it on B and then find the closest bigger element on its right.
If you could not find a bigger element on the right the solution for this element will be -1.

In the end you need to return a new array of the found bigger elements and -1's.
Example:

```
A = [1, 2, 3]
B = [4, 1, 0, 2, 3, -1]
```
Lets start finding the elements:

- For A[0], 1 we find it on B[1]. The first bigger elemnt on its right is B[3], 2.
- For A[1], 2 we find it on B[3]. The first bigger elemnt on its right is B[4], 3.
- For A[2], 3 we find it on B[4]. It has no bigger elements on its right, so -1.
- The solution: [2, 3, -1]

Now I'll share the two solutions.

## Brute Force

- iterate on array A
- for each element `a`
  - find its index on array B
  - from that index and further you iterate on array B items
  - for each item on B, `b`
    - check if `b > a`
    - if so save `b` for our final array
    - if we finished our iterations and found nothing, let's save `-1` for our final solution
- finish our iterations, the result is our saved array with the found items.

As you can see in this solution on the worst case scenarion we will be O(n^2)

The code:

```
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    nextGreater = []
    idx = 0
    while idx < len(nums1):
        num1 = nums1[idx]
        found = False
        secIdx = nums2.index(num1) + 1
        while secIdx < len(nums2):
            num2 = nums2[secIdx]
            secIdx += 1
            if num2 > num1:
                nextGreater.append(num2)
                found = True
                break
        idx += 1
        if not found:
            nextGreater.append(-1)
    return nextGreater
```

## Stack

- create a stack `s`
- create mappings dict `m`
- for `b` in array `B`
  - if `s` is empty, insert into it and continue the loop
  - if head of `s` is bigger than `b`
    - push `b` to `s` and continue the loop
  - start popping items from `s`, as long as they are smaller than `b`
    - for each popped item `p`
    - set its mapping on `m`
    - `m[p] = b`
  - as we finished with the popped items, we insert `b` into `s`
- now we just need to go over the items left in `s`
  - as for each one of them we could not find a bigger element on its right
  - so we set its mapping to -1

The code:

```
class Solution:
    def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
        mappings = {}
        stack = deque()

        for num in nums2:
            if not stack:
                stack.append(num)
                continue
            if stack[-1] > num:
                stack.append(num)
                continue
            while stack and stack[-1] < num:
                item = stack.pop()
                mappings[item] = num
            stack.append(num)

        while stack:
            item = stack.pop()
            mappings[item] = -1

        return list(map(lambda x: mappings[x], nums1))
```
