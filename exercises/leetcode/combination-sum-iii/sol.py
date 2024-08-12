from typing import List, Dict, Counter
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        solutions = []

        def dfs(cur: int, nums: List[int], used: Counter, fromNum: int):
            if len(nums) > k:
                return
            if cur > n:
                return
            for digit in used:
                if used[digit] > 1:
                    return
            if cur == n and len(nums) == k:
                solutions.append(nums.copy())

            for val in range(fromNum, 10):
                used[val] += 1
                dfs(cur + val, nums + [val], used, val + 1)
                used[val] -= 1

        dfs(0, [], Counter(), 1)

        return solutions

s = Solution()
res = s.combinationSum3(3, 9)
print(res)