from bisect import bisect_right

class Solution:
    def find(self, items, item):
        maxed = 0
        left = 0
        right = len(items) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if items[mid][0] > item:
                right = mid - 1
            else:
                maxed = max(maxed, items[mid][1])
                left = mid + 1
            
        return maxed

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])

        maxtil = 0
        for i in range(len(items)):
            maxtil = max(maxtil, items[i][1])
            items[i][1] = maxtil


        matched = self.find(items, 0)
        
        res = []
        for query in queries:
            matched = self.find(items, query)
            res += [matched]
        
        if not res:
            return [0]

        return res

        