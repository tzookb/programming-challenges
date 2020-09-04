from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = [(-1, 0)]
        start = 0
        ans = []

        for log in logs:
            aid, action, time = log.split(":")
            time = int(time)

            prev = stack.pop(0)

            if action == "start":
                if prev[0] != aid:
                    workTime = prev[1] + time - start
                    stack.append((prev[0], workTime))
                    stack.append((aid, 0))
                else:
                    stack.append((aid, 0))

                start = time - 1
            else:
                ans.append(prev[1] + time - start)
                start = time + 1

        return ans[::-1]
s = Solution()
logs = ["0:start:0","0:start:2","0:end:5","0:end:6"]
res = s.exclusiveTime(2, logs)
print(res)
