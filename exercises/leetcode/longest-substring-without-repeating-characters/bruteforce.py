class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 1:
            return 1
        max_sub = 0
        for outer_idx, val in enumerate(s):
            inner_idx = outer_idx
            cur_dict = {}
            if length - inner_idx < max_sub:
                break
            while inner_idx < length:
                cur_val = s[inner_idx]
                # print(inner_idx)
                if cur_val in cur_dict:
                    substring_len = inner_idx - outer_idx
                    if substring_len > max_sub:
                        max_sub = substring_len
                    cur_dict = {}
                    break
                else:
                    cur_dict[cur_val] = True
                inner_idx += 1
            if len(cur_dict) > max_sub:
                max_sub = len(cur_dict)
        return max_sub

            
s = Solution()
print(s.lengthOfLongestSubstring('pwwkew') == 3)
print(s.lengthOfLongestSubstring('abcabcbb') == 3)
print(s.lengthOfLongestSubstring('bbbbb') == 1)
print(s.lengthOfLongestSubstring('a') == 1)
print(s.lengthOfLongestSubstring('ab') == 2)
