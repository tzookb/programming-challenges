# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=623634548182866
# TODO
# https://leetcode.com/problems/reverse-linked-list-ii/solution/
# https://leetcode.com/problems/reverse-nodes-in-k-group/

def flip(head):
    cur = head
    prev = None
    while cur:
        curNext = cur.next
        cur.next = prev
        prev = cur
        cur = curNext
    return prev

def flipFromTo(start, end):
    head = start.next
    cur = head
    prev = cur
    while cur != end:
        prev = cur
        cur = cur.next

    prev.next = None
    end = cur

    rev = flip(head)
    start.next = rev

    cur = rev
    while True:
        if not cur.next:
            cur.next = end
            break
        cur = cur.next

def reverse(head):
    node = head
    start = None
    prev = None

    begin = node
    count = 0
    while node:
        val = node.data
        cur = node
        node = node.next
        prev = cur
        count += 1
        if val % 2 == 0:
            continue
        if start is None:
            start = prev
            continue

        flipFromTo(start, prev)
        start = None
    
    return head

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def printList(head):
    node = head
    vals = []
    while node:
        vals.append(node.data)
        node = node.next
    print(vals)


def createLinkedList(arr):
    head = None
    tempHead = head
    for v in arr:
        if head == None:
            head = Node(v)
            tempHead = head
        else:
            head.next = Node(v)
            head = head.next
    return tempHead


head_1 = createLinkedList([2, 18, 24, 3, 5, 7, 9, 6, 12])
printList(head_1)
# expected_1 = createLinkedList([1, 8, 2, 9, 16, 12])
output_1 = reverse(head_1)
# output_1 = flipFromTo(head_1, head_1.next.next.next)
printList(head_1)