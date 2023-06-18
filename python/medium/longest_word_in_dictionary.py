"""
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

Note that the word should be built from left to right with each additional character being added to the end of a previous word. 


Example 1:

Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".


Example 2:

Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
 
Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 30
words[i] consists of lowercase English letters.
"""
from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        built = set()
        sorted_words = sorted(words)
        longest_word = ''
        
        print(sorted_words)
        
        for word in sorted_words:
            if (len(word) == 1 or word[0:-1] in built):
                built.add(word)
                
                if (len(word) > len(longest_word)):
                    longest_word = word
                    
        return longest_word
                
    
s = Solution()
# print(s.longestWord([ "worl", "wor", "wo", "world", "w"]))
print(s.longestWord(["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]))



