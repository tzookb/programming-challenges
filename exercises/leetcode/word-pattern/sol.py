class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patterns = self.getPatternsMap(pattern)
        words = s.split(" ")
        size = len(words)

        if len(pattern) != size:
            return False

        used_words = {}

        for key in patterns:
            locations = patterns[key]
            prev = None
            for location in locations:
                cur_word = words[location]
                if location >= size:
                    return False
                if prev is None:
                    prev = cur_word
                if prev != cur_word:
                    return False

            if cur_word in used_words:
                return False

            used_words[cur_word] = True

        return True

    def getPatternsMap(self, pattern: str) -> bool:
        mapped = {}
        for idx, c in enumerate(pattern):
            if c not in mapped:
                mapped[c] = []
            mapped[c].append(idx)
        return mapped

pattern = "aaa"
str = "aa aa aa aa"
sol = Solution()
res = sol.wordPattern(pattern, str)
print(res)