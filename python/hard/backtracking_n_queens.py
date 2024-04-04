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
from collections import deque

def print_m(board):
    print('========')
    for row in board:
        print(row)

class Solution:
    def place_queen(self, board, i, j):
        board = deepcopy(board) 

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
    
    def find_solution(self, board, queens_count):
        solutions = 0
        stack = deque()
        visited = set()
        
        stack.append([deepcopy(board), queens_count, []])
        
        while stack:
            board, q_left, queens = stack.pop()
 
            if q_left == 0:
                signature = str(sorted(queens))
                
                if signature in visited:
                    continue
                
                solutions += 1
                visited.add(signature)
                    
                continue
            
            
            for i in range(len(board)):
                for j in range(len(board[0])):
                    cell = board[i][j]
                    
                    if cell == 1:
                        continue
                    
                    new_board = self.place_queen(board, i, j)
                    new_queens = queens.copy()
                    
                    new_queens.append((i, j))

                    stack.append([new_board, q_left - 1, new_queens])
                
        return solutions
    
    def totalNQueens(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        board = [[0] * n for _ in range(n)]
        
        return self.find_solution(board, n)
    
    # ---
    
    def totalNQueens(self, n: int) -> int:
        cols = [False] * n
        d1 = [False] * (n * 2)
        d2 = [False] * (n * 2)
        
        return self.find_solution(0, cols, d1, d2, n)

    
    def find_solution(self, row, cols, d1, d2, n):
        count = 0
        
        if row == n:
            return 1

        for col in range(n):
            diag1 = col - row + n
            diag2 = col + row
            
            if cols[col] or d1[diag1] or d2[diag2]:
                continue
            
            cols[col] = True
            d1[diag1] = True
            d2[diag2] = True
            
            count += self.find_solution(row + 1, cols, d1, d2, n)
            
            cols[col] = False
            d1[diag1] = False
            d2[diag2] = False
            
        return count
            
# 0 0 0 0
# 0 0 1 0
# 0 0 0 0
# 0 0 0 0

s = Solution()
print(s.totalNQueens(4)) # 2
print(s.totalNQueens(1)) # 1
print(s.totalNQueens(5)) # 10
print(s.totalNQueens(6)) # 4
