"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        posts = []
        for kid in root.children:
            kidposts = self.postorder(kid)
            posts += kidposts
        
        posts += [root.val]
        return posts
        