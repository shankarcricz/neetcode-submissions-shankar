class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # heights = sorted(heights)
        p1 = 0
        p2 = len(heights)-1
        maxArea = 0
        while(p1<p2):
            width = abs(p1-p2)
            height = min(heights[p1],heights[p2])
            storage = width*height
            if maxArea < storage: maxArea = storage
            if heights[p1]>heights[p2]:
                p2=p2-1
            elif p2>p1:
                p1=p1+1
        return maxArea


        