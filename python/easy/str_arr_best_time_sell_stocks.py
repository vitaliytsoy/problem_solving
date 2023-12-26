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
        profit = 0 
        
        for i in range(len(prices)):
            price_buy = prices[i]

            for j in range(i + 1, len(prices)):
                price_sell = prices[j]
                profit = max(profit, price_sell - price_buy)
                
        return profit

    # ---
    
    def maxProfit(self, prices: List[int]) -> int:
        buy_pointer = 0
        sell_pointer = 1
        profit = 0
        
        while sell_pointer < len(prices):
            if prices[sell_pointer] < prices[buy_pointer]:
                buy_pointer = sell_pointer
                sell_pointer += 1
                continue
            
            if prices[sell_pointer] - prices[buy_pointer] > profit:
                profit = prices[sell_pointer] - prices[buy_pointer]
                
            sell_pointer += 1
                        
        return profit
    
s = Solution()
print(s.maxProfit([7,1,5,3,6,4])) # 5
print(s.maxProfit([7,6,4,3,1])) # 0
