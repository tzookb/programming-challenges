"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            new_node = Node(val=insertVal)
            new_node.next = new_node
            return new_node
        
        cur = head.next
        prev = head

        to_insert = Node(val=insertVal)
        inserted = False

        while True:
            if cur == head:
                break
            if (
                prev.val <= insertVal and
                cur.val >= insertVal
            ):
                print(prev.val, cur.val, "a")
                prev.next = to_insert
                to_insert.next = cur
                inserted = True
                break

            if cur.val < prev.val:
                if (
                    prev.val <= insertVal or
                    cur.val >= insertVal
                ):
                    print(prev.val, cur.val, "b")
                    prev.next = to_insert
                    to_insert.next = cur
                    inserted = True
                    break

            prev = cur
            cur = cur.next
            
            
        if not inserted:
            prev.next = to_insert
            to_insert.next = cur

        return head