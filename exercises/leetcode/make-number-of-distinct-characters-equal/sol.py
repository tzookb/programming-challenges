from typing import List, Counter
import string

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)

        for k1 in string.ascii_lowercase:
            if k1 not in cnt1:
                continue
            for k2 in string.ascii_lowercase:
                if k2 not in cnt2:
                    continue

                cnt1[k1] -= 1
                cnt1[k2] += 1
                cnt2[k2] -= 1
                cnt2[k1] += 1
                if cnt1[k1] == 0:
                    del cnt1[k1]
                if cnt2[k2] == 0:
                    del cnt2[k2]

                if len(cnt1) == len(cnt2):
                    return True

                cnt1[k1] += 1
                cnt1[k2] -= 1
                cnt2[k2] += 1
                cnt2[k1] -= 1
                if cnt1[k2] == 0:
                    del cnt1[k2]
                if cnt2[k1] == 0:
                    del cnt2[k1]

        return False


s = Solution()
# res = s.isItPossible("abcc", "aab")
res = s.isItPossible("ac", "b")
# res = s.isItPossible("ab", "cd")
print(res)
