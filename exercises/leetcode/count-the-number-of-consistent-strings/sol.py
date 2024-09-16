class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        charsAllowed = {}
        matches = 0
        for c in allowed:
            charsAllowed[c] = True
        
        for word in words:
            matched = True
            for c in word:
                if c not in charsAllowed:
                    matched = False
                    break
            
            if matched:
                matches += 1
        
        return matches


        