from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        isUp = False
        isDown = False
        lastVal = prices[0]
        startI = 0
        steps = []

        for i in range(len(prices)):
            cur = prices[i]
            if cur > lastVal:
                isUp = True
                lastVal = cur
            else:
                if isUp:
                    isUp = False
                    # steps.append([startI, i-1])
                    steps.append(prices[startI:i])
                    startI = i
                    lastVal = cur
                else:
                    startI = i
        if isUp:
            steps.append(prices[startI:len(prices)])
        print(steps)

nums = [3,3,5,0,0,3,1,4]
s = Solution()
res = s.maxProfit(nums)
print(res)
