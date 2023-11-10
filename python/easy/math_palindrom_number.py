"""
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x > 0):
            return False
        
        half = 0 
        
        while half < x:
            half = half * 10 + x % 10
            
            x = x // 10
            
        return x == half or x == half // 10

s = Solution()
print(s.isPalindrome(10)) # False
print(s.isPalindrome(121)) # True
print(s.isPalindrome(-121)) # False

