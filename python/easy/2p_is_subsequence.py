"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""
class Solution:    
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0
        p2 = 0
        
        if len(t) < len(s):
            return False
        
        while p2 < len(t) and p1 < len(s):
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
                continue
            
            p2 += 1
            
        return p1 == len(s)

s = Solution()
print(s.isSubsequence("abc", "ahbgdc")) # True
print(s.isSubsequence("axc", "ahbgdc")) # False
