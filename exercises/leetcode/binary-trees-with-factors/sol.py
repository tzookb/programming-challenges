import math
from typing import List, Optional

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        arr.sort()
        dp = {}
        total = 0
        for i, item in enumerate(arr):
            count = 1
            
            for j in range(0, i):
                divider = arr[j]
                if item % divider > 0:
                    continue
                divider2 = item / divider
                if divider2 not in dp:
                    continue

                possible_sub_trees = dp[divider] * dp[divider2]
                # if divider != divider2:
                #     possible_sub_trees *= 2

                count += possible_sub_trees
                count = count % MOD


            dp[item] = count % MOD
            total += count
            total = total % MOD
        return total % MOD



s = Solution()
# res = s.numFactoredBinaryTrees([2,4,5,10])
# res = s.numFactoredBinaryTrees([2, 4])
# res = s.numFactoredBinaryTrees([18,3,6,2]) # 12
res = s.numFactoredBinaryTrees([3,6,2]) # 5
print(res)