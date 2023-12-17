"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
from typing import List

NEXT_DIRECTION = {
    'up': 'right',
    'right': 'down',
    'down': 'left',
    'left': 'up'
}

class Solution:    
    def make_spiral(self, matrix, i, j, direction, result):        
        if len(result) == len(matrix) * len(matrix[0]):
            return 
        
        result.append(matrix[i][j])
        matrix[i][j] = '#'
                
        if direction == 'right':

            if j + 1 == len(matrix[0]) or matrix[i][j + 1] == '#':
                self.make_spiral(matrix, i + 1, j, NEXT_DIRECTION[direction], result)
            else:
                self.make_spiral(matrix, i, j + 1, direction, result)
            
        elif direction == 'down':
            if i + 1 == len(matrix) or matrix[i + 1][j] == '#':
                self.make_spiral(matrix, i, j - 1, NEXT_DIRECTION[direction], result)
            else:
                self.make_spiral(matrix, i + 1, j, direction, result)
            
        elif direction == 'left':
            if j == 0 or matrix[i][j - 1] == '#':
                self.make_spiral(matrix, i - 1, j, NEXT_DIRECTION[direction], result)
            else:
                self.make_spiral(matrix, i, j - 1, direction, result)
            
        elif direction == 'up':
            if i == 0 or matrix[i - 1][j] == '#':
                self.make_spiral(matrix, i, j + 1, NEXT_DIRECTION[direction], result)
            else:
                self.make_spiral(matrix, i - 1, j, direction, result)
        
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if (len(matrix) == 0):
            return []
        
        if (len(matrix) == 1):
            return matrix[0]
        
        result = []
        
        self.make_spiral(matrix, 0, 0, 'right', result)
        
        return result


    
s = Solution()
# print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]
# print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # [1,2,3,4,8,12,11,10,9,5,6,7]
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])) # 

# [1,2,3,4],
# [5,6,7,8],
# [9,10,11,12],
# [13,14,15,16]
# 1 2 3 4 8 12 16 15 14 13 9 5 6 7
