"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            word = strs[i]
            
            if len(word) < len(prefix):
                prefix = prefix[0:len(word)]
            
            for j in range(len(word)):
                if len(prefix) == 0 or j >= len(prefix):
                    break
                
                if (word[j] == prefix[j]):
                    continue
                
                prefix = prefix[0:j]
                
        return prefix
    
    # ---
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return 0 
        
        if len(strs) == 1:
            return strs[0]
        
        strs.sort()
    
        result = ""
        
        for i in range(min((len(strs[0]), len(strs[-1])))):
            if (strs[0][i]!= strs[-1][i]):
                break

            result += strs[0][i]
      
        return  result
    
    
    
s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"])) # fl
print(s.longestCommonPrefix(["dog","racecar","car"])) # ''
print(s.longestCommonPrefix(["ab","a"])) # 'a'
