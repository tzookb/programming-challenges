class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[0]:
                j = i
                needIdx = 0
                if len(haystack[i:]) < len(needle):
                    return -1
                while j < len(haystack):
                    if haystack[j] != needle[needIdx]:
                        break

                    if needIdx == len(needle)-1:
                        return i
                    needIdx += 1
                    j += 1
            i += 1
        return -1

hay = "aaabbbbb"
need = "bccccccccc"
s = Solution()
res = s.strStr(hay, need)
print(res)