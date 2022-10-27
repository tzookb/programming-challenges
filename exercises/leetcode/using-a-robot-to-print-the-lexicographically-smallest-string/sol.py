
class Solution:
    def robotWithString(self, s: str) -> str:
        final = []
        slist = list(s)
        tlist = []
        abc = [{} for _ in range(26)]
        for idx, c in enumerate(slist):
            abc[ord(c) - ord("a")][idx] = True
        
        cur_pos = 0
        for idx, matches in enumerate(abc):
            c = chr(idx + ord("a"))

            while tlist and ord(tlist[-1]) <= ord(c):
                final.append(tlist.pop())

            for match in matches:
                if match < cur_pos:
                    continue
                while cur_pos <= match:
                    tlist.append(s[cur_pos])
                    cur_pos += 1
                final.append(tlist.pop())
            
        final += tlist[::-1]
        return "".join(final)

s = Solution()
res = s.robotWithString("bdda")
res = s.robotWithString("bac")
res = s.robotWithString("zza")
res = s.robotWithString("vzhofnpo")
print(res)