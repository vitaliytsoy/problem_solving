"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0
"""
from typing import List
import sys


class Solution:
    def coin_change_memo(self, coins: List[int], amount: int, cache: dict) -> int:
        coins.sort(reverse=True)

        min_coins = sys.maxsize
        
        if amount == 0:
            return 0
        
        if amount in cache:
            return cache[amount]
        
        for i in range(len(coins)):
            coin = coins[i]

            if coin > amount: 
                continue
            
            if coin == amount:
                return 1
            
            sub_result = self.coin_change_memo(coins, amount - coin, cache)
            
            if (sub_result == -1):
                cache[amount] = -1   
                continue
            
            min_coins = min(min_coins,  1 + sub_result)
            cache[amount] = min_coins
            
            
        return -1 if min_coins == sys.maxsize else min_coins
    


    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
    
        return self.coin_change_memo(coins, amount, {})
    
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     coins.sort()

    #     count = 0
    #     pointer = len(coins) - 1
    
    #     while pointer >= 0 and amount > 0:
    #         coin = coins[pointer]
            
    #         if coin > amount:
    #             pointer -= 1
    #             continue
            
    #         amount -= coin
    #         count += 1
            
    #     print('LEFT_AMOUNT',amount)
            
    #     return -1 if amount > 0 else count
        
s = Solution()
print(s.coinChange([1,2,5], 11)) # 3 
print(s.coinChange([2], 3)) # -1
print(s.coinChange([1], 0)) # 0
print(s.coinChange([186,419,83,408], 6249)) # 20
print(s.coinChange([484,395,346,103,329], 4259)) # 11


