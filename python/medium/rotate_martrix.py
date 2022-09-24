"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""
from typing import List
from math import floor

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        depth = 0
        max_depth = floor(len(matrix) / 2)

        while depth < max_depth:
            for i in range(depth, size):
                if i + 1 + depth == size:
                    break

                matrix[depth][i], matrix[-(i+1)][depth]  = matrix[-(i+1)][depth], matrix[depth][i]
                matrix[-(i+1)][depth],  matrix[size - 1 - depth][-(i+1)] = matrix[size - 1 - depth][-(i+1)], matrix[-(i+1)][depth]
                matrix[size - 1 - depth][-(i+1)], matrix[i][size - 1 - depth] = matrix[i][size - 1 - depth], matrix[size - 1 - depth][-(i+1)]

            if depth + 1 == max_depth: 
                break
   
            depth += 1

solution = Solution()
# solution.rotate([[1,2,3],[4,5,6],[7,8,9]])
# solution.rotate([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
solution.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
