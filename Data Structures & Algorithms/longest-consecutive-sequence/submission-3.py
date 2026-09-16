class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = sorted(set(nums))
        count = 1
        mxcnt = 1
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        for i in range(len(s)-1):
            if s[i+1] == s[i] + 1:
                count = count+1
                if mxcnt < count: mxcnt = count
            else:
                count = 1
        return mxcnt

            
