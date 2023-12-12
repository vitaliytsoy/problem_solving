"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1. 
"""
class Solution:    
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
    # ---
    
    def find_needle(self, haystack: str, needle: str, start):    
        if needle == '':
            return start

        if haystack == '' or haystack[0] != needle[0]:
            return -1
        
        return self.find_needle(haystack[1:], needle[1:], start)
        
    
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        for i in range(len(haystack)):
            letter = haystack[i]
            
            if letter == needle[0]:
                result = self.find_needle(haystack[i:], needle, i)
                
                if result != -1:
                    return result

        return -1

            
    
s = Solution()
print(s.strStr("sadbutsad", "sad")) # 0
print(s.strStr("leetcode", "leeto")) # -1
print(s.strStr("mississippi", "issip")) # 4
print(s.strStr("aaa", "aaaa")) # -1
print(s.strStr("mississippi", "issipi")) # -1


