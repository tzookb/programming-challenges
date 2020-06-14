from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        checks = [[root]]
        maxes = []

        while checks:
            check = checks.pop(0)
            vals = []
            nextRound = []
            for node in check:
                vals.append(node.val)
                if node.left:
                    nextRound.append(node.left)
                if node.right:
                    nextRound.append(node.right)

            maxes.append(max(vals))
            if nextRound:
                checks.append(nextRound)
            
        return maxes
