"""
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:

Input: n = 0
Output: 0
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)
    
    # ---
    cache = {}
    
    def factorial(self, n: int) -> int:
        if n == 0:
            return 1
        
        if n in self.cache:
            return self.cache[n]
            
        self.cache[n] = n * self.factorial(n - 1)
        
        return n * self.factorial(n - 1)   

    def trailingZeroes(self, n: int) -> int:
        factorial = self.factorial(n)
        zeros = 0
        
        while factorial % 10 == 0:
            zeros += 1 
            factorial //= 10 
        
        return zeros
    
s = Solution()
print(s.trailingZeroes(5)) # 1
print(s.trailingZeroes(3)) # 0
print(s.trailingZeroes(0)) # 0

