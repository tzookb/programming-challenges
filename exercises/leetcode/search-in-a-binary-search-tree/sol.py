# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        if root.val == val:
            return root
        
        leftmatch = self.searchBST(root.left, val)
        if leftmatch:
            return leftmatch
        
        rightmatch = self.searchBST(root.right, val)
        return rightmatch
        