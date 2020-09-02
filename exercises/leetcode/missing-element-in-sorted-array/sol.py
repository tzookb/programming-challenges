from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        cur = nums[0]
        count = 0
        for num in nums:
            if num != cur:
                diff = num - cur
                print(num, cur, count)
                for _ in range(diff):
                    count += 1
                    if count == k:
                        return cur
                    cur += 1
            else:
                cur += 1

        return cur + k - count
            

s = Solution()
x = [4, 7, 9, 10]
k = 1
res = s.missingElement(x, k)
print(res)
# print(x[1:])