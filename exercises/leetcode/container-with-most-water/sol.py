class Solution:        
    def maxArea(self, height: List[int]) -> int:
        curMax = 0
        start = 0
        end = len(height) - 1
        
        while start < end:
            startHeight = height[start]
            endHeight = height[end]
            contHeight = min(startHeight, endHeight)
            contWidth = end - start
            curMax = max(curMax, contHeight * contWidth)

            if startHeight < endHeight:
                start += 1
            else:
                end -= 1

        return curMax
            
        