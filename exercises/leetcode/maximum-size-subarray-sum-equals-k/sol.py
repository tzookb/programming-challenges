from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix = [0]
        for num in nums:
            prefixed_sum = num + prefix[-1] 
            prefix.append(prefixed_sum)

        prefix_map = {}
        max_len = 0
        for rightidx in range(len(prefix)):
            right = prefix[rightidx]
            target = right - k
            if target in prefix_map:
                for idx in prefix_map[target]:
                    max_len = max(max_len, rightidx - idx)
            if right not in prefix_map:
                prefix_map[right] = set()
            prefix_map[right].add(rightidx)

        return max_len


s = Solution()
# res = s.maxSubArrayLen([1,-1,5,-2,3], 3)
res = s.maxSubArrayLen([-2,-1,2,1], 1)
print(res)