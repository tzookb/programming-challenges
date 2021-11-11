from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getProcessor(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root.right:
            return None
        cur = root.right
        while cur.left:
            cur = cur.left
        return cur.val

    def getPredecessor(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root.left:
            return None
        cur = root.left
        while cur.right:
            cur = cur.right
        return cur.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.getProcessor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.getPredecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root
