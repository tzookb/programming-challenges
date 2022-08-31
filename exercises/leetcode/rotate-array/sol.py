from typing import List, Counter
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k == 0:
            return
        size = len(nums)
        actual_k = size % k
        
        count = 0
        start = 0
        while count < size:
            cur, prev = start, nums[start]
            while True:
                next_idx = (cur + k) % size
                nums[next_idx], prev = prev, nums[next_idx]
                cur = next_idx
                count += 1
                if cur == start:
                    break
            
            start += 1
        

items = [1,2,3,4,5,6,7]
k = 3
s = Solution()
print(items)
s.rotate(items, k)
print(items)
