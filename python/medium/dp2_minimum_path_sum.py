"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""
from typing import List
import sys

class Solution:
    # def find_min_path(self, grid: List[List[int]], total, i, j):        
    #     if i == len(grid) - 1 and j == len(grid[0]) - 1:
    #         return total + grid[i][j]
        
    #     if i >= len(grid) or j >= len(grid[0]):
    #         return sys.maxsize
        
    #     return min(
    #         self.find_min_path(grid, total + grid[i][j], i, j + 1),
    #         self.find_min_path(grid, total + grid[i][j], i + 1, j),    
    #     )
    
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     return self.find_min_path(grid, 0, 0, 0)
    
    # ---
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0]) for i in range(len(grid))]
        dp[0][0] = grid[0][0]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                
                num = grid[i][j]
                
                if i == 0:
                    dp[i][j] = dp[i][j-1] + num
                    continue
                
                if j == 0:
                    dp[i][j] = dp[i-1][j] + num
                    continue
                
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + num
                
        return dp[-1][-1]


s = Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]])) # 7 
print(s.minPathSum([[1,2,3],[4,5,6]])) # 12
