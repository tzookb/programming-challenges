from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level_sum = float("-inf")
        level_with_max_sum = float("-inf")
        cur_level = 1
        cur_level_sum = 0
        bfs = [(root, 1)]
        while bfs:
            cur, level = bfs.pop(0)
            if not cur:
                continue
            if cur_level != level:
                if cur_level_sum > max_level_sum:
                    max_level_sum = cur_level_sum
                    level_with_max_sum = cur_level
                cur_level_sum = cur.val
                cur_level = level
            else:
                cur_level_sum += cur.val
            
            bfs.append((cur.left, level+1))
            bfs.append((cur.right, level+1))

        if cur_level_sum > max_level_sum:
            max_level_sum = cur_level_sum
            level_with_max_sum = cur_level
    
        return level_with_max_sum
