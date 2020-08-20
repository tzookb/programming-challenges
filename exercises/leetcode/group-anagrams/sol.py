from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}
        for str in strs:
            copiedStrArr = list(str[::])
            copiedStrArr.sort()
            copiedStr = "".join(copiedStrArr)
            if copiedStr not in mapper:
                mapper[copiedStr] = []
            mapper[copiedStr].append(str)

        finalArr = []
        for key in mapper:
            finalArr.append(mapper[key])
        return finalArr

s = Solution()

res = s.groupAnagrams([
    "eat", "tea", "tan", "ate", "nat", "bat"
])
print(res)
# print(x[1:])