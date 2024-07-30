class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)

        counts = Counter()
        max_len = 0

        left = 0
        right = 0

        while right < len(s):
            key = s[right]
            counts[key] += 1

            while len(counts) > 2:
                rm_key = s[left] 
                counts[rm_key] -= 1
                if counts[rm_key] == 0:
                    del counts[rm_key]
                
                left += 1
            
            cur_len = right - left + 1

            max_len = max(max_len, cur_len)
            right += 1
        
        return max_len