class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertNodeAtPosition(llist, data, position):
    fake = SinglyLinkedList()
    fake.next = llist

    nnode = SinglyLinkedList()
    nnode.data = data
    
    cur = fake
    
    while position > 0:
        position -= 1
        cur = cur.next
    
    mynext = cur.next
    cur.next = nnode
    nnode.next = mynext
    
    return fake.next