import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort interval based on start
        intervals.sort(key=lambda interval: interval[0])

        # sort query
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])

        min_heap = []
        n, i = len(intervals), 0
        result = [-1]*len(queries)

        for query, idx in sorted_queries:
            # put the intervals left <= query to min heap with format (length, right)
            while (i < n and intervals[i][0] <= query):
                heapq.heappush(min_heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i+=1
            
            while (min_heap and min_heap[0][1] < query):
                heapq.heappop(min_heap)
            
            if (min_heap):
                result[idx] = min_heap[0][0]
        
        return result
            



