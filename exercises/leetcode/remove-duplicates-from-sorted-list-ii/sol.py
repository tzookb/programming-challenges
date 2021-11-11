# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        fake = ListNode(None, head)
        prev = fake
        cur = head
        while cur:
            if not cur.next:
                break
            if cur.val != cur.next.val:
                prev = cur
                cur = cur.next
                continue

            dup_val = cur.val
            while cur:
                if cur.val != dup_val:
                    break
                cur = cur.next
            
            prev.next = cur
        
        return fake.next