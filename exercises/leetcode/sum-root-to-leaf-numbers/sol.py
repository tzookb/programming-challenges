# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0

        dfs = [(root, 0)]
        while dfs:
            cur, summed = dfs.pop()
            if not cur:
                continue
            
            if not cur.left and not cur.right:
                total += summed + cur.val
                continue
            
            next_sum = (summed + cur.val) * 10

            dfs.append((cur.left, next_sum))
            dfs.append((cur.right, next_sum))
        
        return total


        