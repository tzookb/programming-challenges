from typing import Dict
from sortedcontainers import SortedList

class LinkedItem:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev    
class MaxStack:

    sorted_list: SortedList
    linekdlist: LinkedItem
    linekdlistmapper: Dict

    def __init__(self):
        self.sorted_list = SortedList()
        self.linekdlist = LinkedItem("dontcare")
        self.linekdlistmapper = {}

    def push(self, x: int) -> None:
        new_item = LinkedItem(x)
        new_item.next = self.linekdlist.next
        new_item.prev = self.linekdlist

        if self.linekdlist.next:
            self.linekdlist.next.prev = new_item
        
        self.linekdlist.next = new_item

        self.sorted_list.add(x)
        
        if x not in self.linekdlistmapper:
            self.linekdlistmapper[x] = []

        self.linekdlistmapper[x].append(new_item)

    def pop(self) -> int:
        poped = self.linekdlist.next
        self.linekdlist.next = poped.next
        if poped.next:
            poped.next.prev = self.linekdlist

        self.sorted_list.remove(poped.val)

        self.linekdlistmapper[poped.val].pop(0)
        return poped.val

    def top(self) -> int:
        return self.linekdlist.next.val

    def peekMax(self) -> int:
        return self.sorted_list[-1]

    def print(self) -> int:
        items = []
        cur = self.linekdlist.next
        while cur:
            items.append(cur.val)
            cur = cur.next
        print(items)

    def popMax(self) -> int:
        max_val = self.sorted_list.pop()

        list_item = self.linekdlistmapper[max_val].pop()

        list_item.prev.next = list_item.next
        if list_item.next:
            list_item.next.prev = list_item.prev

        return max_val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

