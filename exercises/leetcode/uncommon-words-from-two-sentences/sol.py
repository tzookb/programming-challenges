from typing import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c1 = Counter(s1.split(" "))
        c2 = Counter(s2.split(" "))
        c = c1 + c2

        uncommon = []
        for w in c:
            if c[w] > 1:
                continue
            uncommon.append(w)
        
        return uncommon