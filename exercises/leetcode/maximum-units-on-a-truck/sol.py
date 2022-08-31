from typing import List, Counter
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key= lambda x: x[1], reverse=True)
        left_size = truckSize
        total_units = 0
        while left_size:
            box_amount, box_units = boxTypes.pop(0)
            pos_box_space = min(left_size, box_amount)
            total_units += pos_box_space * box_units
            left_size -= pos_box_space
        return total_units

s = Solution()
res = s.maximumUnits([[1,3],[2,2],[3,1]], 4)
print(res)
