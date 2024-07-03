from typing import List


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copied_map = {}
        cur = head
        while cur:
            copied_item = Node(cur.val)
            copied_map[cur] = copied_item
            cur = cur.next
        
        dup_list = Node(0)
        dup_cur = dup_list
        cur = head

        while cur:
            copied_item = copied_map[cur]
            if cur.next:
                copied_item.next = copied_map[cur.next]
            if cur.random:
                copied_item.random = copied_map[cur.random]
            cur = cur.next

        return copied_map[head]