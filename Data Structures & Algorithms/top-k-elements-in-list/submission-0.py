class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        buckets = [[] for _ in range(n)]

        cache = {}

        for num in nums:
            if (num not in cache):
                cache[num] = 0
            cache[num] += 1
        
        for key, val in cache.items():
            buckets[val-1].append(key)
        
        result = []

        for i in range(n-1, -1, -1):
            if (len(result) == k):
                break
            if (len(buckets[i]) != 0):
                result += buckets[i]
        
        return result

