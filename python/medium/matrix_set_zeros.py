"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '#' or matrix[i][j] != 0:
                    continue
                
                for m in range(len(matrix)):
                    if matrix[m][j] == 0:
                        continue
                    
                    matrix[m][j] = '#'
                    
                for n in range(len(matrix[0])):
                    if matrix[i][n] == 0:
                        continue
                    
                    matrix[i][n] = '#'
            
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '#':
                    matrix[i][j] = 0
    
s = Solution()
# print(s.setZeroes([[1,1,1],[1,0,1],[1,1,1]])) # [[1,0,1],[0,0,0],[1,0,1]]
print(s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])) # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        