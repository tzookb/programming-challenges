from typing import List

class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        result = []

        for a,b in zip(self.stepped(encoded1), self.stepped(encoded2)):
            result.append(a * b)

        return result

    def stepped(self, encoded: List[List[int]]) -> int:
        for step in encoded:
            [val, mult] = step
            i = 0
            while i < mult:
                yield val
                i += 1

    def compress(self, arr: List[int]) -> List[List[int]]:
        till_now = None
        count = 0
        result = []
        for cur in arr:
            if cur != till_now:
                if count > 0:
                    result.append([till_now, count])
                count = 1
                till_now = cur
            else:
                count += 1

        if count > 0:
            result.append([till_now, count])

        return result


s = Solution()
enc1 = [[1,4]]
enc2 = [[2,2], [5,2]]
res = s.findRLEArray(enc1, enc2)
res = s.compress([1,1,1,1,1,1,2,2,2,3])
# res = s.findDuplicate([1,2,2,3,4])
print(res)
