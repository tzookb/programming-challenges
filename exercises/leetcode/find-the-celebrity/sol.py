from typing import List, Counter
# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    return True

class Solution:
    def findCelebrity(self, n: int) -> int:
        potentials = {}
        for i in range(n):
            potentials[i] = True
        
        for i in range(n):
            removals = set()
            for potential in potentials:
                i_is_potential = i == potential
                if i_is_potential:
                    continue

                i_knows_potential = knows(i, potential)
                if i_knows_potential:
                    removals.add(i)
                else:
                    removals.add(potential)
            
            for item in removals:
                # del potentials[item]
                potentials.pop(item, None)

        if not potentials:
            return -1

        potential_candidate = list(potentials.keys())[0]

        for i in range(n):
            if i == potential_candidate:
                continue

            if knows(potential_candidate, i):
                return -1

        return potential_candidate




s = Solution()
s.findCelebrity(5)