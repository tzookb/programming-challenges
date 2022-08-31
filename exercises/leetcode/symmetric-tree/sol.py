# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        vals = []
        nodes = []
        cur = root
        while True:
            if cur:
                nodes.append(cur)
                cur = cur.left
            elif nodes:
                vals.append(None)
                cur = nodes.pop()
                vals.append(cur.val)
                cur = cur.right
            else:
                break

        if len(vals) % 2 == 0:
            return False
        
        mid_idx = len(vals) // 2
        left = vals[:mid_idx]
        right = vals[mid_idx+1:]
        right.reverse()
        print(left, right)
        return left == right