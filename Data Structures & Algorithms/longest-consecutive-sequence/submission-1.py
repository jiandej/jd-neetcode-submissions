class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = set()
        longest = 0
        stack = []
        for n in nums:
            cache.add(n)
        
        for n in nums:
            if (n-1 not in cache):
                stack.append(n)
        
        while (stack):
            n = stack.pop()
            lens = 1
            while (n+1 in cache):
                lens+=1
                n+=1
            longest = max(longest, lens)
        
        return longest
        