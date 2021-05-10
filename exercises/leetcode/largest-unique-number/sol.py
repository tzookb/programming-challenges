class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        singles = {}
        for a in A:
            if a not in singles:
                singles[a] = 0
            singles[a] += 1
        
        cur_max = -1

        for key in singles:
            val = singles[key]
            if val > 1:
                continue
            cur_max = max(cur_max, key)

        return cur_max
        