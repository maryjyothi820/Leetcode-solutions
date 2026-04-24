118.pascals triangle 1
class Solution:
    def generate(self, numRows):
        triangle = []
        
        for i in range(numRows):
            row = [1] * (i + 1)
            
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            
            triangle.append(row)
        
        return triangle
119.pascals triangle 2
class Solution:
    def getRow(self, rowIndex):
        row = [1]
        
        for i in range(1, rowIndex + 1):
            new_row = [1] * (i + 1)
            
            for j in range(1, i):
                new_row[j] = row[j - 1] + row[j]
            
            row = new_row
        
        return row
121.best time to buy and sell stock
class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit