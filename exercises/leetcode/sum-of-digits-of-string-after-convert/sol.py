class Solution:
    def getLucky(self, s: str, k: int) -> int:
        parts = []
        for c in s:
            pos = ord(c) - ord("a") + 1
            print(pos)
            parts.append(str(pos))

        joined = "".join(parts)
        cur = int(joined)

        while k:
            total = 0
            curNum = cur
            while curNum:
                total += curNum % 10
                curNum = curNum // 10
            
            cur = total
            k -= 1

        return cur