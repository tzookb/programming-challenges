from typing import List
class Solution:
    def getMaxFromMat(self, mat: List[List[int]]) -> int:
        cur_max = 0
        for row in mat:
            cur_max = max(cur_max, row[-1])
        return cur_max

    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        max_item = self.getMaxFromMat(mat)
        nums = [0] * max_item
        numOfRows = len(mat)

        for row in mat:
            for item in row:
                nums[item - 1] += 1

        for idx, count in enumerate(nums):
            if numOfRows == count:
                return idx + 1

        return -1
        

s = Solution()
res = s.smallestCommonElement([[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]])
print(res)