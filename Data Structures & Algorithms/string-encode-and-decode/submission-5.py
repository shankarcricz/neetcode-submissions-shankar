class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s = s+i
            s = s+'`'
        s=s+str(len(strs))
        print(s)

        return s

    def decode(self, s: str) -> List[str]:
        p = s.split("`")
        p.pop()
        print(p)
        return p
        
