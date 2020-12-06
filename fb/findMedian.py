from heapq import heapify, heappush, heappop

class Heap:
    def __init__(self, is_max=False):
        self.h = []
        self.is_max = is_max
        heapify(self.h)
    def prep(self, val):
        mult = -1 if self.is_max else 1
        return mult * val
    def push(self, val):
        heappush(self.h, self.prep(val))
    def pop(self,):
        return self.prep(heappop(self.h))
    def size(self):
        return len(self.h)
    def peek(self):
        if self.size():
            return self.prep(self.h[0])
        return None
        

def findMedian(arr):
    smalls = Heap(True)
    bigs = Heap(False)
    medians = []

    for x in arr:
        if smalls.size() == bigs.size():
            if smalls.size() == 0:
                smalls.push(x)
            else:
                if x > smalls.peek():
                    bigs.push(x)
                else:
                    smalls.push(x)
        elif smalls.size() > bigs.size():
            if x > smalls.peek():
                bigs.push(x)
            else:
                bigs.push(smalls.pop())
                smalls.push(x)
        else:
            if x < bigs.peek():
                smalls.push(x)
            else:
                smalls.push(bigs.pop())
                bigs.push(x)

        if smalls.size() == bigs.size():
            medians.append((smalls.peek() + bigs.peek()) // 2)
        elif smalls.size() > bigs.size():
            medians.append(smalls.peek())
        else:
            medians.append(bigs.peek())

    return medians



def test_code() -> None:
    # Test 1)
    arr = [2, 4, 7, 1, 5, 3]
    assert findMedian(arr)
    print("success")

if __name__ == "__main__":
    test_code()
