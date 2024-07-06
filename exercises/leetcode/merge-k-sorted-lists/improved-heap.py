from typing import List, Counter, Optional
from heapq import heappush, heappop, heapify

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Item:
    def __init__(self, lst):
        self.lst = lst
    
    def __lt__(self, other):
        return self.lst.val < other.lst.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        fake = ListNode(float("-inf"))
        cur = fake

        prk = []
        for lst in lists:
            if lst:
                heappush(prk, Item(lst))

        while prk:
            next_item = heappop(prk)
            next_item_list = next_item.lst

            cur.next = next_item_list
            cur = cur.next

            if next_item_list.next:
                heappush(prk, Item(next_item_list.next))
            
        return fake.next
