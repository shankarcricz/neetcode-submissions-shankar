class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        arr = [0,0]
        for i in range(len(nums)):
            k = target - nums[i]
            if hashmap.get(k) != None:
                arr[0] = hashmap.get(k)
                arr[1] = i
                return arr
            hashmap[nums[i]] = i
        
        