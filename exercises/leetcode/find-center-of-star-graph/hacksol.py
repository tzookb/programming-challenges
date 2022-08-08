class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dict = {}
        for left, right in edges:
            print(left, right)
            if left in dict:
                return left
            dict[left] = True
            if right in dict:
                return right
            dict[right] = True