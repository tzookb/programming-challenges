from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        seen = {}
        todos = [("0000", 0)]

        while todos:
            [state, dist] = todos.pop(0)
            if state in seen:
                continue
            seen[state] = True
            if state in deadends:
                continue

            if state == target:
                return dist

            neighbours = self.getNextState(state)
            for neighbour in neighbours:
                todos.append((neighbour, dist + 1))
        return -1

    def getNextState(self, state):
        digits = list(state)
        next_states = set()
        for i in range(len(digits)):
            cur = int(digits[i])
            next_dig = cur + 1 if cur < 9 else 0
            prev_dig = cur - 1 if cur > 0 else 9
            next_num = digits[::]
            prev_num = digits[::]

            next_num[i] = str(next_dig)
            prev_num[i] = str(prev_dig)
            next_states.add("".join(next_num))
            next_states.add("".join(prev_num))
        return next_states

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
s = Solution()
res = s.openLock(deadends, target)
# res = s.getNextState("0000")
print(res)
