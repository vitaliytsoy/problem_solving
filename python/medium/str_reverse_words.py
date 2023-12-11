"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        splited = s.split(' ')
        result = []
        
        for i in range(1, len(splited) + 1):
            word = splited[-i]
            
            if word == '':
                continue
            
            result.append(word)
            
        return ' '.join(result)

    
s = Solution()
print(s.reverseWords("  hello world  ")) # world hello
print(s.reverseWords("the sky is blue")) # blue is sky the
print(s.reverseWords("a good   example")) # example good a