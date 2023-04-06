"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2


Example 2:

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
"""
from typing import List, MutableSet

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        province_count = 0
        
        for i in range(len(isConnected)):
            if i not in visited:
                province_count += 1
                self.dfs(i, isConnected, visited)
                
        return province_count
            
    def dfs(self, node: int, matrix: List[List[int]], visited: MutableSet[int],):
        visited.add(node)
        
        for n in range(len(matrix)):
            if matrix[node][n] == 1 and n not in visited:
                self.dfs(n, matrix, visited)
        
        
s = Solution()

print(s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
print(s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
                
    
    
    
"""
 [1,1,0],
 [1,1,0],
 [0,0,1]
"""

"""
[1,0,0],
[0,1,0],
[0,0,1]
"""