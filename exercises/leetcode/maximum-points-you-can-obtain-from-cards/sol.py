from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = len(cardPoints) - k - 1
        min_sum = sum(cardPoints[left:right + 1])
        cur_sum = min_sum
        first_time = True
        while right < len(cardPoints):
            if not first_time:
                prev = cardPoints[left - 1]
                new_num = cardPoints[right]
                cur_sum = cur_sum - prev + new_num
                min_sum = min(min_sum, cur_sum)
            else:
                first_time = False
            right += 1
            left += 1

        full_sum = sum(cardPoints)
        return full_sum - min_sum

cardPoints = [100,40,17,9,73,75]
k = 3
s = Solution()
res = s.maxScore(cardPoints, k)
print(res)