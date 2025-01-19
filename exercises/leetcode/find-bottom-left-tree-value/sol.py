# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        cur_row = -1
        cur_value = None
        bfs = [(root, 0)]

        while bfs:
            item, row = bfs.pop(0)
            if not item:
                continue
            if row != cur_row:
                cur_row = row
                cur_value = item.val
            
            bfs.append((item.left, row + 1))
            bfs.append((item.right, row + 1))
        
        return cur_value