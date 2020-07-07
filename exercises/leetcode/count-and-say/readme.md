---
title: LeetCode - count-and-say challenge solution
author: tzookb
type: post
date: 2020-07-07T21:07:08+00:00
url: /leetcode/count-and-say
desc: leetcode count-and-say exercise
source: https://leetcode.com/problems/count-and-say/
---

This challenge may be "easy" but it was quite challenging, for me at least.

My solution was first creating a function that will create the next string from an existing string.

So when it gets "1" => "11", "11" => "21", "1211" and so on.

It took me some time to understand how this syntax work wo I'll try to explainit here.
For n=1, the string is "1", that's our base case.
For next n+1, is the "string representative of n.

So in case of n=2, that is the string represantive of n=1.
n=1, is "1". How we describe "1", its "count"+"value" so "11".

Now let's show n=3, that is the string represantive of n=2, that is "11".
so "11" is "count"+"value" so "2"+"1" => "21".

Lets do 4 and 5.

n=4, string represantive of n=3, that is "21".
So "21" => "count"+"value" so "1211".

n=5, string represantive of n=4, that is "1211".
So "1211" => "count"+"value" so "111221".

Let me explain n=5 in words, n=5 is the string represantive of n=4.
n=4 is "1211", in words is:

- one time the digit one
- one time the digit two
- two times the digit one
- let's convert the above to numbers:
- 11
- 12
- 21
- lets merge them to a single string:
- 111221
- and that is our result for n=5

Now after we got the idea of how to calculate the string, lets get to the solution of our exercise.

```
def countAndSay(self, n: int) -> str:
    val = "1"
    i = 1
    while i < n:
        val = self.calcNext(val)
        i += 1
    return val
```

As you can Im starting from the base and get my way up until I get to the requested "n" result.
One each iteration I'm calculating the next "representation" until I reach to the desired n, stop and return it.
This is pretty easy, but let me share the code for generating the "string representation".

```
def calcNext(self, n: str) -> str:
    count = 0
    prev = -1
    res = []
    for i in range(len(n)):
        cur = n[i]
        if cur == prev:
            count += 1
        else:
            if count:
                res.append(str(count))
                res.append(prev)
            count = 1
            prev = cur
    if count:
        res.append(str(count))
        res.append(prev)
    return ''.join(res)
```

This is a bit more complex, and I saw other solution that were much shorter.
But I always prefer to have code that is a bit more readable than having one liner tricks that make it harder to understand.