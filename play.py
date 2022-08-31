import functools
import math
from typing import List

class LargerNumKey(str):
    def __lt__(x, y):
        print(x, y, x+y > y+x)
        return x+y > y+x
class Solution:
    def largestNumber(self, nums):
        largest_num = sorted(map(str, nums), key=LargerNumKey)
        largest_num = ''.join(largest_num)
        return '0' if largest_num[0] == '0' else largest_num


# print(owncomp(900, 91))

# nums = [900, 91, 5]
nums = [3,30,34,5,9]
s = Solution()
res = s.largestNumber(nums)
print(res)