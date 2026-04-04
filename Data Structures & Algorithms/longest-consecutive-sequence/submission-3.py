class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = set(nums)
        longest = 0
        
        for n in nums:
            if (n-1 not in cache):
                lens = 1
                while (n+1 in cache):
                    lens+=1
                    n+=1
                longest = max(longest, lens)
        
        return longest
        