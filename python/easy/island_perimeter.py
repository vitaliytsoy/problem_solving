"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
 
Example 1:

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:

Input: grid = [[1]]
Output: 4

Example 3:

Input: grid = [[1,0]]
Output: 4
"""
from typing import List

class Solution:
    def is_in_grid_range(self, grid, row, col):
        col_len = len(grid[0])
        row_len = len(grid)
        
        return row >= 0 and row < row_len and col >= 0 and col < col_len;
        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == 1):
                    return self.dfs(grid, row, col)
                
    def dfs(self, grid, row, col):
        if (not self.is_in_grid_range(grid, row, col) or grid[row][col] == 0 or grid[row][col] == -1):
            return 0
        
        ground_neighbours = 0
        directions = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        grid[row][col] = -1
        
        for direction in directions:
            dir_row, dir_col = direction
            
            if (not self.is_in_grid_range(grid, dir_row, dir_col)):
                continue
            
            if (grid[dir_row][dir_col] == 1 or grid[dir_row][dir_col] == -1):
                ground_neighbours += 1
        
        return (4 - ground_neighbours) \
            + self.dfs(grid, row + 1, col) \
            + self.dfs(grid, row - 1, col) \
            + self.dfs(grid, row, col + 1) \
            + self.dfs(grid, row, col - 1) 
    
s = Solution()
print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])) # 16
print(s.islandPerimeter([[1]])) # 4
print(s.islandPerimeter([[1,0]])) # 4


# [0,1,0,0],
# [1,1,1,0],
# [0,1,0,0],
# [1,1,0,0]