# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, node: TreeNode, L: int, R: int) -> int:
        if not node:
            return 0

        total = 0
        if R >= node.val >= L:
            total += node.val
            
        total += self.rangeSumBST(node.left, L, R)
        total += self.rangeSumBST(node.right, L, R)
        
        return total
