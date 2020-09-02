class Solution:

    def lowestCommonAncestor(self, node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ans = None

        def recu(node: TreeNode, p: TreeNode, q: TreeNode):
            if not node:
                return False
            
            mid = node.val == p.val or node.val == q.val
            left = recu(node.left, p, q)
            right = recu(node.right, p, q)

            if mid + left + right >= 2:
                self.ans = node
            
            return mid or left or right

        recu(node, p, q)
        return self.ans