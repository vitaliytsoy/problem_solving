"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]
"""
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {};

        for word in strs: 
            normalized_key = ''.join(sorted(list(word)))

            if normalized_key not in dict:
                dict[normalized_key] = [word]
            else:
                dict[normalized_key].append(word)

        return dict.values()

        

solution = Solution()

solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])

# 2 + 4 = 6
# 3 + 3 = 6