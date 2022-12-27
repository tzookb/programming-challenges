class MyQueue:
    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        return self.data.pop(0)

    def top(self) -> int:
        return self.data[0]

    def empty(self) -> bool:
        return not bool(self.data)

    def size(self) -> int:
        return len(self.data)
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = MyQueue()
        self.topv = None
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.push(x)
        self.topv = x
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.q.empty():
            return None
        elif self.q.size() == 1:
            self.topv = None
            return self.q.pop()

        new_q = MyQueue()
        while self.q.size() > 2:
            new_q.push(self.q.pop())

        self.topv = self.q.pop()
        to_return = self.q.pop()
        
        new_q.push(self.topv)
        self.q = new_q

        return to_return

    def top(self) -> int:
        return self.topv

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q.empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()