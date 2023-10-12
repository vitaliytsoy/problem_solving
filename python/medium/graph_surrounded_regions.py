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
from collections import deque

class Solution:
    def flip_region(self, board, visited, i, j):
        stack = deque([(i, j)])
        has_boundary_cell = False
        region = []
        
        while stack:
            m, n = stack.pop()
        
            if 0 > m or m > len(board) - 1 or 0 > n or n > len(board[0]) - 1:
                continue
            
            node = board[m][n]
            
            if visited[m][n] or node == "X":
                continue
            
            if m == 0 or m == len(board) - 1 or n == 0 or n == len(board[0]) - 1:
                has_boundary_cell = True
                
            visited[m][n] = True
            region.append((m, n))
            stack.append((m + 1, n));
            stack.append((m, n + 1));
            stack.append((m - 1, n));
            stack.append((m, n - 1));
            
        return [] if has_boundary_cell else region
        
        
    def solve(self, board: List[List[str]]) -> None:
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                node = board[i][j]
                
                if visited[i][j] or node == "X":
                    continue
                
                region = self.flip_region(board, visited, i, j)
                
                if region:
                    for node in region:
                        n, m = node
                        board[n][m] = 'X'
                        
        return board
    
s = Solution()
print(s.solve(
    [["X","X","X","X"],
     ["X","O","O","X"],
     ["X","X","O","X"],
     ["X","O","X","X"]]
)) # [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

print(s.solve(
    [["O","X","X","O","X"],
     ["X","O","O","X","O"],
     ["X","O","X","O","X"],
     ["O","X","O","O","O"],
     ["X","X","O","X","O"]]
)) # [["O","X","X","O","X"],["X","X","X","X","O"],["X","X","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]

print(s.solve(
    [["X"]]
)) # [["X"]]
