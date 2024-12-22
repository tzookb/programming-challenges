# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        cur_level = 1
        final = []
        items = []

        queue = [(root, cur_level)]

        while queue:
            cur, level = queue.pop(0)
            if not cur:
                continue
            
            if level != cur_level:
                final.append(items.copy())
                items = []
                cur_level = level
            
            items.append(cur.val)
            queue.append((cur.left, level + 1))
            queue.append((cur.right, level + 1))
        
        if items:
            final.append(items)
        
        return final[::-1]
        