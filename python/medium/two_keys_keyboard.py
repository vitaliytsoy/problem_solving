"""
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.
 

Example 1:

Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

Example 2:

Input: n = 1
Output: 0
"""

class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        
        for i in range(2, n + 1):
            while(n % i == 0):
                res += i
                n = n / i
    
        return res
    
    
s = Solution()
print(s.minSteps(6))
print(s.minSteps(7))