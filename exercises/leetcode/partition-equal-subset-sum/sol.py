class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total / 2
        
        cur = set()
        cur.add(0)
        
        for num in nums:
            update_set = set()
            for val in cur:
                update_set.add(val + num)
            
            cur = cur.union(update_set)

            if target in cur:
                return True
        
        return False
