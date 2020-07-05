# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# TODO
class Solution(object):
    def isValidBST(self, root):
        return self.isValidBSThelper(root, None, None)
    
    def checkBasicNodeVals(self, root):
        if root is None:
            return True
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        return None

    def isValidBSThelper(self, root, min, max):
        base_result = self.checkBasicNodeVals(root)
        if base_result is not None:
            return base_result
        
        if min is not None:
            if root.left and root.left.val <= min:
                return False
            if root.right and root.right.val <= min:
                return False
        if max is not None:
            if root.left and root.left.val >= max:
                return False
            if root.right and root.right.val >= max:
                return False
        
        return (
            self.isValidBSThelper(root.left, min, root.val) and
            self.isValidBSThelper(root.right, root.val, max)
        )
