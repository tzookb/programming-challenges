from typing import Counter, List, Optional
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        total_pairs = 0
        spare = 0

        for num in cnt:
            appears = cnt[num]
            
            total_pairs += appears // 2
            spare += appears % 2

        return [total_pairs, spare]

pairs = [1,3,2,1,3,2,2]
s = Solution()
res = s.numberOfPairs(pairs)
print(res)
