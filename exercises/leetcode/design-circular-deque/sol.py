
class Node:
    def __init__(self, val, before=None, after=None):
        self.val = val
        self.before = before
        self.after = after

class MyCircularDeque:

    def __init__(self, k: int):
        self.maxSize = k
        self.size = 0
        self.start = Node(-1)
        self.end = Node(-1)
        self.start.after = self.end
        self.end.before = self.start

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        node = Node(value)

        oldfirst = self.start.after

        node.after = oldfirst
        node.before = self.start

        self.start.after = node
        oldfirst.before = node

        self.size += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        node = Node(value)

        oldlast = self.end.before
        oldlast.after = node

        node.after = self.end
        node.before = oldlast

        self.end.before = node

        self.size += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        oldfirst = self.start.after
        newfirst = oldfirst.after

        self.start.after = newfirst
        newfirst.before = self.start
        self.size -= 1

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        oldlast = self.end.before
        newlast = oldlast.before

        self.end.before = newlast
        newlast.after = self.end
        self.size -= 1

        return True

    def getFront(self) -> int:
        return self.start.after.val

    def getRear(self) -> int:
        return self.end.before.val
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.maxSize


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()