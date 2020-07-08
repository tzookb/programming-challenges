from typing import List

class Solution:
    def floodFillIfColor(self, image: List[List[int]], sr: int, sc: int, oldColor: int, newColor: int):
        if not (sr >= 0 and sr < len(image) and sc >= 0 and sc < len(image[0])):
            return

        if image[sr][sc] == newColor:
            return

        if image[sr][sc] != oldColor:
            return

        image[sr][sc] = newColor
        self.floodFillIfColor(image, sr-1, sc, oldColor, newColor) #top
        self.floodFillIfColor(image, sr+1, sc, oldColor, newColor) #bottom
        self.floodFillIfColor(image, sr, sc-1, oldColor, newColor) #left
        self.floodFillIfColor(image, sr, sc+1, oldColor, newColor) #right

        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.floodFillIfColor(image, sr, sc, image[sr][sc], newColor)
        return image
        
        

image = [
    [0,0,0],
    [0,1,1]
]
s = Solution()
res = s.floodFill(image, 1, 1, 1)
print(res)