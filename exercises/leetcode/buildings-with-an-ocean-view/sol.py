class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        highest_from_right = 0
        sees = []
        for i in range(len(heights) - 1, -1, -1):
            cur = heights[i]
            if cur > highest_from_right:
                highest_from_right = cur
                sees.append(i)
        return sees[::-1]