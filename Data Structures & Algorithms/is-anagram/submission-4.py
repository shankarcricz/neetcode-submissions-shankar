class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        if len(s) != len(t): return False
        hash1 = {}
        for i in range(len(s)):
            if hash1.get(s[i]):
                hash1[s[i]] = hash1[s[i]] + 1
            else:
                hash1[s[i]] = 1
            if hash1.get(t[i]):
                hash1[t[i]] = hash1[t[i]] - 1
            else:
                hash1[t[i]] = -1
        print(hash1) 
        for i in hash1.values():
            if i!=0:
                return False
        return True
            
            
        

        
    