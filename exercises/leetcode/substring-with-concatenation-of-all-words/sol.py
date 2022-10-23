from typing import Counter, List, Optional

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        sol = []
        wordsdict = Counter()
        for word in words:
            wordsdict[word] += 1
        
        wordsize = len(words[0])
        wordscount = len(words)
        limit = wordscount * wordsize

        
        for left in range(len(s) - limit + 1):
            start = left
            matched_all = True
            cur_wordsdict = wordsdict.copy()
            for i in range(wordscount):
                cur_word_start = start + wordsize * i
                cur_word = s[cur_word_start : cur_word_start + wordsize]
                if cur_word not in cur_wordsdict or cur_wordsdict[cur_word] == 0:
                    matched_all = False
                    break
                cur_wordsdict[cur_word] -= 1
            if matched_all:
                sol.append(left)
        return sol

# word = "barfoothefoobarman"
# words = ["foo","bar"]
# word = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]
word = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
s = Solution()
res = s.findSubstring(word, words)
print(res)