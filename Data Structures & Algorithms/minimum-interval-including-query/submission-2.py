from collections import defaultdict
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # key: length. value : list of beginning
        buckets = defaultdict(list)

        for left, right in intervals:
            length = right - left + 1
            buckets[length].append(left)
        
        for key in buckets.keys():
            buckets[key].sort()

        sorted_buckets = dict(sorted(buckets.items()))
        result = []

        for query in queries:
            find_query = False
            for length in sorted_buckets.keys():
                # we can optimize this with binary search if needed
                find_query = self.binarySearch(length, sorted_buckets[length], query)
                if (find_query):
                    result.append(length)
                    break
            if (not find_query):
                result.append(-1)
        
        return result
    
    def binarySearch(self, length: int, array: list[int], query: int) -> bool:
        lo = 0
        hi = len(array)

        while (lo <= hi and lo < len(array)):
            mid = lo + (hi-lo)//2

            if (array[mid] <= query <= array[mid] + length - 1):
                return True
            elif (query > array[mid] + length - 1):
                lo = mid + 1
            else:
                hi = mid - 1
        
        return False
