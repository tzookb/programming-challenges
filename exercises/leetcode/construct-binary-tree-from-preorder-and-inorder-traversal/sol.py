# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        head = preorder[0]
        head_index = inorder.index(head)

        left_inorder = inorder[0:head_index]
        right_inorder = inorder[head_index+1:]
        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder):]

        left_branch = self.buildTree(left_preorder, left_inorder)
        right_branch = self.buildTree(right_preorder, right_inorder)
        tree = TreeNode(
            head,
            left_branch,
            right_branch
        )

        return tree
