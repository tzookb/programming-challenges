from heapq import heappush, heappop
from typing import List

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for list in lists:
            item = list
            while item:
                heappush(heap, item.val)
                item = item.next

        fakeHead = ListNode('fake', None)
        cur = fakeHead
        while True:
            if not heap:
                break
            item = heappop(heap)
            tempNode = ListNode(item, None)
            cur.next = tempNode
            cur = cur.next
        return fakeHead.next