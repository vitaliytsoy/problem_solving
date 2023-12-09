"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
    
    # ---
    
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        is_last_word = False
        
        for i in range(1, len(s) + 1):
            letter = s[-i]
            
            if letter == ' ':
                if is_last_word:
                    break
                continue
            
            is_last_word = True
            count += 1
        
        return count
    
s = Solution()
print(s.lengthOfLastWord('luffy is still joyboy')) # 6
print(s.lengthOfLastWord('   fly me   to   the moon  ')) # 4
print(s.lengthOfLastWord('Hello World')) # 5
print(s.lengthOfLastWord('')) # 0
