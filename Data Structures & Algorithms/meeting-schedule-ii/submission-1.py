"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda interval: interval.start)
        rooms = []
        heapq.heappush(rooms, intervals[0].end)

        for i in range(1, len(intervals)):
            if (rooms[0] <= intervals[i].start):
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i].end)
        
        return len(rooms)