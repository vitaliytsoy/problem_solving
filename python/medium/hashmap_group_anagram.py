"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        mapper = {}
        
        for i in range(len(strs)):
            s_word = ''.join(sorted(strs[i]))
            
            if s_word in mapper:
                mapper[s_word].append(i)
                continue
            
            mapper[s_word] = [i]
            
        for indexes in mapper.values():
            result.append(list(map(lambda x: strs[x], indexes)))
            
        return result
    
    
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))

