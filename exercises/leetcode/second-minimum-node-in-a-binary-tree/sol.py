# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        values = set()
        nodes = [root]
        while nodes:
            n = nodes.pop(0)

            values.add(n.val)
            if n.left:
                nodes.insert(0, n.right)
                nodes.insert(0, n.left)

        if len(values) < 2:
                return -1
        
        firstMin = min(values)
        values.remove(firstMin)
        return min(values)