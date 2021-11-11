from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_count = [0] * n
        trusts_count = [0] * n

        for t in trust:
            truster = t[0]
            trustee = t[1]
            
            trusted_count[trustee - 1] += 1
            trusts_count[truster - 1] += 1
        
        try:
            judge_idx = trusted_count.index(n-1)
        except:
            return - 1

        if judge_idx is None:
            return - 1
        
        if trusts_count[judge_idx] > 0:
            return - 1

        return judge_idx + 1
        


n = 3
trusts = [[1,2],[2,3]]
s = Solution()
res = s.findJudge(n, trusts)
print(res)