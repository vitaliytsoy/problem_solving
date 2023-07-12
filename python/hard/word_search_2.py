"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
"""

from typing import List

class TrieNode:
    def __init__(self):
        self.edges = {}
        self.is_end_node = False

class Trie:    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        pointer = self.root
        
        for index in range(len(word)):
            letter = word[index]
            
            if (letter not in pointer.edges): 
                pointer.edges[letter] = TrieNode()
            
            pointer = pointer.edges[letter]
        
            if (index == len(word) - 1):
                pointer.is_end_node = True

    def search(self, word: str) -> bool:
        pointer = self.root
        
        for index in range(len(word)):
            letter = word[index]
            
            if letter not in pointer.edges:
                return False
            
            if index == len(word) - 1 and not pointer.edges[letter].is_end_node:
                return False
            
            pointer = pointer.edges[letter]
        
        return True
                
    def startsWith(self, prefix: str) -> bool:
        pointer = self.root
        
        for letter in prefix: 
            if (letter in pointer.edges):
                pointer = pointer.edges[letter]
                continue;
            
            return False
        
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        result_words = []
    
        for word in words:
            trie.insert(word)
            
            
    def helper(self, board, words, result_words)
            
        for row_i, row in enumerate(board):
            for column_i in enumerate(row):
                
