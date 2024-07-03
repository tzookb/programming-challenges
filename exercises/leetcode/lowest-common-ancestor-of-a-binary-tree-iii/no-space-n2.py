from typing import List, Counter, Optional
from heapq import heappush, heappop, heapify

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        r1 = p
        r2 = q
        while r1 != r2:
            r1 = r1.parent if r1.parent else p
            r2 = r2.parent if r2.parent else q
        
        return r1
