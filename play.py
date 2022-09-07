
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.final = float("inf")

        def recu(ds, total):
            if not ds:
                self.final = min(self.final, total)
                return

            # one day
            recu(ds[1:], total + costs[0])

            # seven days
            today = ds[0]
            for idx in range(len(ds)):
                cur = ds[idx]
                if today + 7 < cur:
                    break
            recu(ds[idx:], total + costs[1])

            # thirty days
            today = ds[0]
            for idx in range(len(ds)):
                cur = ds[idx]
                if today + 30 < cur:
                    break
            recu(ds[idx:], total + costs[2])

        recu(days, 0)

        return self.final

days = [1,4,6,7,8,20]
costs = [2,7,15]
s = Solution()
res = s.mincostTickets(days, costs)
print(res)