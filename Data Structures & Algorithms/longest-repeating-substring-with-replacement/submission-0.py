class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        l=0
        r=0
        maxval = 0
        windowsize=0
        while r<len(s):
            if hashmap.get(s[r]) is not None:
                hashmap[s[r]] = hashmap.get(s[r])+1
            else:
                hashmap[s[r]] = 1
            maxkey = max(hashmap, key=hashmap.get, default=0)
            maxvalue = hashmap.get(maxkey,0)
            windowsize = r-l+1
            if (windowsize - maxvalue) > k:
                hashmap[s[l]] = hashmap.get(s[l]) - 1
                l = l+1
            else:
                maxval = max(maxval,windowsize)
            r+=1
            
        return maxval


