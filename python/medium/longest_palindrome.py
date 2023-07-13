"""
Given a string s, return the longest palindromic substringin s.


Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"
 
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        right = 0
        palindrome = [0, 0]
        
        for i in range(len(s)):
            right = i
            left = i    

            while right < (len(s) - 1) and s[right + 1] == s[left]:
                right += 1
                
                if (right - left + 1 > palindrome[1] - palindrome[0] + 1):
                    palindrome[0] = left
                    palindrome[1] = right

            
            while  left > 0 and right < (len(s) - 1) and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
                
                if (right - left + 1 > palindrome[1] - palindrome[0] + 1):
                    palindrome[0] = left
                    palindrome[1] = right
        
        return s[palindrome[0]: palindrome[1] + 1]
        
        
s = Solution()
print("ANSWER", s.longestPalindrome("babad"))
print("ANSWER", s.longestPalindrome("cbbd"))
print("ANSWER", s.longestPalindrome("bb"))
print("ANSWER", s.longestPalindrome("aba"))