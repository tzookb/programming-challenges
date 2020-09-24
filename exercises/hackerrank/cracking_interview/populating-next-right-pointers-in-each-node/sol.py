"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        nodes = [(root, 1)]
        curDepth = 1
                
        while nodes:
            node, depth = nodes.pop(0)
            if node is None:
                continue
            if nodes:
                possibleNextNode = nodes[0]
                if possibleNextNode[1] != depth:
                    nextNode = None
                else:
                    nextNode = possibleNextNode[0]
            else:
                nextNode = None
            node.next = nextNode

            nodes.append((node.left, depth + 1))
            nodes.append((node.right, depth + 1))
        return root