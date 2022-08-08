from typing import Counter, List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = self.inorder(root)
        left = 0
        right = len(arr) - 1
        while left < right:
            summed = arr[left] + arr[right]
            if summed > k:
                right -= 1
            elif summed < k:
                left += 1
            else:
                return True

        return False

    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        final = []
        def recu(node: Optional[TreeNode]):
            if not node:
                return None
            recu(node.left)
            final.append(node.val)
            recu(node.right)
        recu(root)
        return final
