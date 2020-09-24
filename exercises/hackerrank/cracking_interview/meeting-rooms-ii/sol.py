class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        sortByStart = lambda x: x[0]
        intervals.sort(key=sortByStart)
        
        for inter in intervals:
            interStart = inter[0]
            interEnd = inter[1]

            if rooms:
                rooms.sort()
                if interStart >= rooms[0]:
                    rooms[0] = interEnd
                    continue
            
            rooms.append(interEnd)
    
        return len(rooms)
        