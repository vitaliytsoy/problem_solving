"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:

Input: triangle = [[-10]]
Output: -10
"""
from typing import List
import sys 

class Solution:
    def find_min_path_sum(self, triangle, total, i, j): 
        if (i == len(triangle)):
            return total
        
        num = triangle[i][j]
        
        return min(self.find_min_path_sum(triangle, total + num, i + 1, j), self.find_min_path_sum(triangle, total + num, i + 1, j + 1))
                
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0:
            return 0

        return self.find_min_path_sum(triangle, 0, 0, 0)
                

                
        pass
    
    
s = Solution()
print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])) # 11
print(s.minimumTotal([[-10]])) # -10