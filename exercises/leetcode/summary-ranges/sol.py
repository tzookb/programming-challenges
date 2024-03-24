class Solution:
    def getStringRep(self, nums: List[int]) -> str:
        if nums[0] == nums[1]:
            return f"{nums[1]}"
        return f"{nums[0]}->{nums[1]}"
        
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = -1
        end = -1
        prev = None
        solutions = []

        for i, num in enumerate(nums):
            if num - 1 == prev:
                end = i
                prev = num
                continue
            
            solutions.append([start, end])
            start = end = i
            prev = num
        
        solutions.append([start, end])

        solutions = solutions[1:]

        solutions = [[nums[x[0]], nums[x[1]]] for x in solutions]
        solutions = [self.getStringRep(x) for x in solutions]
        
        return solutions

        