---
title: LeetCode - validate-binary-search-tree challenge solution
author: tzookb
type: post
date: 2020-07-11T09:07:08+00:00
url: /leetcode/validate-binary-search-tree
desc: leetcode validate-binary-search-tree exercise
source: https://leetcode.com/problems/validate-binary-search-tree/
---

This one is quite nice, and you should know how to play around with trees.
The exercise is to validate this is a binary search tree.
That means items on the left are smaller than the head, and items on the right are larger than the head.
The above rules should be valid all down the tree path.

In the code below you code see several methods and I'll explain each one of them.

First we start with `isValidBST` this is our exercise method that will return our solution.

### checkBasicNodeVals

is just a helper that will just check that our node and its children adhere to our rules.

### isValidBSThelper

Here is where most of the work happens, and this method will called recuresively .
for each node we will check for the `checkBasicNodeVals` first.
then we check for min val and that values are correct and do the same for max vals.

If we got to here, we will call the children and make sure to update the min, max for them as well.

```
class Solution(object):
    def isValidBST(self, root):
        return self.isValidBSThelper(root, None, None)

    def checkBasicNodeVals(self, root):
        if root is None:
            return True
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        return None

    def isValidBSThelper(self, root, min, max):
        base_result = self.checkBasicNodeVals(root)
        if base_result is not None:
            return base_result

        if min is not None:
            if root.left and root.left.val <= min:
                return False
            if root.right and root.right.val <= min:
                return False
        if max is not None:
            if root.left and root.left.val >= max:
                return False
            if root.right and root.right.val >= max:
                return False

        return (
            self.isValidBSThelper(root.left, min, root.val) and
            self.isValidBSThelper(root.right, root.val, max)
        )
```
