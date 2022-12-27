from typing import List, Counter
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def mergeSort(lst: ListNode):
            if not lst or not lst.next:
                return lst
            left, right = self.splitList(lst)
            merged = self.mergeLists(mergeSort(left), mergeSort(right))
            return merged

        return mergeSort(head)

    def splitList(self, lst: ListNode) -> tuple[ListNode, ListNode]:
        if not lst:
            return (None, None)
        if not lst.next:
            return (lst, None)
        prev_slow = None
        slow = fast = lst

        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        
        prev_slow.next = None
        return (lst, slow)

    def mergeLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        fake = ListNode()
        cur = fake
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        
        return fake.next

def buildList(arr):
    fake_head = ListNode()
    prev = fake_head
    for item in arr:
        next_val = ListNode(item)
        prev.next = next_val
        prev = next_val
    return fake_head.next

def getArrFromList(head):
    arr = []
    cur = head
    while cur:
        arr.append(cur.val)
        cur = cur.next
    return arr

lst = buildList([1,2,3,4])
s = Solution()
res = s.sortList(lst)
print(getArrFromList(res))

# print(getArrFromList(s.mergeLists(buildList([1,2]), buildList([3,4]))))
