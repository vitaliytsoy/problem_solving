"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = 0
        max_p = 1
        profit = 0
        
        while max_p < len(prices):
            if (prices[min_p] >= prices[max_p]):
                min_p = max_p
                max_p += 1
                continue
            
            new_profit = prices[max_p] - prices[min_p]
            
            if (new_profit > profit):
                profit = new_profit
                
            max_p += 1
        
        return profit
        
    
    
s = Solution()

print(s.maxProfit([7,1,5,3,6,4])) # 5
print(s.maxProfit([7,6,5,4,3,2,1])) # 0