class MyStack(object):
    def __init__(self):
        self.holder = []

    def getAll(self):
        return self.holder

    def size(self):
        return len(self.holder)

    def pop(self):
        return self.holder.pop(0)

    def put(self, value):
        self.holder.append(value)
        
class MyQueue(object):
    def __init__(self):
        self.pushes = MyStack()
        self.pops = MyStack()
    
    def peek(self):
        pops = self.pops.getAll()
        if (len(pops) > 0):
            return pops[0]
        pushes = self.pushes.getAll()
        if (len(pushes) > 0):
            return pushes[0]
        return None
        
    def pop(self):
        if self.pops.size() == 0:
            for  i in xrange(self.pushes.size()):
                self.pops.put(self.pushes.pop())

        return self.pops.pop()
        
    def put(self, value):
        self.pushes.put(value)