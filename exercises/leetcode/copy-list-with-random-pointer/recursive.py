from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        created = {}
        def build(cur: Optional[Node]):
            if not cur:
                return None

            if cur in created:
                return created[cur]

            item = Node(cur.val)
            created[cur] = item
            item.next = build(cur.next)
            item.random = build(cur.random)
            
            return item
        
        return build(head)
            