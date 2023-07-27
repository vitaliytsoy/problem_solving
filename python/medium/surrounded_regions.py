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
    def is_in_bound(self, board, row, col):
        col_len = len(board[0])
        row_len = len(board)
        
        return row >= 0 and row < row_len and col >= 0 and col < col_len;

    def solve(self, board: List[List[str]]) -> None:
        queue = deque()
        visited = [[False for i in range(len(board[0]))] for i in range(len(board))]
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (board[row][col] == 'X'):
                    continue;
                
                queue.append((row, col))
        
        while queue:
            row, col = queue.popleft()
            
            if (visited[row][col]):
                continue
            
            self.hepler(board, visited, row, col)
                       
        print(board)
        
    def hepler(self, board, visited, row, col):
            if (not self.is_in_bound(board, row, col) or board[row][col] == "X"):
                return
        
            directions = [(row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)]
            visited[row][col] = True
            is_persist = False
            
            for direction in directions:
                dir_row, dir_col = direction
                
                if (not self.is_in_bound(board, dir_row, dir_col)):
                    is_persist = True
                    break
                
                if (board[dir_row][dir_col] == "O" and visited[dir_row][dir_col]):
                    is_persist = True
                    break
                        
            if (not is_persist):
                board[row][col] = "X"
                
            for direction in directions:
                dir_row, dir_col = direction 
                
                if (not self.is_in_bound(board, dir_row, dir_col) or visited[dir_row][dir_col]): 
                    continue
                                
                self.hepler(board, visited, dir_row, dir_col)
                    


                

                    
    
    

s = Solution()
# s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
# [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# s.solve([["O","O"],["O","O"]])
# [["O","O"],["O","O"]]
# s.solve([["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]])

s.solve([["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]])

# ["O","X","X","O","X"],
# ["X","O","O","X","O"],
# ["X","O","X","O","X"],
# ["O","X","O","O","O"],
# ["X","X","O","X","O"]


# ["O","X","X","O","X"],
# ["X","X","X","X","O"],
# ["X","X","X","O","X"],
# ["O","X","O","O","O"],
# ["X","X","O","X","O"]


# ["O","X","X","O","X"],
# ["X","X","X","X","O"],
# ["X","X","X","X","X"],
# ["O","X","X","X","O"],
# ["X","X","O","X","O"]

