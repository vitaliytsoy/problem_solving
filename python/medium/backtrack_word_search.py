"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""
from typing import List

class Solution:
    def dfs(self, board, visited, word, i, j, count):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        
        if visited[i][j]:
            return False
        
        cell = board[i][j]
        
        if cell == word[count]:
            if count + 1 == len(word):
                return True
            
            visited[i][j] = True
            
            if self.dfs(board, visited, word, i + 1, j, count + 1):
                return True
            if self.dfs(board, visited, word, i, j + 1, count + 1):
                return True
            if self.dfs(board, visited, word, i - 1, j, count + 1):
                return True
            if self.dfs(board, visited, word, i, j - 1, count + 1):
                return True
            
            visited[i][j] = False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                cell = board[i][j]
            
                if cell == word[0]:
                    visited = [[False] * len(board[0]) for _ in range(len(board))]
                    
                    if (self.dfs(board, visited, word, i, j, 0)):
                        return True
                    
        return False
    
s = Solution()
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # true
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")) # true
print(s.exist([
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]], "ABCB")) # false
print(s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS")) # true
print(s.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], "AAAAAAAAAAAAAAB")) # false
print(s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS")) # true

