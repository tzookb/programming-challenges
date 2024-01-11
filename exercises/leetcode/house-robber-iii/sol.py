from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def recu(node: Optional[TreeNode]):
            if not node:
                return [0, 0]

            left = recu(node.left)
            right = recu(node.right)

            val_with_cur = node.val + left[1] + right[1]
            val_without_cur = max(left) + max(right)

            return [val_with_cur, val_without_cur]

        return max(recu(root))
