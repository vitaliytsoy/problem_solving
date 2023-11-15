"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""
from typing import List

class TrieNode:
    def __init__(self, edges, is_end):
        self.edges = edges
        self.is_end = is_end

class Trie:
    def __init__(self, wordsList):
        self.root_node = TrieNode({}, False)
        
        for word in wordsList:
            pointer = self.root_node
            
            for i in range(len(word)):
                letter = word[i]
                
                if letter not in pointer.edges:
                    pointer.edges[letter] = TrieNode({}, False)
            
                pointer = pointer.edges[letter]
                
                if i == len(word) - 1:
                    pointer.is_end = True
                    
    def startsFrom(self, string):
        pointer = self.root_node
        
        for s in string:
            if s not in pointer.edges:
                return (False, False)
            
            pointer = pointer.edges[s]            
            
        return (True, pointer.is_end)


class Solution:
    def search_word_break(self, s: str, trie: Trie) -> bool:
        temp = ''
        
        if s == '':
            return True
        
        for i in range(len(s)):
            letter = s[i]
            temp += letter
            
            is_starting_from, is_end_word = trie.startsFrom(temp)
            
            if (not is_starting_from):
                return False
            
            if (not is_end_word):
                continue
            
            if self.search_word_break(s[i + 1:], trie):
                return True
    
        return False
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie(wordDict)
                
        return self.search_word_break(s, trie)
    
s = Solution()
print(s.wordBreak('leetcode', ["leet","code"])) # True
print(s.wordBreak('applepenapple', ["apple","pen"])) # True
print(s.wordBreak('catsandog', ["cats","dog","sand","and","cat"])) # False
print(s.wordBreak('bb', ["a","b","bbb","bbbb"])) # True
print(s.wordBreak("aaaaaaa", ["aaaa","aa"])) # False


