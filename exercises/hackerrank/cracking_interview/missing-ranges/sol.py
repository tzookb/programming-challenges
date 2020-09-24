from typing import List

class Solution:
    def getPairs(self, nums: List[int], lower: int, upper: int) -> List[str]:
        i = 0
        results = []
        while i < len(nums) - 1:
            cur = nums[i]
            nextV = nums[i + 1]
            diff = nextV - cur
            print(cur, nextV)
            if diff == 1:
                i += 1
                continue
            results.append((
                cur + 1,
                nextV - 1
            ))
            i += 1
        
        print(results)
        if nums[-1] < upper:
            results.append((
                nums[-1] + 1,
                upper
            ))
        if nums[0] > lower:
            results.insert(0, (
                lower,
                nums[0] - 1
            ))
        return results

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if nums:
            results = self.getPairs(nums, lower, upper)
        else:
            results = [(lower, upper)]

        def prepConnector(pair):
            if pair[0] == pair[1]:
                return str(pair[0])
            return str(pair[0]) + "->" + str(pair[1])

        results = list(map(prepConnector, results))

        return results

        