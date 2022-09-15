from typing import Counter, List, Optional

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort()
        perimeter = sum(matchsticks)
        if perimeter % 4 > 0:
            return False
        side = perimeter / 4

        # results will contain the options to build the corresponding match
        # for each round.
        # it start with an empty array inside it, as there is one option to build zero matches.
        # first loop will have the options to build one match with all the matchsticks we have.
        # second loop will have options to build one match after we removed the matches for building the first match.
        # third loop the same
        # not looping for the forth time, as we know if we got to build 3rd match, the left will be able to build the forth
        results = [[]]
        for _ in range(3):
            cur_results = []
            for result in results:
                left_matches = self.getLeftItems(matchsticks, result)
                cur_match_builds = self.getNums(left_matches, side)
                cur_match_builds = [result + x for x in cur_match_builds]
                cur_results += cur_match_builds
            results = cur_results
        return bool(results)


    def getLeftItems(self, big: List[int], small: List[int]) -> List[int]:
        """returns big array items after we removed the items
        that exist in small array. duplicated items are not relevant,
        we will remove the exact count as we have.
        ie:
        big -> [1,2,2,3]
        small -> [1,2]
        result -> [2,3]
        """
        cntbig = Counter(big)
        cntsmall = Counter(small)
        diff = cntbig - cntsmall
        result = []
        for item in diff:
            result += [item] * diff[item]
        return result

    def getNums(self, matchsticks: List[int], target: int) -> List[List[int]]:
        """gets a list of nums and a target,
        returns all the unique subsets that sum to the target
        """
        results = []
        def backtrack(cur, idx, tgt):
            if tgt == 0:
                results.append(cur.copy())
            if idx >= len(matchsticks):
                return
            
            prev = None
            for i in range(idx, len(matchsticks)):
                next_val = matchsticks[i]
                if next_val == prev:
                    continue
                prev = next_val
                if next_val > tgt:
                    continue
                cur.append(next_val)
                backtrack(cur, i + 1, tgt - next_val)
                cur.pop()
        backtrack([], 0, target)
        
        return results



s = Solution()
# res = s.makesquare([1,1,2,2,2])
res = s.makesquare([2,2,2,2,2,6])
# res = s.makesquare([3,3,3,3,4])
# res = s.extractNsum([1,1,2,2,2], 2)
# res = s.getLeftItems([1,1,2,2,2], [1,2])
print(res)