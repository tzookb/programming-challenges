class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxDist = -1
        mapper = {}
        for idx,c in enumerate(s):
            if  c not in mapper:
                mapper[c] = []
            mapper[c].append(idx)
        
        for c in mapper:
            arr = mapper[c]
            if len(arr) == 1:
                continue
            first = arr[0]
            last = arr[-1]
            dist = last - first - 1
            if dist >= 0:
                maxDist = max(maxDist, dist)
        return maxDist
            
        