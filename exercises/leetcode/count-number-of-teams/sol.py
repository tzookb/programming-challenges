from collections import defaultdict

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0
        
        greater = [0] * len(rating)
        less = [0] * len(rating)
        res = 0
        
		# greater[i] is the number of elements after index i greater than ratings[i]
        for i in range(len(rating)-1):
            for j in range(i+1, len(rating)):
                if rating[j] > rating[i]:
                    greater[i] += 1
                else:
                    less[i] += 1
        
		# Accumulate counts
        for i in range(len(rating)-2):
            for j in range(i+1, len(rating)):
                if rating[i] < rating[j]:
                    res += greater[j]
                else:
                    res += less[j]
        
        return res