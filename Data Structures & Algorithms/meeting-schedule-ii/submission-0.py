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
        max_room = 1
        end_times = []
        heapq.heapify(end_times)

        for interval in intervals:
            if not end_times:
                heapq.heappush(end_times, interval.end)
            else:
                if (end_times[0] > interval.start):
                    heapq.heappush(end_times, interval.end)
                    max_room = max(max_room, len(end_times))
                else:
                    heapq.heappop(end_times)
                    heapq.heappush(end_times, interval.end)
        
        return max_room