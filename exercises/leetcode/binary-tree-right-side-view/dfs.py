from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        nodes = [(root, 1)]
        rightView = []

        while nodes:
            node, height = nodes.pop(0)
            if not node:
                continue
            if height > len(rightView):
                rightView.append(node.val)
            nodes.insert(0,(node.left, height + 1))
            nodes.insert(0,(node.right, height + 1))

        return rightView
            
            

s = Solution()
s.rightSideView('xxxx')