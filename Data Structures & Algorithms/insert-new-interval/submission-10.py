class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        idx = self.binary_search(intervals, newInterval)
        begin, end = newInterval

        if (idx > 0):
            # no overlapping
            if (intervals[idx-1][1] >= newInterval[0]):
                idx -= 1
            result += intervals[:idx]

        while (idx < len(intervals)):
            # no overlapping
            if (intervals[idx][0] > newInterval[1]):
                break
            begin = min(intervals[idx][0], begin)
            end =  max(intervals[idx][1], end)
            idx += 1
        
        result.append([begin, end])
        result += intervals[idx:]

        return result
    
    def binary_search(self, intervals: List[List[int]], newInterval: List[int]) -> int:
        lo = 0
        hi = len(intervals)-1

        while (lo <= hi):
            mid = lo + (hi-lo)//2

            if (intervals[mid][0] > newInterval[0]):
                hi = mid-1
            else:
                lo = mid+1
        
        return lo

