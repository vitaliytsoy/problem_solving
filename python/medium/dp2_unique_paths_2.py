"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

 
Example 1:

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:

Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
"""
from typing import List

class Solution:
    def find_unique_paths(self, grid, i, j):
        if i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] == 1:
            return 0
        
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return 1
        
        return self.find_unique_paths(grid, i + 1, j) + self.find_unique_paths(grid, i, j + 1)
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.find_unique_paths(obstacleGrid, 0, 0)
    
    # ---

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0] * len(obstacleGrid[0]) for i in range(len(obstacleGrid))]
        dp[0][0] = 1
        
        if (obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1):
            return 0
        
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0 and j == 0 or obstacleGrid[i][j] == 1:
                    continue
                
                if i == 0:
                    dp[i][j] = dp[i][j - 1]
                    continue
                
                if j == 0:
                    dp[i][j] = dp[i - 1][j]
                    continue
                
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
                
        return dp[-1][-1]

s = Solution()
print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])) # 2
print(s.uniquePathsWithObstacles([[0,1],[0,0]])) # 1