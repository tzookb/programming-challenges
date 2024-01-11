from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        seen = {}
        def dp(cur):
            hashed = "__".join(map(str, cur))
            
            if hashed in seen:
                return seen[hashed]
            if len(cur) <= 2:
                res = 0
                if len(cur) == 2:
                    res = cur[0] * cur[1] + max(cur)
                elif len(cur) == 1:
                    res = cur[0]
                seen[hashed] = res
                return res

            adapted = [1] + cur + [1]

            max_burst = float("-inf")
            for i in range(1, len(adapted) - 1):
                bursted_val = adapted[i - 1] * adapted[i] * adapted[i + 1]
                extract_arr = adapted[1:i] + adapted[i + 1: -1]
                next_bursts_val = dp(extract_arr)
                max_burst = max(max_burst, bursted_val + next_bursts_val)

            seen[hashed] = max_burst
            return max_burst
        res = dp(nums)
        return res

s = Solution()
# res = s.maxCoins([3,1,5,8])
res = s.maxCoins([1,5])
print(res)

