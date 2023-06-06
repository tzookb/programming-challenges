from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        head_helper = ListNode(0, head)
        size = self.getListSize(head_helper)

        positions = list(range(1, size, k))
        is_full = (size-1) % k == 0
        
        reverse_groups = []
        for pos in positions:
            left_start = self.getNodeAndPrevInPos(head_helper, pos + 1)
            reverse_groups.append(left_start)
        
        sub_groups = []
        for item in reverse_groups:
            left_connector, start = item
            left_connector.next = None
            sub_groups.append(start)

        reveresed = [self.reverseList(sg) for sg in sub_groups[:-1]]
        last = self.reverseList(sub_groups[-1]) if is_full else sub_groups[-1]
        reveresed.append(last)

        for i in range(len(reveresed) - 1):
            first = reveresed[i]
            sec = reveresed[i + 1]
            while first.next:
                first = first.next
            first.next = sec
        
        return reveresed[0]
        

    def reverseList(self, head: Optional[ListNode]) -> ListNode:
        prev = None
        cur = head
        
        while cur:
            next_cur = cur.next
            cur.next = prev
            prev = cur
            cur = next_cur

        return prev
        

    def getNodeAndPrevInPos(self, head: Optional[ListNode], pos: int) -> ListNode:
        cur = head
        prev = None
        count = 0
        
        while cur:
            count += 1
            if count == pos:
                return (prev, cur)
            prev = cur
            cur = cur.next
        return None

    def getListSize(self, head: Optional[ListNode]) -> int:
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

