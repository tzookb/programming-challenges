from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort()
        def backtrack(cur, left):
            final.append(cur.copy())
            prev = None
            for i in range(len(left)):
                item = left[i]
                left_items = left[i + 1:]
                if item == prev:
                    continue
                prev = item
                cur.append(item)
                backtrack(cur, left_items)
                cur.pop()

        backtrack([], nums)
        return final

nums = [1,2,2]
s = Solution()
res = s.subsetsWithDup(nums)
print(res)