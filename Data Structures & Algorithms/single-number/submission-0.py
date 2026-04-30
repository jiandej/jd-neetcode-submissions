class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cache = set()

        for num in nums:
            if num not in cache:
                cache.add(num)
            else:
                cache.remove(num)
        
        return next(iter(cache))