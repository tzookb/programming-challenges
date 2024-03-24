class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def has_cycle(head):
    if not head or not head.next:
        return 0
    slow = head
    fast = head.next

    while fast != None and fast.next != None:
        if slow == fast:
            return 1
        slow = slow.next
        fast = fast.next.next

    return 0