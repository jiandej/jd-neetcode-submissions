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
        # intervals.sort(key=lambda interval: interval.start)
        # rooms = []
        # heapq.heappush(rooms, intervals[0].end)

        # for i in range(1, len(intervals)):
        #     if (rooms[0] <= intervals[i].start):
        #         heapq.heappop(rooms)
        #     heapq.heappush(rooms, intervals[i].end)
        
        # return len(rooms)

        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        n = len(intervals)
        rooms, result = 0, 0
        s_idx, e_idx = 0, 0

        while (s_idx < n):
            if (starts[s_idx] < ends[e_idx]):
                # when min start is smaller than min end, we need a new room
                rooms += 1
                s_idx += 1
            else:
                rooms -= 1
                e_idx += 1
            result = max(result, rooms)
        
        return result