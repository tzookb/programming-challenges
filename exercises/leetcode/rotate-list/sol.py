from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        list_size = self.getListSize(head)
        actual_k = k % list_size
        if actual_k == 0:
            return head

        last = self.getLastItem(head)
        last.next = head

        moves = list_size - actual_k
        cur = head
        while moves > 1:
            moves -= 1
            cur = cur.next

        to_ret = cur.next
        cur.next = None

        return to_ret

    def getFastPointer(self, head: ListNode, steps) -> ListNode:
        if not head:
            return head
        i = 0
        cur = head
        while i < steps:
            i += 1
            cur = cur.next
        return cur

    def getLastItem(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = head
        prev = None
        while cur:
            prev = cur
            cur = cur.next
        return prev

    def getKitem(self, head: ListNode, k: int) -> Optional[ListNode]:
        cnt = 1
        cur = head
        # prev = None
        while cnt < k and cur:
            # prev = cur
            cnt += 1
            cur = cur.next
        return cur

    def getListSize(self, head: Optional[ListNode]) -> int:
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        return count

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


s = Solution()
head = buildList([1,2,3])
turned = s.rotateRight(head, 2000000000)
print(getArrFromList(turned))

def test_sss():
    head = buildList([1,2,3,4,5])
    turned = s.rotateRight(head, 2)
    assert getArrFromList(turned) == [4,5,1,2,3]

    head = buildList([1,2,3])
    turned = s.rotateRight(head, 2000000000)
    assert getArrFromList(turned) == [4,5,1,2,3]


def test_get_k_item():
    assert s.getKitem(buildList([1,2,3,4,5]), 1).val == 1
    assert s.getKitem(buildList([1,2,3,4,5]), 2).val == 2
    assert s.getKitem(buildList([1,2,3,4,5]), 5).val == 5
    assert s.getKitem(buildList([1]), 1).val == 1
    assert s.getKitem(buildList([1,2]), 1).val == 1
    assert s.getKitem(buildList([1,2]), 2).val == 2

def test_get_list_size():
    assert s.getListSize(buildList([1,2,3,4,5])) == 5
    assert s.getListSize(buildList([1,2])) == 2
    assert s.getListSize(buildList([1])) == 1
    assert s.getListSize(buildList([])) == 0

def test_get_last():
    assert s.getLastItem(buildList([1,2,3])).val == 3
    assert s.getLastItem(buildList([1,2])).val == 2
    assert s.getLastItem(buildList([1])).val == 1
    assert s.getLastItem(buildList([])) == None

def test_get_fast_pointer():
    long_list = buildList([1,2,3,4,5])
    two_list = buildList([1,2])
    one_list = buildList([1])
    zero_list = buildList([])

    assert s.getFastPointer(zero_list, 10) == None
    assert s.getFastPointer(one_list, 1) == None
    assert s.getFastPointer(one_list, 0) == one_list
    assert s.getFastPointer(two_list, 0) == two_list
    assert s.getFastPointer(two_list, 1) == two_list.next
    assert s.getFastPointer(two_list, 2) == two_list.next.next
    assert s.getFastPointer(long_list, 2) == long_list.next.next
    