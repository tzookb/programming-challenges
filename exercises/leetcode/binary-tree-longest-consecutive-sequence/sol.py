# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.max_count = 0
        def recu(cur, prev_val, count):
            self.max_count = max(self.max_count, count)

            if not cur:
                return
            
            if cur.val == prev_val + 1:
                recu(cur.left, cur.val, count + 1)
                recu(cur.right, cur.val, count + 1)
            else:
                # fresh
                recu(cur.left, cur.val, 1)
                recu(cur.right, cur.val, 1)

        recu(root, float("inf"), 0)

        return self.max_count
        