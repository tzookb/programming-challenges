from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        new_tree = None
        
        def copy(t1, t2):
            if t1 is None and t2 is None:
                return None
            val = 0
            if t1 is not None and t2 is not None:
                val = t1.val + t2.val
            elif t1 is not None:
                val = t1.val
            else:
                val = t2.val

            next_right_call1 = t1.right if t1 else None
            next_right_call2 = t2.right if t2 else None
            
            next_left_call1 = t1.left if t1 else None
            next_left_call2 = t2.left if t2 else None
            
            generated_right = copy(next_right_call1, next_right_call2)
            
            generated_left = copy(next_left_call1, next_left_call2)
            
            new_tree = TreeNode(val, generated_left, generated_right)
            
            return new_tree
        return copy(root1, root2)