class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        if len(prices) < 2:
            return 0
        for i in range(len(prices)-1):
            curr_max = max(prices[i+1:])
            curr_profit = curr_max - prices[i]
            max_profit = max(max_profit , curr_profit)
        return max_profit
        