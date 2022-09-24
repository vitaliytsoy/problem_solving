"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true

Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
"""
from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        dict: dict[str, set] = {}

        for r, row in enumerate(matrix):
            for c, column in enumerate(row):
                key = r - c

                if key not in dict:
                    dict[key] = {column}
                else:
                    dict[key].add(column)

        for diagonal in dict.values():
            if len(diagonal) > 1:
                return False

        return True

a = set()

a.add
solution = Solution()
print(solution.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))