class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for idx, val in enumerate(arr):
            if idx == val:
                return idx
        
        return -1
            
        