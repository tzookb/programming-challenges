# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(left: TreeNode, right: TreeNode):
            if not left and not right:
                return True
            if (not left and right) or (not right and left):
                return False
            if left.val != right.val:
                return False
            
            return (
                check(left.left, right.right)
                and
                check(left.right, right.left)
            )
        if not root:
            return True
        return check(root.left, root.right)