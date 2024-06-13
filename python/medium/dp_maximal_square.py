"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:

Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
"""

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[False] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        max_size = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                    max_size = max(dp[i+1][j+1], max_size)
                    
                    
        return max_size ** 2
    
s = Solution()
print(s.maximalSquare([
    ["0", "1", "1"],
    ["1", "1", "1"],
    ["1", "1", "1"],
    ["0", "1", "1"]
])) # 4
print(s.maximalSquare([
    ["1", "1", "1"],
    ["1", "1", "1"],
    ["1", "1", "1"],
    ["1", "1", "1"]
])) # 9
print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])) # 4
print(s.maximalSquare([["0","1"],["1","0"]])) # 1
print(s.maximalSquare([["0"]])) # 0