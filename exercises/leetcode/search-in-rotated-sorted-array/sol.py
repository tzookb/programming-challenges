from typing import List

class Solution:    

    def find_rotate_index(self, nums):
        if nums[0] < nums[-1]:
            return 0
        left = 0
        right = len(nums) - 1
        if right == 1:
            return 1

        while left <= right:
            mid = left + (right - left) // 2
            # print(left,right,mid)
            if nums[mid] > nums[mid + 1]:
                return mid + 1
            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid
        return left

    def binary_search(self, nums, target, sleft, sright):
        left = sleft
        right = sright

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

        # 1,2,3,4,5

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        rotate_idx = self.find_rotate_index(nums)
        rotate_val = nums[rotate_idx]

        if rotate_val == target:
            return rotate_idx

        if rotate_idx == 0:
            left = 0
            right = len(nums) - 1
        elif target < nums[0]:
            left = rotate_idx
            right = len(nums) - 1
        else:
            left = 0
            right = rotate_idx - 1

        return self.binary_search(nums, target, left, right)
        

sol = Solution()
res = sol.search([8,9,2,3,4], 9)
print(res)


