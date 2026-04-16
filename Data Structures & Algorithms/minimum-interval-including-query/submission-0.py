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
                for left in sorted_buckets[length]:
                    if (left <= query <= left + length-1):
                        result.append(length)
                        find_query = True
                        break
                if (find_query):
                    break
            if (not find_query):
                result.append(-1)
        
        return result
