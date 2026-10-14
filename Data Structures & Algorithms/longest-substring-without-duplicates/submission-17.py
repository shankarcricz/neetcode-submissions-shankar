class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        output = 0
        l=0
        m = {}
        for r in range(len(s)):
            if m.get(s[r]) is not None:
                history = m.get(s[r])
                if history >= l:
                    l = history+1 
            m[s[r]] = r
            length = r-l+1
            output = max(output,length)
        return output


