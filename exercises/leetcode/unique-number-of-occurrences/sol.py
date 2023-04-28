from typing import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        counts = cnt.values()

        return len(counts) == len(set(counts))