from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        list_size = self.getListSize(head)
        if k > list_size:
            chunk_size = 1
            extras = 0
        else:
            chunk_size = list_size // k
            extras = list_size % k

        lists = []
        cur = head

        while cur:
            curChunk = chunk_size if extras <= 0 else chunk_size + 1
            extracted, cur = self.extractNitemsFromList(cur, curChunk)

            lists.append(extracted)

            extras -= 1
        
        for _ in range(k - len(lists)):
            lists.append(None)

        return lists

    def extractNitemsFromList(self, head: Optional[ListNode], n: int) -> list[ListNode]:
        if n == 0:
            return [None, head]
        
        extractListFake = ListNode()
        curExtractList = extractListFake
        cur = head
        count = n

        while cur and count > 0:
            curExtractList.next = cur
            curExtractList = curExtractList.next
            cur = cur.next
            count -= 1
        
        if curExtractList:
            curExtractList.next = None
        
        return [extractListFake.next, cur]
        

    def getListSize(self, head: Optional[ListNode]) -> int:
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
        return size
        