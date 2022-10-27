import itertools
from os import times
from time import time
from typing import Counter, Dict, List, Optional


# https://leetcode.com/problems/analyze-user-website-visit-pattern/submissions/

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        grouped = {}
        for user, web in zip(username, website):
            if user not in grouped:
                grouped[user] = []
            grouped[user].append(web)
        
        patterns = Counter()
        for user in grouped:
            webs = grouped[user]
            user_patterns = {}
            for i in range(2, len(webs)):
                pattern = (webs[i-2], webs[i-1], webs[i])
                if pattern in user_patterns:
                    continue
                user_patterns[pattern] = True

                patterns[pattern] += 1

        max_pat = -1
        for pattern in patterns:
            max_pat = max(max_pat, patterns[pattern])
        
        suitable = []
        for pattern in patterns:
            if patterns[pattern] == max_pat:
                suitable.append(pattern)
        
        if len(suitable) <= 1:
            return suitable[0]


        max_patterns = ["".join(pt[0]) for pt in suitable]
        max_patterns.sort()
        return max_patterns[0]

# username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
# timestamp = [1,2,3,4,5,6,7,8,9,10]
# website = ["home","about","career","home","cart","maps","home","home","about","career"]

# username = ["ua","ua","ua","ub","ub","ub"]
# timestamp = [1,2,3,4,5,6]
# website = ["a","b","c","a","b","a"]
username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]

s = Solution()
res = s.mostVisitedPattern(username, timestamp, website)
print(res)