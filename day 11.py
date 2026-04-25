122.best time to buy and sellstock 2
class Solution:
    def maxProfit(self, prices):
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        
        return profit
123.best time to buy and sellstock 
class Solution:
    def maxProfit(self, prices):
        buy1 = float('inf')
        buy2 = float('inf')
        profit1 = 0
        profit2 = 0
        
        for price in prices:
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)
            
            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)
        
        return profit2