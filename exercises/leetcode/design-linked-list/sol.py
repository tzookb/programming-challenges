class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        fake_head = Node("dontcare")
        self.start = fake_head

    def get(self, index: int) -> int:
        prev = self.start
        cur = self.start.next
        cur_idx = 0
        while cur_idx < index and cur:
            prev = cur
            cur = cur.next
            cur_idx += 1

        if cur:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        cur_head = self.start.next
        new_head = Node(val, cur_head)
        self.start.next = new_head

    def addAtTail(self, val: int) -> None:
        prev = self.start
        cur = self.start.next
        while cur:
            prev = cur
            cur = cur.next

        prev.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        prev = self.start
        cur = self.start.next
        cur_idx = 0
        while cur_idx < index and cur:
            prev = cur
            cur = cur.next
            cur_idx += 1
        
        old_next = prev.next
        new_node = Node(val, old_next)
        prev.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        prev = self.start
        cur = self.start.next
        cur_idx = 0
        while cur_idx < index and cur:
            prev = cur
            cur = cur.next
            cur_idx += 1
        
        old_next = prev.next
        after_next = old_next.next if old_next else None
        prev.next = after_next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)