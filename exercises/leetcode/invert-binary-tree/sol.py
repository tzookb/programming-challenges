# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recu(node: Optional[TreeNode]):
            if not node:
                return
            node.left, node.right = node.right, node.left
            recu(node.right)
            recu(node.left)
        recu(root)
        return root
        