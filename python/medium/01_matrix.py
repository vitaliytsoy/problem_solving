"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]


Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""
from typing import List
from collections import deque

class Solution:
    def is_in_matrix_range(self, row, col, row_len, col_len):
        return row < col_len and row >= 0 and col < row_len and col >= 0
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = [[False for i in range(len(mat[0]))] for i in range(len(mat))]
        queue = deque()
        row_len = len(mat[0])
        col_len = len(mat)
    
        for row in range(len(mat)):
            for col in range(len(mat[0])):                
                if (mat[row][col] == 0):
                    queue.append((row, col))
                    visited[row][col] = True
                    
                    
        while queue:
            row, col = queue.popleft()
            
            # print(row, col)
            # print(row_len, col_len)
            # print(self.is_in_matrix_range(row + 1, col, row_len, col_len))
            # print(self.is_in_matrix_range(row - 1, col, row_len, col_len))
            # print(self.is_in_matrix_range(row, col + 1, row_len, col_len))
            # print(self.is_in_matrix_range(row, col - 1, row_len, col_len))
            
            if (self.is_in_matrix_range(row + 1, col, row_len, col_len)):
                if (visited[row + 1][col]):
                    if (mat[row + 1][col] > mat[row][col] + 1):
                        mat[row + 1][col] = mat[row][col] + 1
                else:
                    mat[row + 1][col] = mat[row][col] + 1
                    visited[row + 1][col] = True
                    queue.append((row + 1, col))
            
            if (self.is_in_matrix_range(row, col + 1, row_len, col_len)):
                if (visited[row][col + 1]):
                    if (mat[row][col + 1] > mat[row][col] + 1):
                        mat[row][col + 1] = mat[row][col] + 1
                else:
                    mat[row][col + 1] = mat[row][col] + 1
                    visited[row][col + 1] = True
                    queue.append((row, col + 1))
            
            if (self.is_in_matrix_range(row - 1, col, row_len, col_len)):
                if (visited[row - 1][col]):
                    if (mat[row - 1][col] > mat[row][col] + 1):
                        mat[row - 1][col] = mat[row][col] + 1
                else:
                    mat[row - 1][col] = mat[row][col] + 1
                    visited[row - 1][col] = True
                    queue.append((row - 1, col))
            
            if (self.is_in_matrix_range(row, col - 1, row_len, col_len)):
                if (visited[row][col - 1]):
                    if (mat[row][col - 1] > mat[row][col] + 1):
                        mat[row][col - 1] = mat[row][col] + 1
                else:
                    mat[row][col - 1] = mat[row][col] + 1
                    visited[row][col - 1] = True
                    queue.append((row, col - 1))
            
        return mat
            
                
    
s = Solution()
# print(s.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])) # [[0,0,0],[0,1,0],[0,0,0]]
print(s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])) # [[0,0,0],[0,1,0],[1,2,1]]
# print(s.updateMatrix([[0],[0],[0],[0],[0]])) #

# 
# [-,-,-],
# [-,1,-],
# [1,1,1]