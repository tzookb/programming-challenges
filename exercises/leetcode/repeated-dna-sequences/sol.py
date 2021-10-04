from typing import List
from collections import Counter

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mol_size = 10
        str_size = len(s)
        dnas_counts = Counter()

        for i in range(str_size - mol_size + 1):
            cur_mol  = s[i:i+mol_size]
            dnas_counts[cur_mol] += 1

        result = []
        for dna in dnas_counts:
            count = dnas_counts[dna]
            if count > 1:
                result.append(dna)
        
        return result

sol = Solution()
res = sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
print(res)