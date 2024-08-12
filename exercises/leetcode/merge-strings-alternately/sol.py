class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        total = []
        w1 = w2 = 0
        from_first = True
        while w1 < len(word1) and w2 < len(word2):
            if from_first:
                total.append(word1[w1])
                w1 += 1
                from_first = False
            else:
                total.append(word2[w2])
                w2 += 1
                from_first = True
        
        if w1 < len(word1):
            total += word1[w1:]
        if w2 < len(word2):
            total += word2[w2:]
        
        return "".join(total)