"""
Given a string s, find the length of the longest substring without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_p = 0
        letters = {}
        max_len = 0
        
        for right_p in range(len(s)):
            letter = s[right_p]
            
            if (letter not in letters):
                max_len = max(max_len, right_p - left_p + 1)
                letters[letter] = right_p
                continue
            
            if letters[letter] < left_p:
                max_len = max(max_len, right_p - left_p + 1)
            else:
                left_p = letters[letter] + 1
        
            letters[letter] = right_p

        return max_len

                    
                
                    
            

    
s = Solution()

print(s.lengthOfLongestSubstring('  '))
# print(s.lengthOfLongestSubstring('dvdf'))
