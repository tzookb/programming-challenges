import bisect


class MyCalendar:

    def __init__(self):
        self.dates = []
        

    def book(self, start: int, end: int) -> bool:
        if self.isColiding(start, end):
            return False

        event = [start, end]
        bisect.insort(self.dates, event, key=lambda x: x[0])
        
        return True

    def isColiding(self, start: int, end: int) -> bool:
        left = 0
        right = len(self.dates) - 1
        if not self.dates:
            return False

        while left <= right:
            mid = left + (right - left) // 2
            print(left, right, mid)
            cur = self.dates[mid]
            curs, cure = cur
            maxstart = max(curs, start)
            minend = min(cure, end)
            if maxstart < minend:
                return True
            
            if curs < start:
                left = mid + 1
            else:
                right = mid - 1

        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)