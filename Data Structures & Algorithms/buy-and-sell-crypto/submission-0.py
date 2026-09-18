class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cheapPick = 200
        for i in prices:
            if cheapPick > i:
                cheapPick = i
            if i>cheapPick:
                profit = max(i-cheapPick,profit)
                
        return profit
