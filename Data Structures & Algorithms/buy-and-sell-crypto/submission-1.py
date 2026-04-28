class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        if len(prices) < 2:
            return 0
       
        i = 0
        j = i + 1
        while j < len(prices):
          
            if prices[i] < prices[j]:
                max_profit = max(max_profit , prices[j] - prices[i])
            else:
                i = j
            j+=1
        return max_profit

        