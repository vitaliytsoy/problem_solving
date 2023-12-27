"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l_mapper = {}
        w_mapper = {}
        words = s.split(' ')
        
        if len(pattern) != len(words):
            return False
        
        for i in range(len(pattern)):
            letter = pattern[i]
            word = words[i]
            
            if letter in l_mapper and word not in w_mapper:
                return False
            
            if letter not in l_mapper and word in w_mapper:
                return False
            
            if letter in l_mapper and word in w_mapper and (l_mapper[letter] != word or w_mapper[word] != letter):
                return False
            
            l_mapper[letter] = word
            w_mapper[word] = letter

        return True

    
s = Solution()
print(s.wordPattern("abba", "dog cat cat dog")) # True
print(s.wordPattern("abba", "dog cat cat fish")) # False
print(s.wordPattern("aaaa", "dog cat cat dog")) # False
print(s.wordPattern("bcbd", "dog cat dog fish")) # True
print(s.wordPattern("abba", "dog dog dog dog")) # False
