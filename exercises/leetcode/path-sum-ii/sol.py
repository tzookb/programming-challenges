from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        paths = []
        def findPathRecu(head: TreeNode, curSum: int, curPath: List[int]):
            nonlocal paths
            if head is None:
                return
            if head.left is None and head.right is None:
                if head.val + curSum == targetSum:
                    found_path = curPath + [head.val]
                    paths.append(found_path)
            else:
                next_sum = curSum + head.val
                next_path = curPath + [head.val]
                findPathRecu(head.left, next_sum, next_path)
                findPathRecu(head.right, next_sum, next_path)

        findPathRecu(root, 0, [])
        return paths
