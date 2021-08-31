class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.TIME_LIMIT = 300
        self.total_hits = 0
        self.hits_map = {
            0: 0
        }
        self.hits_times = [0]
        

    def print(self):
        print("total_hits", self.total_hits)
        print("hits_map", self.hits_map)
        print("hits_times", self.hits_times)
        print("-----")

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.isPassedTimeLimit(timestamp):
            self.popOldestTime()
        
        if timestamp not in self.hits_map:
            self.hits_map[timestamp] = 0
            self.hits_times.append(timestamp)

        self.hits_map[timestamp] += 1
        self.total_hits += 1


    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.isPassedTimeLimit(timestamp):
            self.popOldestTime()
        return self.total_hits
        
    def popOldestTime(self):
        oldest_hit = self.hits_times.pop(0)
        hit_count = self.hits_map[oldest_hit]
        del self.hits_map[oldest_hit]
        self.total_hits -= hit_count

    def isPassedTimeLimit(self, timestamp: int) -> int:
        if not self.hits_times:
            return False
        first_hit = self.hits_times[0]
        if first_hit + self.TIME_LIMIT <= timestamp:
            return True
        return False


# Your HitCounter object will be instantiated and called as such:
hitCounter = HitCounter();
hitCounter.hit(1);       # hit at timestamp 1.
# hitCounter.print()
hitCounter.hit(2);       # hit at timestamp 2.
# hitCounter.print()
hitCounter.hit(3);       # hit at timestamp 3.
# hitCounter.print()
# hitCounter.getHits(302);   # get hits at timestamp 4, return 3.
hitCounter.hit(300);     # hit at timestamp 300.
hitCounter.getHits(300); # get hits at timestamp 300, return 4.
hitCounter.print()
hitCounter.getHits(301); # get hits at timestamp 301, return 3.
