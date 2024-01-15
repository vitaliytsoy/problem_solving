"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
"""
import functools

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapper = {}
        
        for letter in s:
            if letter in mapper:
                mapper[letter] += 1
                continue
                
            mapper[letter] = 1
            
        for letter in t:
            if letter not in mapper:
                return False
            
            mapper[letter] -= 1
            
        return functools.reduce(lambda acc, item: False if not acc or item != 0 else True, mapper.values(), True)
    
    # ---
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
         
        s_sorted = list(s)
        t_sorted = list(t)
        
        s_sorted.sort()
        t_sorted.sort()
        
        for i in range(len(s_sorted)):
            if s_sorted[i] != t_sorted[i]:
                return False
        
        return True
    

s = Solution()
print(s.isAnagram("rat", "car")) # False
print(s.isAnagram("anagram", "nagaram")) # True