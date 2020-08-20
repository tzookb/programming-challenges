class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.longest = 0
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            pathSum = left + right
            if pathSum > self.longest:
                self.longest = pathSum
            return max(left, right) + 1
        depth(root)
        return self.longest
        