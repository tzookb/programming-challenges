from typing import Counter, Dict, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def checkContainsOne(node: Optional[TreeNode]):
            if not node:
                return False
            leftside_has_one = checkContainsOne(node.left)
            rightside_has_one = checkContainsOne(node.right)
            am_i_one = node.val == 1
            if not leftside_has_one and not rightside_has_one and not am_i_one:
                return False
            
            if not leftside_has_one:
                node.left = None
            if not rightside_has_one:
                node.right = None

            return True


        is_root_contains_one = checkContainsOne(root)
        if not is_root_contains_one:
            return None
        return root