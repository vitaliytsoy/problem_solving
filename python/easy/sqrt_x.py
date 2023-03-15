"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""
import math 

class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        
        if x == 0: return 0
        
        
        while start <= end:
            middle = (start + end) // 2
            double = middle * middle
            
            if (double == x or start == end):
                return middle - (1 if double > x else 0)
            
            if (double > x):
                end = middle - 1
                continue
            
            if (double < x ):
                start = middle + 1 
                continue

        return end 
        
s = Solution()

# print('4 ', s.mySqrt(4))
# print('3 ', s.mySqrt(3))
# print('5 ', s.mySqrt(5))
print('8 ', s.mySqrt(8))
# print('9 ', s.mySqrt(9))
# print('16 ', s.mySqrt(16))
# print('12 ', s.mySqrt(12))
