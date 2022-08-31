from typing import List, Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        final = []

        def backtrack(cur, pos, target):
            if target == 0:
                final.append(cur.copy())
                return
            if target < 0:
                return
            
            prev = None
            for idx in range(pos, len(candidates)):
                val = candidates[idx]
                if val == prev:
                    continue
                prev = val
                cur.append(val)
                backtrack(cur, idx + 1, target - val)
                cur.pop()

        backtrack([], 0, target)
        return final



candidates = [10,1,2,7,6,1,5]
target = 8
s = Solution()
res = s.combinationSum2(candidates, target)
print(res)