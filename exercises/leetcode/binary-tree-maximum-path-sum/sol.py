class Solution:
    def maxPathSumRec(self, node: TreeNode) -> int:
        if not node:
            return 0
        lmax = self.maxPathSumRec(node.left)
        rmax = self.maxPathSumRec(node.right)

        self.final = max(
            self.final,
            node.val,
            node.val + lmax,
            node.val + rmax,
            node.val + lmax + rmax
        )

        return node.val + max(lmax, rmax, 0)
        

    def maxPathSum(self, root: TreeNode) -> int:
        self.final = float("-inf")
        self.maxPathSumRec(root)
        return self.final
