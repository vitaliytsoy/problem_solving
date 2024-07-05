"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""
from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:        
        dp = [([0] * len(prices)) for _ in range(k+1) ]
        
        if k >= len(prices) / 2:
            profit = 0
            
            for i in range(len(prices) - 1):
                if prices[i] < prices[i + 1]:
                    profit += prices[i + 1] - prices[i]

            return profit

        for i in range(1, k + 1):
            buy_price = -prices[0]
            
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j-1], prices[j] + buy_price)
                buy_price = max(dp[i-1][j-1] - prices[j], buy_price)
                
                
        return dp[k][len(prices) - 1]
        
        
        

s = Solution()
# print(s.maxProfit(2, [2,4,1])) # 2
# print(s.maxProfit(2, [3,2,6,5,0,3])) # 7
print(s.maxProfit(2, [1,2,4])) # 3


# print(s.maxProfit([3,3,5,0,0,3,1,4])) # 6
# print(s.maxProfit([1,2,3,4,5])) # 4
# print(s.maxProfit([7,6,4,3,1])) # 0
# print(s.maxProfit([1,2,4,2,5,7,2,4,9,0])) # 13
