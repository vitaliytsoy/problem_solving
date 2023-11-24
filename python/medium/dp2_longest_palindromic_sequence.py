"""
Given a string s, return the longest 
palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"
"""
class Solution:
    def find_palindrom_sequence(self, s, left, right):        
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
            
        return [left + 1, right - 1]
    
    def longestPalindrome(self, s: str) -> str:
        pointer = 0
        longest_palindrom = [0, 0]
        
        while pointer < len(s):
            palindrom = self.find_palindrom_sequence(s, pointer, pointer)

            if longest_palindrom[1] - longest_palindrom[0] + 1 < palindrom[1] - palindrom[0] + 1:
                longest_palindrom[0] = palindrom[0]
                longest_palindrom[1] = palindrom[1]
                
            palindrom = self.find_palindrom_sequence(s, pointer, pointer + 1)
            
            if longest_palindrom[1] - longest_palindrom[0] + 1 < palindrom[1] - palindrom[0] + 1:
                longest_palindrom[0] = palindrom[0]
                longest_palindrom[1] = palindrom[1]
                
            pointer += 1
            
        return s[longest_palindrom[0]:longest_palindrom[1]+1]
    
    
s = Solution()
print(s.longestPalindrome("babad")) # bab
print(s.longestPalindrome("cbbd")) # bb