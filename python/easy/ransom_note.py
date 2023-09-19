"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        
        for letter in ransomNote:
            if (letter in letters):
                letters[letter] += 1
            else:
                letters[letter] = 1
                
                
        counter = len(ransomNote)
                
        for letter in magazine:
            if counter == 0:
                break
            
            if letter not in letters:
                continue;
            
            if letters[letter] >= 1:
                counter -= 1
                letters[letter] -= 1
                
        return counter == 0
    
s = Solution()
print(s.canConstruct('a', 'b')) # False
print(s.canConstruct('aa', 'ab')) # False
print(s.canConstruct('aa', 'aab')) # True
print(s.canConstruct('fihjjjjei', 'hjibagacbhadfaefdjaeaebgi')) # False
            
                
            