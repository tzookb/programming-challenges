class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        def removeUnusedClosers(arr, open, closer):
            sb = []
            opens = 0
            for c in arr:
                if c == open:
                    opens += 1
                    sb.append(c)
                elif c == closer:
                    if opens > 0:
                        opens -= 1
                        sb.append(c)
                else:
                    sb.append(c)
            return sb

        final = list(s)
        final = removeUnusedClosers(final, "(", ")")
        final = removeUnusedClosers(final[::-1], ")", "(")
        return "".join(final[::-1])


sol = Solution()
res = sol.minRemoveToMakeValid("))(ab(")
print(res)





