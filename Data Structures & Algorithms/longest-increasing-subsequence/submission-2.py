import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        sub = []
        for num in nums:
            if (not sub or sub[-1] < num):
                sub.append(num)
            idx = bisect.bisect_left(sub, num)
            sub[idx] = num
        
        return len(sub)
