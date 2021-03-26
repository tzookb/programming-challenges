from typing import List

class Solution:
    def getBestRate(self, fr, to, converter) -> List[float]:
        visited = {}
        next_coins = [fr]
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        convert_map = {}
        for i in range(len(equations)):
            equat = equations[i]
            rate = values[i]
            if equat[0] not in convert_map:
                convert_map[equat[0]] = {}
            if equat[1] not in convert_map:
                convert_map[equat[1]] = {}
            
            convert_map[equat[0]][equat[1]] = 1 / rate
            convert_map[equat[1]][equat[0]] = rate

        print(convert_map)

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
# queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
queries = [["a","c"]]

s = Solution()

res = s.calcEquation(equations, values, queries)

print(res)
