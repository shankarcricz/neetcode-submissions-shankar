class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for i in nums:
            hm[i] = hm.get(i,0) + 1
        hm = dict(sorted(hm.items(), key=lambda item: item[1], reverse=True))
        return [l for l in hm.keys()][0:k]