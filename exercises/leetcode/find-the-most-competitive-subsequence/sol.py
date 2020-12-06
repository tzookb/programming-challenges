from typing import List

class Solution:

    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        sol = []
        
        for i, x in enumerate(nums):
            if not sol:
                sol.append(x)
                continue
            left_items = len(nums) - i - 1

            while sol:
                found_items_size = len(sol)
                last_sol = sol[-1]
                if last_sol > x and left_items >= k - found_items_size:
                    sol.pop()
                else:
                    break

            sol.append(x)

        return sol[0:k]


s = Solution()
res = s.mostCompetitive([3,5,2,1,2,4,5,1,9], 3)
# res = s.mostCompetitive([3,5,2,6,1,8,4], 2)
print(res)
