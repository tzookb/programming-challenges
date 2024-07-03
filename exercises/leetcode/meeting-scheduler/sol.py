from typing import List

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        p1 = p2 = 0
        while p1 < len(slots1) and p2 < len(slots2):
            merged_start = max(slots1[p1][0], slots2[p2][0])
            merged_end = min(slots1[p1][1], slots2[p2][1])
            if slots1[p1][1] > slots2[p2][1]:
                p2 += 1
            else:
                p1 += 1
            if merged_start >= merged_end:
                continue
            if merged_end - merged_start >= duration:
                return [merged_start, merged_start + duration]

        return []

# slots1 = [[60,120], [10,50],[140,210]]
# slots2 = [[0,15],[60,70]]
# duration = 8
# 60, 68

slots1 = [[10,60]]
slots2 = [[12,17],[21,50]]
duration = 8
# 21,29


s = Solution()
res = s.minAvailableDuration(slots1, slots2, duration)
print(res)