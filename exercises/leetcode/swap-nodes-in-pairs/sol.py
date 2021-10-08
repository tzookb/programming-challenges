
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake_head = ListNode(0, head)
        cur = fake_head

        while cur and cur.next and cur.next.next:
            sec = cur.next
            third = sec.next
            forth = third.next
            cur.next = third
            third.next = sec
            sec.next = forth
            cur = cur.next.next
        
        return fake_head.next
