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
        is_on_right = False
        is_on_bottom = False
        
        items_count = row_len * col_len
        result = []
        iterations = 0

        while len(result) < items_count:
            min_iter = min(left, right, top, bottom)

            print(min_iter)

            if top == right and min_iter == top:
                print('TOP')
                for i in range (0 + left, row_len - right):
                    result.append(matrix[top][i])
                top += 1
                is_on_right = True
                continue;
            
            if right == bottom and min_iter == bottom:
                print('RIGHT')
                for i in range (0 + top, col_len - bottom):
                    result.append(matrix[i][row_len - right -1])
                right += 1
                is_on_bottom = True
                continue;

            
            if bottom == left and min_iter == bottom:
                print('BOTTOM')
                for i in range (row_len - right, 0 + left, -1):
                    result.append(matrix[bottom][-i])
                bottom += 1
                is_on_right = False
                continue;


            if left + 1 == top and min_iter == left:
                print('LEFT')
                for i in range (col_len - bottom, 0 + top, -1):
                    result.append(matrix[i][left])
                left += 1
                is_on_bottom = False
                continue;

            


            iterations += 1
            if(iterations > 20): break

        return result




# is_row = True
# print(is_row)
# is_row = not is_row
# print(is_row)


# for i in range(9, 6, -1):
    # print(i)

solution = Solution()
print(solution.spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

# [1,2,3,4]
# [5,6,7,8]
# [9,10,11,12]
# [9,10,11,12]
