class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        prefix, suffix = 0, 0

        max_product = nums[0]

        for i in range(n):
            if (prefix == 0):
                # new start
                prefix = nums[i]
            else:
                prefix *= nums[i]
            
            if (suffix == 0):
                # new start
                suffix = nums[n-1-i]
            else:
                suffix *= nums[n-1-i]
            
            max_product = max(max_product, prefix, suffix)
        
        return max_product
