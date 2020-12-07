
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def recu(node, isLeft):
            if not node:
                return 0
            
            if not node.left and not node.right and isLeft:
                return node.val

            return recu(node.left, True) + recu(node.right, False)
        return recu(root, False)