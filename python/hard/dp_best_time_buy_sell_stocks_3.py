"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
from typing import List
import heapq
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pointer = 0
        buy_price = 0
        profits = []
        n = len(prices) - 1 
        
        if len(prices) <= 1:
            return 0
        
        while pointer < n:
            while pointer < n and prices[pointer + 1] <= prices[pointer]:
                pointer += 1
                
            buy_price = prices[pointer]
            
            while pointer < n and prices[pointer + 1] > prices[pointer]:
                pointer += 1
                
            sell_price = prices[pointer]
            
            print(buy_price, sell_price, -(sell_price - buy_price))
            
            heapq.heappush(profits, -(sell_price - buy_price))
            
        if len(profits) == 1:
            return -heapq.heappop(profits)
            
        return -(heapq.heappop(profits)) + -(heapq.heappop(profits))

    # ---

    def maxProfit(self, prices: List[int]) -> int:
        s_1, s_2 = 0, 0
        b_1, b_2 = -sys.maxsize, -sys.maxsize
        
        for price in prices:
            s_2 = max(s_2, b_2 + price)
            b_2 = max(b_2, s_1 - price)
            s_1 = max(s_1, b_1 + price)
            b_1 = max(b_1, -price)
            
        return s_2
        
        

s = Solution()
# print(s.maxProfit([3,3,5,0,0,3,1,4])) # 6
# print(s.maxProfit([1,2,3,4,5])) # 4
# print(s.maxProfit([7,6,4,3,1])) # 0
print(s.maxProfit([1,2,4,2,5,7,2,4,9,0])) # 13
