"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Example 1:

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

"""
from typing import List

neighbours = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

class Solution:
    def get_alive_neighbours_count(self, board, i, j):
        count = 0
        
        for neigbours in neighbours:
            i_mod, j_mod = neigbours
            
            if i + i_mod < 0 or i + i_mod >= len(board):
                continue
            
            if j + j_mod < 0 or j + j_mod >= len(board[0]):
                continue
            
            if board[i + i_mod][j+j_mod] == 1:
                count += 1
            
        return count
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        alive = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                alive[i][j] = self.get_alive_neighbours_count(board, i, j)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if alive[i][j] == 2 or alive == 3:
                    continue
                
                if alive[i][j] == 3:
                    board[i][j] = 1
                    continue
                
                board[i][j] = 0
                
                
        # ---
        
    def get_alive_neighbours_count(self, board, i, j):
        count = 0
        
        for neigbours in neighbours:
            i_mod, j_mod = neigbours
            
            if i + i_mod < 0 or i + i_mod >= len(board):
                continue
            
            if j + j_mod < 0 or j + j_mod >= len(board[0]):
                continue
            
            if (board[i + i_mod][j+j_mod] >> 0) & 1 == 1:
                count += 1
            
        return count
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                alive_n = self.get_alive_neighbours_count(board, i, j)
                
                if (board[i][j] >> 0):  
                    board[i][j] = board[i][j] | (1 << 1)
                else:
                    board[i][j] = board[i][j] & ~(1 << 1)
                    
                
                if alive_n == 2 or board == 3:
                    continue
                
                if alive_n == 3:
                    board[i][j] = board[i][j] | (1 << 1)
                    continue

                board[i][j] = board[i][j] & ~(1 << 1)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = (board[i][j] >> 1) & 1
                
s = Solution()
print(s.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])) # [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
print(s.gameOfLife([[1,1],[1,0]])) # [[1,1],[1,1]]
        