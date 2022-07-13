from typing import List
class Solution:
    def getBinRepAsList(self, num: int, minLength: int) -> List[bool]:
        bin_rep = "{0:b}".format(num)
        cur_len = len(bin_rep)
        extra = "0" * (minLength - cur_len)
        final = extra + bin_rep
        return list(map(lambda x: x == "1", list(final)))

    def getMatches(self, nums: List[int], selectors: List[bool]):
        res = []
        for selector, num in zip(selectors, nums):
            if not selector:
                continue
            res.append(num)
        return res
    
    def getKey(self, nums: List[int]):
        return "_".join(
            list(
                map(
                    lambda x: str(x), nums
                )
            )
        )

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        max_items = 2**len(nums)
        cur = 0
        matches = {}
        final = []

        while cur < max_items:
            bin_rep = self.getBinRepAsList(cur, len(nums))
            res = self.getMatches(nums, bin_rep)
            key = self.getKey(res)
            if key not in matches:
                matches[key] = True
                final.append(res)

            cur += 1

        return final

nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
s = Solution()
res = s.subsetsWithDup(nums)
print(res)