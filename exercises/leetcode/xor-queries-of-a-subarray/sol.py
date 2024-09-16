class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefSum = [0]

        for num in arr:
            prefSum.append(prefSum[-1] ^ num)
        prefSum.pop(0)
        
        print(prefSum)
        sol = []

        for query in queries:
            left, right = query
            rightV = prefSum[right]
            if left == 0:
                sol.append(rightV)
                continue
            
            
            sol.append(prefSum[left - 1] ^ rightV)
        
        return sol
            
