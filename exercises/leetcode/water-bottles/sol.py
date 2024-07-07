class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drinked = numBottles
        empties = numBottles

        while empties >= numExchange:
            refilled = empties // numExchange
            leftover = empties % numExchange
            drinked += refilled

            empties = refilled + leftover
        
        return drinked