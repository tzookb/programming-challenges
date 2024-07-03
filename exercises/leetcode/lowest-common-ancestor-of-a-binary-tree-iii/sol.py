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
        parent = self.find_parent(p)
        common = self.lowestCommonAncestorFromParent(parent, p, q)
        print(common)
        return common

    def find_parent(self, node: 'Node') -> 'Node':
        prev = None
        cur = node
        while cur:
            prev = cur
            cur = cur.parent
        
        return prev

    def lowestCommonAncestorFromParent(self, parent: Node, p: 'Node', q: 'Node') -> 'Node':
        self.solved = None
        def recu(node: Optional[Node]):
            if not node:
                return [False, False]
            
            left_side = recu(node.left)
            right_side = recu(node.right)

            result = [
                left_side[0] or right_side[0] or node.val == p.val,
                left_side[1] or right_side[1] or node.val == q.val,
            ]

            if result[0] and result[1] and self.solved is None:
                self.solved = node
            
            return result

        recu(parent)
        return self.solved


