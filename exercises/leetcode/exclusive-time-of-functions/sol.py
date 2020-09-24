from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        ans = [0] * n

        for log in logs:
            log = log.split(":")
            aid = int(log[0])
            action = log[1]
            time  = int(log[2])

            if action == "start":
                if stack:
                    prev = stack.pop()
                    ans[prev[0]] += time - prev[1]
                    stack.append((prev[0], time))
                stack.append((aid, time))
            else:
                time += 1
                prev = stack.pop()
                ans[prev[0]] += time - prev[1]
                if stack:
                    prev = stack.pop()
                    stack.append((prev[0], time))
        return ans

s = Solution()
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
res = s.exclusiveTime(2, logs)
print(res)
