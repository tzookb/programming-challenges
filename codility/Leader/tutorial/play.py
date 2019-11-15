class LimitedStack:

    def __init__(self, size):
        self.size = size
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
        if len(self.stack) > self.size:
            self.stack.pop(0)
    
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None
    
    def len(self):
        return len(self.stack)

    def view_last(self):
        return self.view(self.len())

    def view(self, idx):
        real_idx = len(self.stack) - idx - 1
        if real_idx < len(self.stack):
            return self.stack[real_idx]
        return None


ar = [4,6,6,6,6,8,8]

def get_leader(arr):
    s = LimitedStack(2)
    for v in arr:
        if s.len() == 0:
            s.push(v)
            print(s.stack)
            continue
        if s.view_last() != v:
            s.pop()
            continue
        s.push(v)
        print(s.stack)

    return s

res = get_leader(ar)
print(res.stack)