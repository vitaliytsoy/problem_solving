"""
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:

Input: n = 0
Output: 0

Example 3:

Input: n = 1
Output: 0
"""

import math

class Solution:
    # def is_prime(self, num: int) -> bool:
    #     if num == 2:
    #         return True
        
    #     for i in range(2, num):
    #         if i ** 2 >= num:
    #             break
            
    #         if num % i == 0:
    #             return False
        
    #     return True
    
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        
        is_prime_list = [True] * n
    
        is_prime_list[0] = is_prime_list[1] = False
        
        for i in range(2, n):
            if is_prime_list[i]:
                j = i * 2
                
                while j < n:
                    is_prime_list[j] = False
                    j += i
                    
        return sum(is_prime_list)
    
s = Solution()

# print('INPUT 10:', s.countPrimes(10))
# print('INPUT 0:', s.countPrimes(0))
print('INPUT 0:', s.countPrimes(5000000))
# print('INPUT 0:', s.countPrimes(1000))