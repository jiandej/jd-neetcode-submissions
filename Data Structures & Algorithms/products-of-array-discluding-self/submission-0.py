class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n

        for i in range(n):
            if (i != 0):
                prefix[i] = prefix[i-1]*nums[i]
                suffix[n-1-i] = suffix[n-i]*nums[n-1-i]
            else:
                prefix[i] = nums[i]
                suffix[n-1-i] = nums[n-1-i]
        
        result = []
        for i in range(n):
            left = prefix[i-1] if i !=0 else 1
            right = suffix[i+1] if i != n-1 else 1
            result.append(left*right)
        
        return result