from typing import Counter, List

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        bfs = [(root,0)]
        level = 0
        fix = []
        while bfs:
            cur, curlevel = bfs.pop(0)
            if not cur:
                continue
            if curlevel != level:
                level = curlevel
                for i in range(len(fix) - 1):
                    fix[i].next = fix[i + 1]
                fix = []
            
            fix.append(cur)
            bfs.append((cur.left, curlevel + 1))
            bfs.append((cur.right, curlevel + 1))
        for i in range(len(fix) - 1):
            fix[i].next = fix[i + 1]
        return root