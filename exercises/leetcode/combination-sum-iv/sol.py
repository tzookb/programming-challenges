class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        solutions = [0 for _ in range(target + 1)]
        solutions[0] = 1

        for i in range(1, target + 1):
            options = 0
            for num in nums:
                if i - num < 0:
                    continue
                options += solutions[i - num]
            
            solutions[i] = options
        
        print(solutions)
        return solutions[-1]

        

        