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
        curLevel = 1
        curVals = []
        rightView = []

        while nodes:
            node, height = nodes.pop(0)
            if not node:
                continue
            if curLevel != height:
                rightView.append(curVals[-1])
                curVals = []
                curLevel = height
            curVals.append(node.val)

            nodes.append((node.left, height + 1))
            nodes.append((node.right, height + 1))

        if curVals:
            rightView.append(curVals[-1])

        return rightView
            
            

s = Solution()
s.rightSideView('xxxx')