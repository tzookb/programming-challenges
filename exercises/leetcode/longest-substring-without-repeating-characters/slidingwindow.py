from typing import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        counts = Counter()
        max_size = 0
        
        while right < len(s):
            cur = s[right]
            counts[cur] += 1
            while counts[cur] > 1:
                leftval = s[left]
                counts[leftval] -= 1
                left += 1
            
            max_size = max(max_size, right - left + 1)
            right += 1
        
        return max_size
            


            
s = Solution()
# print(s.lengthOfLongestSubstring('pwwkew') == 3)
# print(s.lengthOfLongestSubstring('abca') == 3)
# print(s.lengthOfLongestSubstring('abcabcbb') == 3)
# print(s.lengthOfLongestSubstring('bbbbb') == 1)
# print(s.lengthOfLongestSubstring('a') == 1)
print(s.lengthOfLongestSubstring('ab') == 2)
