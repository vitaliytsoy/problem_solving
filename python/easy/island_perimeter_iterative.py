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
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        result = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):                
                if (grid[row][col] == 1):
                    if row == 0 or grid[row-1][col] == 0:
                        result += 1
                        
                    if col == 0 or grid[row][col-1] == 0:
                        result += 1
                        
                    if row == row_len - 1 or grid[row + 1][col] == 0:
                        result += 1
                        
                    if col == col_len - 1 or grid[row][col + 1] == 0:
                        result += 1
                        
        return result
    
s = Solution()

print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])) # 16
print(s.islandPerimeter([[1]])) # 4
print(s.islandPerimeter([[1,0]])) # 4


# [0,1,0,0],
# [1,1,1,0],
# [0,1,0,0],
# [1,1,0,0]