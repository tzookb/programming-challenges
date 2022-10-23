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

        max_pattern = patterns.most_common()
        print(max_pattern)
        # return [max_pattern[0], max_pattern[1], max_pattern[2]]

username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]

# username = ["ua","ua","ua","ub","ub","ub"]
# timestamp = [1,2,3,4,5,6]
# website = ["a","b","c","a","b","a"]
s = Solution()
res = s.mostVisitedPattern(username, timestamp, website)
print(res)