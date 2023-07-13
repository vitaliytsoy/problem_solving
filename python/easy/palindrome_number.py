"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
"""

class Solution:
    def isPalindromeString(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    
    def isPalindromeReverseInt(self, x: int) -> bool:
        reverse_number = 0
        initial_number = x
    
        if (abs(x) != x):
            return False
        
        while x != 0:
            reverse_number = reverse_number * 10 + x % 10
            
            x = x // 10
            
        return initial_number == reverse_number
    
    def isPalindromeReverseInt(self, x: int) -> bool:
        if ((x % 10 == 0 and x > 0) or x < 0):
            return False
        
        half_number = 0

        while x > half_number:
            half_number = half_number * 10 + x % 10
            
            x = x // 10
            
        return x == half_number or x == half_number // 10
    
s = Solution()
print(s.isPalindrome(10))