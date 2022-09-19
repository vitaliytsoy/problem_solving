"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""
from typing import List
class Solution:
    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        row_len = len(matrix[0])
        col_len = len(matrix)
        top, right, bottom, left = 0, 0, 0, 0
        
        items_count = row_len * col_len
        result = []

        while len(result) < items_count:
            min_iter = min(left, right, top, bottom)

            if top == right and min_iter == top:
                for i in range (0 + left, row_len - right):
                    result.append(matrix[top][i])
                top += 1
                continue
            
            if right == bottom and min_iter == bottom:
                for i in range (0 + top, col_len - bottom):
                    result.append(matrix[i][row_len - right -1])
                right += 1
                continue

            
            if bottom == left and min_iter == bottom:
                for i in range (row_len - right -1, 0 + left - 1, -1):
                    result.append(matrix[(col_len - 1) - bottom][i])
                bottom += 1
                continue


            if left + 1 == top and min_iter == left:
                for i in range (col_len - bottom - 1, 0 + top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
                continue

        return result


solution = Solution()
print(solution.spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
