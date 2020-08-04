class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        parts = list(filter(lambda x: x!="", parts))
        if not parts:
            return "/"
        
        cur = []
        for next in parts:
            if next == "..":
                if cur:
                    cur.pop()
            elif next == ".":
                pass
            else:
                cur.append(next)
        return "/" + "/".join(cur)

path = "/../a/b/c/./.."
s = Solution()
res = s.simplifyPath(path)
print(res)
