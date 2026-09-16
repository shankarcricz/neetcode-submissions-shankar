class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = []
        suffix_prod = []
        prod = 1
        for i in nums:
            prefix_prod.append(prod)
            prod = prod * i
        prod = 1
        for i in range(len(nums)-1,-1,-1):
            suffix_prod.append(prod)
            prod = prod*nums[i]
        final = []
        for i in range(len(nums)):
            p = prefix_prod[i] * suffix_prod[len(nums)-i-1]
            final.append(p)
        return final

