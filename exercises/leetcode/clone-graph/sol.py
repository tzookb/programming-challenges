from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        created = {}
        nodes = [(node, None)]
        while nodes:
            curNode, addTo = nodes.pop(0)
            if curNode.val not in created:
                copiedNode = Node(curNode.val)
                created[curNode.val] = copiedNode
                for neighbor in curNode.neighbors:
                    nodes.append(
                        (neighbor, curNode.val)
                    )
            if addTo:
                attachTo = created[addTo]
                whoToAdd = created[curNode.val]
                attachTo.neighbors.append(whoToAdd)

        return created[node.val]