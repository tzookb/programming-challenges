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
    def maxPathSumRec(self, root: TreeNode) -> int:
        if not root:
            return 0

        leftMax = self.maxPathSumRec(root.left)
        rightMax = self.maxPathSumRec(root.right)

        return max([
            leftMax,
            leftMax + root.val,
            root.val,
            rightMax,
            rightMax + root.val,
        ])

    def maxPathSum(self, root: TreeNode) -> int:
        return self.maxPathSumRec(root)
        

root = TreeNode(1)
root_left = TreeNode(2)
root_right = TreeNode(5)
root_left_left = TreeNode(3)
root_left_right = TreeNode(4)
root_right_right = TreeNode(-6)

#      1
#   2     5
# 3   4     6
root.left = root_left
root.right = root_right
root_left.left = root_left_left
root_left.right = root_left_right
root_right.right = root_right_right

s = Solution()
res = s.maxPathSum(root)
print(res)