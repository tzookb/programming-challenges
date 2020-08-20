# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        def depth(node, path):
            if not node:
                return
            curPath = path[::]
            curPath.append(node.val)

            if not node.left and not node.right:
                return paths.append(curPath)

            if node.left:
                depth(node.left, curPath)
            if node.right:
                depth(node.right, curPath)
            
        depth(root, [])
        res = ["->".join([str(pathStep) for pathStep in pathItems]) for pathItems in paths]
        return res
        