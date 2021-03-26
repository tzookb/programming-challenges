from typing import List
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapper = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapper:
            self.mapper[key] = []
        self.mapper[key].append((value, timestamp))
        self.mapper[key].sort(key=lambda x: x[1])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapper:
            return ""
        print(self.mapper)
        arr = self.mapper[key]

        start = 0
        end = len(arr)
        while start < end:
            mid = start + (end - start)//2
            print(mid)
            item_stamp = arr[mid][1]
            if timestamp > item_stamp:
                start = mid + 1
            elif timestamp < item_stamp:
                end = mid
            else:
                return arr[mid][0]

        if mid < timestamp:
            return arr[mid-1][0]
        


# 1 3 6 7 9
# Your TimeMap object will be instantiated and called as such:
["TimeMap","set","get","get","set","get","get"]
[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
obj = TimeMap()
obj.set('foo', 'bar', 1)
# print(obj.get("foo", 1))
print(obj.get("foo", 3))
# obj.set('foo', 'bar2',41)
# print(obj.get("foo", 4))
# print(obj.get("foo", 5))