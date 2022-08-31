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

