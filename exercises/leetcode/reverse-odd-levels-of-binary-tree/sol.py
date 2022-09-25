from typing import Counter, List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def switch(a: TreeNode, b: TreeNode, level):
            if not a or not b:
                return
            if level % 2 == 1:
                a.val, b.val = b.val, a.val

            switch(a.left, b.right, level + 1)
            switch(a.right, b.left, level + 1)

        if not root:
            return root

        switch(root.left, root.right, 1)
        return root