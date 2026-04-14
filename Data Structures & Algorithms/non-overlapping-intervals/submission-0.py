class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if (not intervals):
            return 0
        intervals.sort(key=lambda interval: interval[0])

        num_erased = 0
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            # no overlapping
            if (start >= prev_end):
                prev_end = end
            else:
                num_erased += 1
                prev_end = min(prev_end, end)
        
        return num_erased