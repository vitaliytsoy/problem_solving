"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:

Input: board = [["X"]]
Output: [["X"]]
"""
from typing import List

class Solution:
    def is_in_bound(self, board, row, col):
        col_len = len(board[0])
        row_len = len(board)
        
        return row >= 0 and row < row_len and col >= 0 and col < col_len;

    def solve(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            if (board[i][0] == "O"):
                self.dfs(board, i, 0)
                pass
            
            if (board[i][len(board[0]) - 1] == "O"):
                self.dfs(board, i, len(board[0]) - 1)
                pass
        
        for i in range(len(board[0])):
            if (board[0][i] == "O"):
                self.dfs(board, 0, i)
                pass
            
            if (board[len(board) - 1][i] == "O"):
                self.dfs(board, len(board) - 1, i)
                pass
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (board[row][col] == "#"):
                    board[row][col] = "O"
                    continue
                    
                if (board[row][col] == "O"):
                    board[row][col] = "X"
                    
        print(board)
        
    def dfs(self, board, row, col):
        if (not self.is_in_bound(board, row, col)):
            return
        
        if (board[row][col] == "X" or board[row][col] == "#"):
            return
        
        if (board[row][col] == "O"):
            board[row][col] = '#'
        
        self.dfs(board, row + 1, col)
        self.dfs(board, row - 1, col)
        self.dfs(board, row, col + 1)
        self.dfs(board, row, col - 1)

                

                    
    
    

s = Solution()
s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
# [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# s.solve([["O","O"],["O","O"]])
# [["O","O"],["O","O"]]
# s.solve([["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]])

# s.solve([["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]])
