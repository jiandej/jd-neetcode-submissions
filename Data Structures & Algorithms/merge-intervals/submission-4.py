class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            new_start, new_end = intervals[i]
            if (result[-1][1] < intervals[i][0]):
                result.append(intervals[i])
            else:
                result[-1][1] = max(result[-1][1], intervals[i][1])
        
        return result