# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.final = 0
        def drill(prevmax, node):
            if not node:
                return

            if node.val >= prevmax:
                self.final += 1
                prevmax = node.val
            
            drill(prevmax, node.left)
            drill(prevmax, node.right)
        
        drill(float("-inf"), root)
        return self.final
        