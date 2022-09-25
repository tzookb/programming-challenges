from typing import Counter, List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.keyed = {}
        def recu(node: Optional[TreeNode], val):
            if not node:
                return
            self.keyed[val] = True
            node.val = val
            recu(node.left, 2 * val + 1)
            recu(node.right, 2 * val + 2)
        recu(root, 0)
        self.root = root

    def find(self, target: int) -> bool:
        return target in self.keyed


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)