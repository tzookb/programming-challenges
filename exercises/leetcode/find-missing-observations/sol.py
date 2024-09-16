class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        evaluated = sum(rolls)
        totalThrows = len(rolls) + n
        mainTarget = totalThrows * mean
        target = mainTarget - evaluated

        print(target)
        if target < n:
            return []
        if target > n * 6:
            return []
        
        sol = [1] * n
        target -= n
        i = 0

        while target:
            add = min(5, target)
            target -= add
            sol[i] += add
            i+= 1

        return sol
        