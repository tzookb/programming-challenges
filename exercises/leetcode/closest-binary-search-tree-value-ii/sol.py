from typing import List, Optional
from heapq import heappop, heappush
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        if not root:
            return []

        heap = [(float("-inf"), 0)] * k
        bfs = [root]

        while bfs:
            cur = bfs.pop(0)
            if not cur:
                continue
            diff = abs(target - cur.val)
            if -heap[0][0] > diff:
                heappop(heap)
                heappush(heap, (-diff, cur.val))
            bfs.append(cur.left)
            bfs.append(cur.right)
        
        from typing import List, Optional
from heapq import heappop, heappush
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        if not root:
            return []

        heap = [(float("-inf"), 0)] * k
        bfs = [root]

        while bfs:
            cur = bfs.pop(0)
            if not cur:
                continue
            diff = abs(target - cur.val)
            if -heap[0][0] > diff:
                heappop(heap)
                heappush(heap, (-diff, cur.val))
            bfs.append(cur.left)
            bfs.append(cur.right)
        
        res = map(lambda x: x[1], heap)
        return res