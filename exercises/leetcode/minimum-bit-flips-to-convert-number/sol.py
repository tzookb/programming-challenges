class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        binstart = bin(start)[2:]
        bingoal = bin(goal)[2:]
        maxsize = max(len(binstart), len(bingoal))
        
        binstart = "0" * (maxsize - len(binstart)) + binstart
        bingoal = "0" * (maxsize - len(bingoal)) + bingoal
        
        changes = 0
        for s, g in zip(binstart, bingoal):
            if s != g:
                changes += 1

        return changes
        