from typing import List, Counter

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = map(lambda x: x%60, time)
        mapped = Counter()
        count = 0
        for t in time:
            completer = 60 - t
            if t == 0:
                count += mapped[0]
            elif completer in mapped:
                count += mapped[completer]
            
            mapped[t] += 1

        return count

s = Solution()

# res = s.numPairsDivisibleBy60([30,20,150,100,40]) # 3
# res = s.numPairsDivisibleBy60([60,60,60]) # 3
res = s.numPairsDivisibleBy60([418,204,77,278,239,457,284,263,372,279,476,416,360,18]) # 3
print(res)