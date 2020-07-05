class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        items_dict = {}
        for idx, num in enumerate(nums):
            partner = target - num
            if partner in items_dict:
                return [items_dict[partner], idx]
            items_dict[num] = idx
        return []
            