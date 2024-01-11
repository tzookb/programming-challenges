from typing import List, Dict, Tuple

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        distinct_subarrays = set()

        size = len(nums)
        for i in range(size):
            cur_divises = 0
            for j in range(i, size):
                cur = nums[j]
                if cur % p == 0:
                    cur_divises += 1 
                if cur_divises > k:
                    break
                
                distinct_subarrays.add(tuple(nums[i:j+1]))

        return len(distinct_subarrays)


s = Solution()
res = s.countDistinct([2,3,3,2,2], 2, 2)
print(res)