# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        mid = len(nums) // 2
        left_arr = nums[:mid]
        right_arr = nums[mid+1:]

        left = self.sortedArrayToBST(left_arr)
        right = self.sortedArrayToBST(right_arr)
        return TreeNode(nums[mid], left, right)