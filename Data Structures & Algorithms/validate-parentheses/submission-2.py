class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        for i in s:
            if len(stack)>0 and pairs.get(i):
                lastEl = stack.pop()
                if pairs.get(i) != lastEl:
                    return False
            else:
                stack.append(i)
        if len(stack)!=0 : return False
        return True

                
        