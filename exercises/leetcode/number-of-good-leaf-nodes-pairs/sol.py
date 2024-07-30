from typing import List, Counter, Optional
from heapq import heappush, heappop, heapify



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.counted = 0
        def recu(node, dist):
            counts = Counter()
            if not node:
                return counts
            if not node.left and not node.right:
                counts[dist] += 1
                return counts
            
            left_dists = recu(node.left, dist + 1)
            right_dists = recu(node.right, dist + 1)

            if not node.left or not node.right:
                return left_dists + right_dists
            
            for left in left_dists:
                actual_left = left - dist
                for right in right_dists:
                    actual_right = right - dist
                    if actual_left + actual_right <= distance:
                        self.counted += left_dists[left] * right_dists[right]
            
            return left_dists + right_dists
            
        recu(root, 0)

        return self.counted