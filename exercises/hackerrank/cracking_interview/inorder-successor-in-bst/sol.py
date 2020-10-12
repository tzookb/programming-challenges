# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        node = root
        stack = []
        found = False
        
        while True:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                if found:
                    return node
                if node.val == p.val:
                    found = True
                node = node.right
            else:
                break

        return None
        