from typing import List, Dict, Tuple

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        pos = self.getDigitPositions(cards)
        min_diff = float("inf")

        for card_key in pos:
            if len(pos[card_key]) < 2:
                continue
            for i in range(len(pos[card_key]) - 1):
                cur = pos[card_key][i]
                next = pos[card_key][i + 1]
                diff = next - cur + 1

                min_diff = min(min_diff, diff)
        
        if min_diff == float("inf"):
            return -1
        return min_diff

    def getDigitPositions(self, cards: List[int]) -> int:
        pos = {}
        for i, card in enumerate(cards):
            if card not in pos:
                pos[card] = []
            pos[card].append(i)
        return pos

s = Solution()
res = s.minimumCardPickup([3,4,2,3,4,7])
print(res)