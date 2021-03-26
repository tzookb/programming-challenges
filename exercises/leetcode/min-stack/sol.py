class MinStack:

    def __init__(self):
        self.items = []

    def push(self, x: int) -> None:
        cur_min = x
        if self.items:
            cur_min = min(cur_min, self.getMin())
        self.items.append((x, cur_min))

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        return self.items[-1][0]

    def getMin(self) -> int:
        return self.items[-1][1]
