# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def recu(node: Optional[TreeNode]):
            if not node:
                return 0
            left = recu(node.left)
            right = recu(node.right)
            
            self.longest = max(self.longest, left + right)

            return max(left, right) + 1
            
        recu(root)
        return self.longest