from typing import List
class Solution:
    def recu(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        ran = {}
        final = []
        for idx, num in enumerate(nums):
            if num in ran:
                continue
            start = nums[0:idx]
            end = nums[idx+1:]
            nexts = start + end
            results = self.recu(nexts)
            for res in results:
                final.append([num] + res)
            if not results:
                final.append([num])
            ran[num] = True
        return final

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.recu(nums)

s = Solution()
res = s.permuteUnique([1,1,2])
print(res)

