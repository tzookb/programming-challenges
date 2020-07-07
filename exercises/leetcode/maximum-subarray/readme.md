---
title: LeetCode - maximum-subarray challenge solution
author: tzookb
type: post
date: 2020-07-07T09:07:08+00:00
url: /leetcode/maximum-subarray
desc: leetcode maximum-subarray exercise
source: https://leetcode.com/problems/maximum-subarray/
---

I know there are several options to solve this problem, but in the end I got with this approach.

As we only need to return the maximum sum of sub arrays, we dont need to return the subarray itself, 
so we can just follow the max value.

I'll be iterating over the array and for each item, I'll calculate if the current value
is higher then the value of the current + the previous sum.
Example array: [3, -1, 1]
so the max sum from left to right:

[3, 2, 3]

each index explained:

- 0: first cell so its only its value
- 1: the value alone is -1, but if we add the previous max sum, we will get -1 + 3 => 2
- 2: the value alone is 1, but if we add the previous max sum, we will get 1 + 2 => 3

So if we get the max from the above array we get 3