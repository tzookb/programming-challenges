# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_to_arr(tree):
    final = []
    stack = [tree]
    while stack:
        cur = stack.pop(0)
        if not cur:
            final.append(None)
            continue
        final.append(cur.val)
        stack.append(cur.left)
        stack.append(cur.right)
    return stack

class Solution:
    
    def flattenTree(self, node):
        
        # Handle the null scenario
        if not node:
            return None
        
        # For a leaf node, we simply return the
        # node as is.
        if not node.left and not node.right:
            return node
        
        # Recursively flatten the left subtree
        leftTail = self.flattenTree(node.left)
        
        # Recursively flatten the right subtree
        rightTail = self.flattenTree(node.right)
        
        # If there was a left subtree, we shuffle the connections
        # around so that there is nothing on the left side
        # anymore.
        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None
        
        # We need to return the "rightmost" node after we are
        # done wiring the new connections. 
        return rightTail if rightTail else leftTail
    
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.flattenTree(root)

root = TreeNode(1)
root_left = TreeNode(2)
root_right = TreeNode(5)
root_left_left = TreeNode(3)
root_left_right = TreeNode(4)
root_right_right = TreeNode(6)

root.left = root_left
root.right = root_right
root_left.left = root_left_left
root_left.right = root_left_right
root_right.right = root_right_right

s = Solution()
res = s.flatten(root)
print(tree_to_arr(root))