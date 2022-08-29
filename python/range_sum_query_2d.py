from typing import List

class NumMatrix:
    """
    Given a 2D matrix matrix, handle multiple queries of the following type:

    Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
    Implement the NumMatrix class:

    NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
    int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
    You must design an algorithm where sumRegion works on O(1) time complexity.
    """
    # [3, 0, 1, 4, 2], 
    # [5, 6, 3, 2, 1], 
    # [1, 2, 0, 1, 5], 
    # [4, 1, 0, 1, 7],
    # [1, 0, 3, 0, 5]

    # sum(row2 col2) - sum(row2 col1-1) - sum(row1-1 col2) + sum(row1-1 col1-1)
    def __init__(self, matrix: List[List[int]]):
        self.source = matrix
        self.sums = []

        for i in range(0, len(matrix)):
            self.sums.append([])

            for j in range (0, len(matrix[i])):
                result = matrix[i][j]

                if i > 0:
                    result = matrix[i][j] + self.sums[i - 1][j]

                if j > 0:
                    result = matrix[i][j] if j == 0 else matrix[i][j] + self.sums[i][j - 1]
                
                if i > 0 and j > 0:
                    result = self.sums[i][j - 1] + self.sums[i - 1][j] - self.sums[i - 1][j - 1] + matrix[i][j]
                    
                    # matrix[i - 1][j] + matrix[i][j]
                    # print(f"IJ[{i}-{j}]: {self.sums[i][j - 1]} + {matrix[i - 1][j]} + {matrix[i][j]} = {result}")


                self.sums[i].append(result)



        for i in range(0, len(self.sums)):
            print(self.sums[i])


    def get_sum(self, row: int, col: int) -> int:
        if (row < 0 or col < 0): return 0

        return self.sums[row][col]
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.get_sum(row2, col2) - self.get_sum(row2, col1 - 1) - self.get_sum(row1 - 1, col2) + self.get_sum(row1 - 1, col1 - 1)


obj = NumMatrix([
    [3, 0, 1, 4, 2], 
    [5, 6, 3, 2, 1], 
    [1, 2, 0, 1, 5], 
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
])

sums = [
    [3, 3, 1, 5, 6], 
    [5, 11, 9, 5, 3], 
    [1, 3, 2, 1, 6], 
    [4, 5, 1, 1, 8], 
    [1, 1, 3, 3, 5]
]

print(obj.sumRegion(2, 1, 4, 3)) # 8
print(obj.sumRegion(1, 1, 2, 2)) # 11
print(obj.sumRegion(1, 2, 2, 4)) # 12   


# Input
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# Output
# [null, 8, 11, 12]