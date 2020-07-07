---
title: LeetCode - length-of-last-word challenge solution
author: tzookb
type: post
date: 2020-07-07T21:07:08+00:00
url: /leetcode/length-of-last-word
desc: leetcode length-of-last-word exercise
source: https://leetcode.com/problems/length-of-last-word/
---

This one was super easy at least after you understand the edge cases.

So I just trimmed the input string in case we get a string with whitespace in end.

After that, we split the sentence into words, take the last word and return the length of it.

```
def lengthOfLastWord(self, s: str) -> int:
    lastWord = s.strip().split(" ")[-1]
    return len(lastWord)
```