from typing import List

class Vector2D:

    def __init__(self, v: List[List[int]]):
        def getIt():
            for row in v:
                for item in row:
                    yield item
        self.it = getIt()
        self.cur = None

    def next(self) -> int:
        if self.cur != None:
            temp = self.cur
            self.cur = None
            return temp
        return self._getNext()
        
    def hasNext(self) -> bool:
        if self.cur != None:
            return True
        self.cur = self._getNext()
        return self.cur != None

    def _getNext(self) -> int:
        try:
            return next(self.it);
        except StopIteration:
            return None