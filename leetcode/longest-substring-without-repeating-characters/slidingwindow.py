class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        start_idx = 0
        end_idx = 0
        max_sub = 0
        chars_dict = {}

        while end_idx < length and start_idx < length:
            if s[end_idx] not in chars_dict:
                chars_dict[s[end_idx]] = True
                max_sub = max(max_sub, end_idx - start_idx + 1)
                end_idx += 1
            else:
                del chars_dict[s[start_idx]]
                start_idx += 1
        return max_sub

            
s = Solution()
# print(s.lengthOfLongestSubstring('pwwkew') == 3)
# print(s.lengthOfLongestSubstring('abca') == 3)
# print(s.lengthOfLongestSubstring('abcabcbb') == 3)
# print(s.lengthOfLongestSubstring('bbbbb') == 1)
# print(s.lengthOfLongestSubstring('a') == 1)
print(s.lengthOfLongestSubstring('ab') == 2)
