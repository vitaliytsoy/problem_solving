"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:

Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:

Input: n = 1
Output: 1
"""
from copy import deepcopy

class Solution:
    def place_queen(self, board, i, j):        
        for n in range(len(board)):
            board[n][j] = 1
            board[i][n] = 1
            
            if  i - n >= 0 and j - n >= 0:
                board[i - n][j - n] = 1
                
            if  i + n < len(board) and j + n < len(board[0]):
                board[i + n][j + n] = 1
                
            if  i + n < len(board) and j - n >= 0:
                board[i + n][j - n] = 1
                
            if  i - n >= 0 and j + n < len(board[0]):
                board[i - n][j + n] = 1
        
        return board
    
    def is_board_has_empty(self, board):
        s = 0
        
        for row in board:
            s += sum(row)
            
        return s < (len(board) * len(board))
    
    def find_solution(self, board):
        if not self.is_board_has_empty(board):
            return 0 
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                cell = board[i][j]
                
                if cell == 1:
                    continue
                
                self.place_queen(board, i, j)
                self.find_solution(deepcopy(board))
        
    
    def totalNQueens(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        board = [[0] * n for _ in range(n)]
        
        return self.find_solution(board)
        
        
        
# 0 0 0 0
# 0 0 1 0
# 0 0 0 0
# 0 0 0 0

# 0 3
# 1 2
# 2 1
# 3 0

# 0 1
# 1 2
# 2 3  
s = Solution()
# print(s.totalNQueens(4)) # 2
# print(s.totalNQueens(1)) # 1

board = [[0] * 4 for _ in range(4)]


print(board)
print()

for row in s.place_queen(board, 2, 2):
    print(row)
    
    
sum
print()
