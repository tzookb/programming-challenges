from typing import List
from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_dict = {x: True for x in banned}
        paragraph = re.sub(r'[^A-Za-z0-9 ]+', ' ', paragraph)
        words = paragraph.lower().split()
        words_dict = Counter()
        counts = Counter()
        for word in words:
            words_dict[word] += 1

        max_val = -1
        max_word = None
        for word in words_dict:
            if word in banned_dict:
                continue
            count = words_dict[word]
            if count > max_val:
                max_val = count
                max_word = word
        return max_word

s = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
s.mostCommonWord(paragraph, banned)