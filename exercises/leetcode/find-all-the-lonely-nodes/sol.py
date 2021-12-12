from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        sol = []

        def recu(node: TreeNode, is_lonely):
            if not node:
                return
            
            if is_lonely:
                sol.append(node.val)
            
            next_lonely = False if node.left and node.right else True

            recu(node.left, next_lonely)
            recu(node.right, next_lonely)

        recu(root, False)
        return sol


