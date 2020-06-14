from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates = sorted(candidates)
        
        ans = []
        
        self.rec([],target,ans,candidates)
        return ans
        
    
    def rec(self,output,target,ans,arr):
        
        if target == 0:
            ans.append(list(output))
            return
        
        if target < 0:
            return
        
        if len(arr) == 0:
            return
        
        output.append(arr[0])
        self.rec(output,target-arr[0],ans,arr[:])
        output.pop()
        self.rec(output,target,ans,arr[1:])

s = Solution()
res = s.combinationSum([2,3,5], 8)
# res = s.combineIntAndArrays(1, [[1,2], [3,4], [5,6]])
print(res)