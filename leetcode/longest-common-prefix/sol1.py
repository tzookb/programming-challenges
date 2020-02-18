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

    def getCommonPrefix(self, shorter: str, second: str) -> str:
      length = len(shorter)
      prefix = ''
      if length == 0:
        return prefix

      for idx, char in enumerate(shorter):
        if char != second[idx]:
          return prefix
        prefix = prefix + char

      return prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
          return ''
        if len(strs) == 1:
          return strs[0]
        
        shortest = strs[0]
        for str in strs:
          if len(str) < len(shortest):
            shortest = str

        prefix = shortest
        for str in strs:
          prefix = self.getCommonPrefix(prefix, str)
          if prefix == '':
            return ''
        return prefix

        



s = Solution()
r = s.longestCommonPrefix([
  'abc',
  'abc',
  'abcd',
])
print(r)