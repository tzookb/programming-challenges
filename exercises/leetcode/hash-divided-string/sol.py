class Solution:
    def stringHash(self, s: str, k: int) -> str:
        final = []
        groups = self.getGroups(s, k)
        for group in groups:
            fullVal = self.getWordValue(group)
            cleanedVal = fullVal % 26 + ord("a")
            final.append(chr(cleanedVal))

        return "".join(final)

    def getWordValue(self, s: str) -> int:
        total = 0
        for c in s:
            total += (ord(c) - ord("a"))
        return total

    def getGroups(self, s: str, k: int) -> list[str]:
        return [s[i*k:i*k + k] for i in range(len(s)//k)]
        