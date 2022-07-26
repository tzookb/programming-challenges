from typing import Counter, List, Optional

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        both = list(zip(plantTime, growTime))
        sorted_both = sorted(both, key=lambda x: x[1], reverse=True)
        max_day = 0
        cur_day = 0
        for pt, gt in sorted_both:
            cur_day += pt
            max_day = max(max_day, cur_day + gt)

        return max_day

# plantTime = [1,4,3]
# growTime = [2,3,1]

# plantTime = [1,2,3,2]
# growTime = [2,1,2,1]

plantTime = [1]
growTime = [1]


s = Solution()
res = s.earliestFullBloom(plantTime, growTime)
print(res)
