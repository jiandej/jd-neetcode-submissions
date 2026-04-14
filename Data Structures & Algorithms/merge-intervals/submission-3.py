class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])

        result = []

        start, end = intervals[0]

        for i in range(1, len(intervals)):
            new_start, new_end = intervals[i]
            if (end < new_start):
                result.append([start, end])
                start = new_start
                end = new_end
            else:
                start = min(start, new_start)
                end = max(end, new_end)
        result.append([start, end])
        
        return result