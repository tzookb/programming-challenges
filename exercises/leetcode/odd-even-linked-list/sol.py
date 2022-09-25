class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        fakeEven = ListNode()
        fakeOd = ListNode()
        cur_even = fakeEven
        cur_od = fakeOd

        cur = head
        idx = 1
        while cur:
            if idx % 2 == 0:
                cur_even.next = cur
                cur_even = cur
            else:
                cur_od.next = cur
                cur_od = cur

            idx += 1
            cur = cur.next

        cur_od.next = fakeEven.next
        cur_even.next = None
    
        print(fakeEven, fakeOd)
        return fakeOd.next