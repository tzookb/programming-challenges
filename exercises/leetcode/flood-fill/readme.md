---
title: LeetCode - flood-fill challenge solution
author: tzookb
type: post
date: 2020-07-07T09:07:08+00:00
url: /leetcode/flood-fill
desc: leetcode flood-fill exercise
source: https://leetcode.com/problems/flood-fill/
---

After reading some coding tips, it mentioned the "flood fill" algorithm.
So I decided to find one and try it. Doesn't seems complicated, but this is an "easy" level question.

My code is not the smallest, but I think its easy to read and that's what important on my perspective at least.

```
class Solution:
    def floodFillIfColor(self, image: List[List[int]], sr: int, sc: int, oldColor: int, newColor: int):
        if not (sr >= 0 and sr < len(image) and sc >= 0 and sc < len(image[0])):
            return

        if image[sr][sc] == newColor:
            return

        if image[sr][sc] != oldColor:
            return

        image[sr][sc] = newColor
        self.floodFillIfColor(image, sr-1, sc, oldColor, newColor) #top
        self.floodFillIfColor(image, sr+1, sc, oldColor, newColor) #bottom
        self.floodFillIfColor(image, sr, sc-1, oldColor, newColor) #left
        self.floodFillIfColor(image, sr, sc+1, oldColor, newColor) #right

        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.floodFillIfColor(image, sr, sc, image[sr][sc], newColor)
        return image
```

The function that does the real work is `floodFillIfColor`.

- It first checks if the point is in the boundries of the grid, if not we exit.
- Then we check if the current position is the same color as the new color, if so we skip the change.
- Then we check if the current color is different from the older color where we started the paint, if so exit out as well.
- if we got here, we update the color
- and call the "floodFillIfColor" for our top, right, bottom and left neighbours. 