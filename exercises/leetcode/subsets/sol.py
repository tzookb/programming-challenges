from typing import List

def binit(k):
    max_val = pow(2, k)
    all_ones_after_first = max_val - 1
    return max_val | all_ones_after_first

def get_bin_list(val):
    bin_rep = [int(i) for i in list('{0:0b}'.format(val))] 
    bin_rep.pop(0)
    return bin_rep

class Solution:
    def subsets(self, nums: List[int]):
        size = len(nums)
        max_val = pow(2, size)
        bin_rep = binit(size)
        count = 0
        results = []

        while count < max_val:
            bin_list = get_bin_list(bin_rep)
            cur_sub = []
            for is_in, num in zip(bin_list, nums):
                if is_in:
                    cur_sub.append(num)
            results.append(cur_sub)
            bin_rep -= 1
            count += 1
        return results

s = Solution()
res = s.subsets([1,2,3])
print(res)
