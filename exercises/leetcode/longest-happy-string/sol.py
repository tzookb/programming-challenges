from typing import Counter, List

class Node(object):
    def __init__(self, count, val):
        self.count = count
        self.val = val

    def __repr__(self):
        return f'{self.val}: {self.count}'

    def __lt__(self, other):
        return self.count < other.count

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        final = []

        nodes = []
        if a:
            nodes.append(Node(a, "a"))
        if b:
            nodes.append(Node(b, "b"))
        if c:
            nodes.append(Node(c, "c"))

        pushback = []
        nodes.sort(reverse=True)
        while nodes:
            print(nodes)
            cur = nodes.pop(0)
            if len(final) >= 2 and final[-1] == final[-2] == cur.val:
                pushback.append(cur)
                continue
            final.append(cur.val)
            cur.count -= 1
            if cur.count > 0:
                nodes.append(cur)
            
            nodes += pushback
            pushback = []
            nodes.sort(reverse=True)

        return "".join(final)
a = 2
b = 7
c = 10 
s = Solution()
res = s.longestDiverseString(a, b, c)
print(res)