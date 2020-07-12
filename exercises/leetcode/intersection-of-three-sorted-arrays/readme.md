---
title: LeetCode - intersection-of-three-sorted-arrays challenge solution
author: tzookb
type: post
date: 2020-07-11T09:07:08+00:00
url: /leetcode/intersection-of-three-sorted-arrays
desc: leetcode intersection-of-three-sorted-arrays exercise
source: https://leetcode.com/problems/intersection-of-three-sorted-arrays/
---

This one I tried doing in a very simple approach. As the questions askes to merge 3 arrays into a single array.
That is the same like merging arrays A and B to => Z and then merge the result Z to array C and thats your answer.

This would work the same with n arrays, but instead of hardcoding the merged arrays you can just use a loop.

So Lets start from merging two array, well more accurately intersecting two arrays.
Luckily the arrays are sorted so we can just do it in O(n|m) as n,m are the lengths of the arrays.
We simply start from the beginning of each array, then we slowly progress by comparing the values.
If one is smaller then the other we increase its index, if the are equal we increment both indexes.

```
def intersectTwoArrys(self, arr1: List[int], arr2: List[int]) -> List[int]:
    newArr = []
    i1 = i2 = 0
    while i1 < len(arr1) and i2 < len(arr2):
        v1 = arr1[i1]
        v2 = arr2[i2]
        if v1 == v2:
            newArr.append(v1)
            i1 += 1
            i2 += 1
            continue
        if v1 > v2:
            i2 += 1
        else:
            i1 += 1
    return newArr
```

So after we have the above solution for merging the intersection of two arrays. Here is the final solution for this question.

```
def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    arr12 = self.intersectTwoArrys(arr1, arr2)
    return self.intersectTwoArrys(arr12, arr3)
```
