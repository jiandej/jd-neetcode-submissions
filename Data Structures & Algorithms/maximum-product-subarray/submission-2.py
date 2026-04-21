class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        max_product = max(nums)
        
        for i in range(n):
            product = nums[i]
            for j in range(i+1, n):
                product *= nums[j]
                max_product = max(max_product, product)
                if (product == 0):
                    break
        
        return max_product