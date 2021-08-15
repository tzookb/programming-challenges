# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.failed = False

        def recu(head: Optional[TreeNode]) -> int:
            if self.failed:
                return 0
            if head is None:
                return 0
            
            left_size = recu(head.left) + 1
            right_size = recu(head.right) + 1

            if abs(left_size - right_size) > 1:
                self.failed = True
            
            return max(left_size, right_size)
        
        recu(root)

        return not self.failed
