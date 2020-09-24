# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        nodes = [(root, 1)]
        curDepth = 1
        isReveresed = False
        curNodes = []
        results = []
        
        while nodes:
            node, depth = nodes.pop(0)
            if node is None:
                continue
            if depth != curDepth:
                if isReveresed:
                    curNodes = curNodes[::-1]
                results.append(curNodes)
                curNodes = []
                isReveresed = not isReveresed
                curDepth = depth
                pass

            curNodes.append(node.val)
            nodes.append((node.left, depth + 1))
            nodes.append((node.right, depth + 1))
        
        if curNodes:
            if isReveresed:
                curNodes = curNodes[::-1]
            results.append(curNodes)
        
        return results