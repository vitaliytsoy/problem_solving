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
    
    
    
    def search_word_break(self, s: str, word_set: set) -> bool:
        word = ''
        
        if s == '':
            return True
        
        for i in range(len(s)):
            word += s[i]
            
            if word in word_set and self.search_word_break(s[i + 1:], word_set):
                return True
        
    
        return False
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_start = [False] * len(s)
        word_end = [False] * len(s)
        trie = Trie(wordDict)
        
        i = 0
        
        while i < len(s):
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                is_starting_from, is_end_word = trie.startsFrom(word)

                print(i, j)
                print(word_start)
                print(word_end)

                if not is_starting_from:
                    if (i == 0):
                        i += 1

                    while i < len(s) and not word_end[i]:
                        i += 1
                        
                    i += 1

                    break
                        
                
                if is_end_word:
                    word_start[i] = True
                    word_end[j - 1] = True
                    
            i += 1
            
        print(word_start)
        print(word_end)
                    
                    
        # if not wb[-1] or not wb[0]:
        #     return False
        
        # pointer = 1
        
        # while pointer < len(s) - 1:
        #     if not wb[pointer]:
        #         pointer += 1
        #         continue
            
        #     if not wb[pointer + 1]:
        #         return False
            
        #     pointer += 2
            
        
        return True
        
                    
        print(wb)
    
s = Solution()
# print(s.wordBreak('leetcode', ["leet","code"])) # True
# print(s.wordBreak('applepenapple', ["apple","pen"])) # True
# print(s.wordBreak('catsandog', ["cats","dog","sand","and","cat"])) # False
# print(s.wordBreak('bb', ["a","b","bbb","bbbb"])) # True
print(s.wordBreak("aaaaaaa", ["aaaa","aa"])) # False
# print(s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))



