class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        globalObj = {}
        for i in strs:
            sorted_string = "".join(sorted(i))
            if globalObj.get(sorted_string):
                arr = []
                globalObj[sorted_string].append(i)
            else:
                globalObj[sorted_string] = [i]
        return [l for l in globalObj.values()]