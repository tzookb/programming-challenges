class Solution:
    def __init__(self):
        self.mapper = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
    def romanToInt(self, s: str) -> int:
        number = 0
        tmp = self.mapper[s[0]]
        for x in range(len(s)):
            cur_val = self.mapper[s[x]]
            if tmp < cur_val:
                number = number + cur_val - 2 * tmp
                tmp = cur_val
            else:
                number = number + cur_val
                tmp = cur_val
        return number




s = Solution()
r = s.romanToInt('MCM')
# r = s.romanToInt('MCMXCIV')
print(r)