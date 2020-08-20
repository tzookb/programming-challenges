from typing import List
import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def verticalOrder(self, root: TreeNode) -> List[List[int]]:
    def verticalOrder(self, root) -> List[List[int]]:
        if not root:
            return []
        nodes = [(root, 0)]
        sp = collections.defaultdict(list)
        
        while nodes:
            cur, pos = nodes.pop(0)
            if not cur:
                continue
            sp[pos].append(cur.val)
            nodes.append((cur.left, pos - 1))
            nodes.append((cur.right, pos + 1))
        
        
        dictKeys = sp.keys()
        offset = 0 - min(dictKeys)
        
        arrayed = [None] * len(dictKeys)
        for key in sp:
            spot = key + offset
            arrayed[spot] = sp[key]
        
        return arrayed
