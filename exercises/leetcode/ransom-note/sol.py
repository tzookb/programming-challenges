from typing import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)
        
        for c in r:
            needed_count = r[c]
            if c not in m:
                return False
            possible_count = m[c]
            if needed_count > possible_count:
                return False
        
        return True