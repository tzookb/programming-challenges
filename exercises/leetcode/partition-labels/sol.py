from collections import Counter
from typing import List
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        locations = {c: i for i, c in enumerate(S) }
        groups = []
        j = anchor = 0
        for i, v in enumerate(S):
            j = max(j, locations[v])
            if j == i:
                groups.append(i - anchor + 1)
                anchor = i + 1

        return groups
        
s = Solution()
res = s.partitionLabels("abacde")
print(res)