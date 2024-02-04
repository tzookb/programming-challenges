from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers_count = {}

        for winner, loser in matches:
            if winner not in losers_count:
                losers_count[winner] = 0
            if loser not in losers_count:
                losers_count[loser] = 0
            losers_count[loser] += 1
        
        only_wins = []
        single_loses = []
        
        for user in losers_count:
            if losers_count[user] == 0:
                only_wins.append(user)
            elif losers_count[user] == 1:
                single_loses.append(user)
        
        only_wins.sort()
        single_loses.sort()
        return [only_wins, single_loses]