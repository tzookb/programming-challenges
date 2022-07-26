from typing import List, Optional

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0] * len(temperatures)
        stacked = []

        for idx, temp in enumerate(temperatures[::-1]):
            # print(idx, temp)
            if not stacked:
                stacked.append((temp, idx))
                continue
            
            while stacked:
                if stacked[-1][0] < temp:
                    stacked.pop()
                    continue
                print(idx)
                _, last_idx = stacked[-1]
                diff = idx - last_idx
                answers[idx] = diff
                break
            
            stacked.append((temp, idx))

        answers.reverse()
        return answers

temperatures = [73,74,75,71,69,72,76,73]
s = Solution()
res = s.dailyTemperatures(temperatures)
print(res)
