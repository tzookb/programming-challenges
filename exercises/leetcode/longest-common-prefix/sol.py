from typing import List

class Solution:

    def getCharByIdx(self, str, idx) -> str:
      try:
        return str[idx]
      except:
        return ''

    def isCharInIndexCommon(self, strs: List[str], idx) -> bool:
        common_char = self.getCharByIdx(strs[0], idx)
        for str in strs:
          char = self.getCharByIdx(str, idx)
          if common_char != char or char == '':
            return False
        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
          return ''
        idx = 0
        prefix = ''
        while True:
          is_cur_char_common = self.isCharInIndexCommon(strs, idx)
          if not is_cur_char_common:
            return prefix
          prefix = prefix + self.getCharByIdx(strs[0], idx)
          idx += 1



s = Solution()
r = s.longestCommonPrefix([
  ''
])
print(r)