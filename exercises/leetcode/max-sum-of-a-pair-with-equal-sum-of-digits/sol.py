from typing import Counter, List, Optional
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        nums.sort()
        sums = {}

        for num in nums:
            sum_of_digits = self.getSumOfDigits(num)
            if sum_of_digits not in sums:
                sums[sum_of_digits] = []

            sums[sum_of_digits].append(num)
        
        print(sums)
        maxed_pair = -1
        for sumval in sums:
            nums = sums[sumval]
            if len(nums) < 2:
                continue
            cur_sum = nums[-1] + nums[-2]
            maxed_pair = max(maxed_pair, cur_sum)

        return maxed_pair

    def getSumOfDigits(self, num: int) -> int:
        digits_sum = 0
        cur_num = num
        while cur_num:
            leftover = cur_num % 10
            digits_sum += leftover
            cur_num = cur_num // 10
        
        return digits_sum


nums = [10,12,19,14]
s = Solution()
res = s.maximumSum(nums)
print(res)
