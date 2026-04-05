class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache = set()

        for n in nums:
            if (n in cache):
                return True
            cache.add(n)
        
        return False