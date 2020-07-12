from typing import List

class Solution:
    def intersectTwoArrys(self, arr1: List[int], arr2: List[int]) -> List[int]:
        newArr = []
        i1 = i2 = 0
        while i1 < len(arr1) and i2 < len(arr2):
            v1 = arr1[i1]
            v2 = arr2[i2]
            if v1 == v2:
                newArr.append(v1)
                i1 += 1
                i2 += 1
                continue
            if v1 > v2:
                i2 += 1
            else:
                i1 += 1
        return newArr

    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        arr12 = self.intersectTwoArrys(arr1, arr2)
        return self.intersectTwoArrys(arr12, arr3)


arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]
s = Solution()
res = s.arraysIntersection(arr1, arr2, arr3)
# res = s.intersectTwoArrys(arr2, arr3)
print(res)