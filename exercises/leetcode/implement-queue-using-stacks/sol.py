class MyQueue:

    def __init__(self):
        self.instack = []
        self.out = []

    def push(self, x: int) -> None:
        self.instack.append(x)
        

    def pop(self) -> int:
        if self.out:
            return self.out.pop()
        self._transfer()
        return self.out.pop()
        

    def peek(self) -> int:
        if self.out:
            return self.out[-1]
        self._transfer()
        return self.out[-1]
        

    def empty(self) -> bool:
        return not self.instack and not self.out
    
    def _transfer(self):
        while self.instack:
            self.out.append(self.instack.pop())
            
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()