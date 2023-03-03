"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative_power = False
        result = 1
        
        if n == 0:
            return 1
        
        if n < 0:
            negative_power = True
            n = -n
            
        while n > 0:
            if n % 2 == 0:
                x = x * x
                n = n / 2
                continue
            
            result = result * x
            n = n - 1
        
        return 1 / result if negative_power else result
            
s = Solution()
print(s.myPow(2.0000, -2))