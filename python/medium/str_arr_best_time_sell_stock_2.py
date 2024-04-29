"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = 0
        sell_price = 0
        pointer = 0
        n = len(prices) - 1
        
        while pointer < n:
            while pointer < n and prices[pointer + 1] <= prices[pointer]:
                pointer += 1
                
            buy_price = prices[pointer]
            
            while pointer < n and prices[pointer + 1] > prices[pointer]:
                pointer += 1
                
            sell_price = prices[pointer]
            
            profit += sell_price - buy_price
            
        return profit
            
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        pointer = 1
        n = len(prices)
        
        while pointer < n:
            profit += max(prices[pointer] - prices[pointer - 1], 0)
            pointer += 1
            
        return profit

s = Solution()
print(s.maxProfit([7,6,4,3,1])) # 0
print(s.maxProfit([1,2,3,4,5])) # 4