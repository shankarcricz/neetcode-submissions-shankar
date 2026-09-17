class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if(i>0):
                if nums[i]==nums[i-1]:
                    continue
            j = i+1
            k = len(nums)-1
            while (j<k):
                
                
                tot = nums[i]+nums[j]+nums[k]
                if(tot>0):
                    k=k-1
                elif (tot<0):
                    j=j+1
                else:
                    final.append([nums[i], nums[j], nums[k]])
                    j=j+1
                    k=k-1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                
        return final

        