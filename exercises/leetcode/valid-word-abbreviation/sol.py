from typing import List, Counter
from heapq import heappush, heappop, heapify

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if not self._is_valid_with_no_leading_zeros(abbr):
            return False
        abbr_items = self._break_abbr_to_items(abbr)
        
        wi = 0
        ai = 0

        print(abbr_items)
        while wi < len(word) and ai < len(abbr_items):
            if not isinstance(abbr_items[ai], int):
                if word[wi] != abbr_items[ai]:
                    return False
                wi += 1
                ai += 1
                continue

            wi += abbr_items[ai]
            ai += 1
        
        if wi != len(word):
            return False
        
        if ai < len(abbr_items):
            return False

        return True


    def _break_abbr_to_items(self, abbr: str) -> list[str|int]:
        items = ["removeme"]
        for ch in abbr:
            if not ch.isdigit():
                items.append(ch)
                continue
            if isinstance(items[-1], int):
                items[-1] = items[-1] * 10 + int(ch)
                continue
            items.append(int(ch))
        
        return items[1:]

    def _is_valid_with_no_leading_zeros(self, abbr: str) -> bool:
        number_started = False
        for ch in abbr:
            if not ch.isdigit():
                number_started = False
                continue
            if ch == "0" and number_started == False:
                return False
            
            number_started = True
        return True

s = Solution()
# res = s.validWordAbbreviation(word = "internationalization", abbr = "i12iz4n") # true
# res = s.validWordAbbreviation(word = "apple", abbr = "a2e") # false
res = s.validWordAbbreviation(word = "hi", abbr = "1") # false
print(res)