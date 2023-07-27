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

class Solution:    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        result_words = []
    
        for word in words:
            trie.insert(word)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.helper(board, words, trie.root, '', row, col, result_words)
                
        return result_words
            
            
    def helper(self, board: List[List[str]], words: List[str], node: TrieNode, word: str, row: int, column: int, res: List[str]):        
        if (node.is_end_node):
            res.append(word)
            node.is_end_node = False
        
        if (row >= len(board) or row < 0 or column >= len(board[0]) or column < 0):
            return
        
        if (len(words) == len(res)):
            return
        
        if (board[row][column] not in node.edges):
            return
        
        temp = board[row][column]
        word += board[row][column]
        node = node.edges[temp]
        board[row][column] = '#'
            
        self.helper(board, words, node, word, row + 1, column, res)
        self.helper(board, words, node, word, row, column + 1, res)
        self.helper(board, words, node, word, row - 1, column, res)
        self.helper(board, words, node, word, row, column - 1, res)
        
        board[row][column] = temp
                
s = Solution()

# print(s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])) # ["eat","oath"]
# print(s.findWords([["a"]], ["a"])) # ["a"]
# print(s.findWords([["a","b"],["c","d"]], ["abcb"])) # []
# print(s.findWords([["a","b"]], ["a", "b"])) # []

board = [["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]]
words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(s.findWords(board, words)) # []


                
# print(len([1,2,3]))