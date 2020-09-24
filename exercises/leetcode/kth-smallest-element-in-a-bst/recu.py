class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.cur_item = 0
        self.cur_count = 0
        self.ans = -1

        def inorder(node):
            if self.cur_count == k:
                return
            if node is None:
                return
            inorder(node.left)
            self.cur_count += 1
            self.cur_item = node.val
            if self.cur_count == k:
                self.ans = self.cur_item
            inorder(node.right)

        inorder(root)
        return self.ans