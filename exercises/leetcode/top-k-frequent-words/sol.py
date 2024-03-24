from typing import Counter
from heapq import heappush, heappop
from functools import cmp_to_key
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        cnts = Counter(words)
        all = []

        for word in cnts:
            count = cnts[word]
            all.append((count, word))

        def compare(item1, item2):
            if item1[0] == item2[0]:
                return 1 if item1[1] > item2[1] else -1

            return 1 if item1[0] < item2[0] else -1
        
        all.sort(key=cmp_to_key(compare))

        # return heap
        return [x[1] for x in all][0:k]


words = ["i","love","leetcode","i","love","coding"]
k = 2
# words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
# k = 4
s = Solution()
res = s.topKFrequent(words, k)
print(res)