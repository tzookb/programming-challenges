---
title: LeetCode - implement strstr challenge solution
author: tzookb
type: post
date: 2020-07-06T13:50:08+00:00
url: /leetcode/implement-strstr
desc: leetcode implement-strstr exercise
source: https://leetcode.com/problems/implement-strstr/
---

`strstr` is a super useful function most of us use without  appreciating the code behind it. This is my approach on implementing the solution.

Just wanted to mention as I recently did a lot of recursions and dynamic programming I almost tried to use that approach, but in the end I went with the "simple" approach.

So the general idea is I'll be iterating over each char in the haystack, when I find a char that equals to the first character in the needle. I'll start another loop to compare the rest with what is left with the needle.

If I failed in one of those comparisons, I'll go back to where I started and look again for the first character in the needle and start the process again.

Important note is I'm checking the needle length and the length of what I have left with the haystack as if haystack leftover is smaller, so we will surely wont find a solution so we can exit out.

```
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[0]:
                j = i
                needIdx = 0
                if len(haystack[i:]) < len(needle):
                    return -1
                while j < len(haystack):
                    if haystack[j] != needle[needIdx]:
                        break
                    if needIdx == len(needle)-1:
                        return i
                    needIdx += 1
                    j += 1
            i += 1
        return -1
```
