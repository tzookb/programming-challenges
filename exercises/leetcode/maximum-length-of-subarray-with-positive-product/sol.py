from typing import List
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        sub_arrs = self.getCleanedArrsFromZeros(nums)

        max_size = 0
        for subarr in sub_arrs:
            cur_size = self.getMaxNonZeros(subarr)
            max_size = max(max_size, cur_size)

        return max_size

    def getMaxNonZeros(self, nums: List[int]) -> int:
        negatives_count = 0
        for num in nums:
            if num < 0:
                negatives_count += 1
        
        if negatives_count % 2 == 0:
            return len(nums)
        
        till_neg_from_left = 0
        till_neg_from_right = 0

        for num in nums:
            if num < 0:
                till_neg_from_left += 1
                break
            till_neg_from_left += 1

        nums.reverse()
        for num in nums:
            if num < 0:
                till_neg_from_right += 1
                break
            till_neg_from_right += 1
        
        size = len(nums)
        from_left_size = size - till_neg_from_right
        from_right_size = size - till_neg_from_left

        return max(from_left_size, from_right_size)


    def getCleanedArrsFromZeros(self, nums: List[int]) -> int:
        sub_arrs = []
        cur = []
        for item in nums:
            
            if item != 0:
                cur.append(item)
            elif cur:
                sub_arrs.append(cur)
                cur = []
        if cur:
            sub_arrs.append(cur)

        return sub_arrs


s = Solution()
# res = s.getMaxLen([[1,-2,-3,4]])
res = s.getMaxLen([1,2,0,3,4,5,-1,7,4,1,6,])
print(res)