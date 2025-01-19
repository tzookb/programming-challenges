# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        diff = float("inf")

        bfs = [(root, float("-inf"), float("inf"))]
        while bfs:
            cur, mininf, maxinf = bfs.pop(0)
            if not cur:
                continue
            
            diff = min(
                diff,
                abs(cur.val - mininf),
                abs(maxinf - cur.val),
            )
            
            bfs.append((cur.left, mininf, cur.val))
            bfs.append((cur.right, cur.val, maxinf))
            
        return diff