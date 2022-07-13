from distutils.command.build_scripts import first_line_re
from typing import List
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = -1
        level = 1
        nodes = []
        bfs = [(root, 1, 1)]
        while bfs:
            cur, cur_level, idx = bfs.pop(0)
            if level != cur_level:
                level = cur_level
                # check nodes
                cur_width = self.calcWidth(nodes)
                max_width = max(max_width, cur_width)
                nodes = []

            if not cur:
                continue
            
            nodes.append((cur.val, idx))

            bfs.append((cur.left, cur_level + 1, idx * 2 ))
            bfs.append((cur.right, cur_level + 1, idx * 2 + 1))

        return max_width
    
    def calcWidth(self, nodes) -> int:
        first = nodes[0]
        last = nodes[-1]
        return last[1] - first[1] + 1