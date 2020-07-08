---
title: LeetCode - assign-cookies challenge solution
author: tzookb
type: post
date: 2020-07-07T09:07:08+00:00
url: /leetcode/assign-cookies
desc: leetcode assign-cookies exercise
source: https://leetcode.com/problems/assign-cookies/
---

This is based on the "greedy algorithm". But its relativelly easy todo.
First we sort the cookies and children. I did in a descending order. But I think its not relevant here, as we are trying to find the amount of happy children and not fit exact numbers.

So after we sorted out we just iterate until we are out of children or cookies.
We will change the cookie index each time we find a match with c child.

In the end the amount happy children with be the cookie index, as it incremented each time we found a cookie-child match.

```
def findContentChildren(g: List[int], s: List[int]) -> int:
    g.sort(reverse=True)
    s.sort(reverse=True)
    cookieIdx = childIdx = 0
    while childIdx < len(g) and cookieIdx < len(s):
        if g[childIdx] <= s[cookieIdx]:
            cookieIdx += 1
        childIdx += 1
    return cookieIdx
```
