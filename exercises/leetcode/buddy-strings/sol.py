from typing import List
from collections import Counter

# Definition for singly-linked list.
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if len(s) == len(goal) == 1:
            return False
        
        mismatches = 0
        misses = []
        for a, b in zip(s, goal):
            if a != b:
                mismatches += 1
                misses.append([a,b])
            if mismatches > 2:
                return False

        if mismatches == 1:
            return False
        if len(set(s)) == len(s) and mismatches == 0:
            return False

        if mismatches == 2:
            return (
                misses[0][0] == misses[1][1] and
                misses[0][1] == misses[1][0]
            )
        return True
