
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        max_left = 1 + self.maxDepth(root.left)
        max_right = 1 + self.maxDepth(root.right)
        return max(max_left, max_right)