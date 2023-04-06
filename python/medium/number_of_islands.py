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
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False for x in range(cols)] for y in range(rows)] 
        
        for row in range(rows):
            for col in range(cols):
                item = grid[row][col]
                
                if not visited[row][col] and item == '1':
                    count += 1
                    self.searchBoundaries(row, col, grid, visited)
                    
        return count
    
    def checkIsInBoundaries(self, row, col, grid): 
            rows, cols = len(grid) - 1, len(grid[0]) - 1

            if row < 0 or row > rows:
                return False
            
            if col < 0 or col > cols:
                return False
            
            return True
    
    def searchBoundaries(self, row, col, grid, visited):
        top, bottom, right, left = (row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)
        
        if self.checkIsInBoundaries(top[0], top[1], grid) and not visited[top[0]][top[1]] and grid[top[0]][top[1]] == '1':
            visited[top[0]][top[1]] = True
            self.searchBoundaries(top[0], top[1], grid, visited)
            
        if self.checkIsInBoundaries(bottom[0], bottom[1], grid) and not visited[bottom[0]][bottom[1]] and grid[bottom[0]][bottom[1]] == '1':
            visited[bottom[0]][bottom[1]] = True
            self.searchBoundaries(bottom[0], bottom[1], grid, visited)
            
        if self.checkIsInBoundaries(right[0], right[1], grid) and not visited[right[0]][right[1]] and grid[right[0]][right[1]] == '1':
            visited[right[0]][right[1]] = True
            self.searchBoundaries(right[0], right[1], grid, visited)
            
        if self.checkIsInBoundaries(left[0], left[1], grid) and not visited[left[0]][left[1]] and grid[left[0]][left[1]] == '1':
            visited[left[0]][left[1]] = True
            self.searchBoundaries(left[0], left[1], grid, visited)
            
    
s = Solution()


print(s.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
"""
[[True, True, True, True, False], 
[True, True, True, True, False], 
[True, True, True, True, False], 
[True, True, True, True, False]]
"""

print(s.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
