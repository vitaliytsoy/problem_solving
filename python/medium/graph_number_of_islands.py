"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from typing import List

class Solution:
    def mark_island(self, grid: List[List[str]], i: int, j: int):
        if 0 > i or i >= len(grid) or 0 > j or j >= len(grid[0]):
            return 
        
        land = grid[i][j]
        
        if land == "#" or land == "0":
            return
        
        if land == "1": 
            grid[i][j] = "#"
            
            self.mark_island(grid, i + 1, j)
            self.mark_island(grid, i, j + 1)
            self.mark_island(grid, i - 1, j)
            self.mark_island(grid, i, j - 1)

    
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                land  = grid[i][j]
                
                if land == "0" or land == "#":
                    continue
                
                if land == "1":
                    self.mark_island(grid, i, j)
                    counter += 1
                
        return counter
                
    
s = Solution()
print(s.numIslands([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
])) # 3

print(s.numIslands([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
])) # 1