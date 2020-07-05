class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def printList(l):
    item = l
    vals = []
    while item:
        vals.append(item.value)
        item = item.next
    print(vals)

def removeKFromList(l, k):
    fakeHead = ListNode('notk')
    fakeHead.next = l

    item = fakeHead
    while item:
        if item.next and item.next.value == k:
            item.next = item.next.next
            continue
        item = item.next

    return fakeHead.next

a1 = ListNode(1)
a2 = ListNode(1)
# a3 = ListNode(2)
# a4 = ListNode(3)
# a5 = ListNode(4)
# a6 = ListNode(5)
a1.next = a2
# a2.next = a3
# a3.next = a4
# a4.next = a5
# a5.next = a6

res = removeKFromList(a1, 1)
printList(res)