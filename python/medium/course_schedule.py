"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.


Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""
from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, pre_course in prerequisites:
            graph[pre_course].append(course)
            in_degree[course] += 1
            
            # Initialize a queue with courses that have no prerequisites
        queue = deque(course for course in range(numCourses) if in_degree[course] == 0)
        
        print(in_degree)
        print(queue)
        print(graph)
        
           # Topological sort algorithm
        while queue:
            pre_course = queue.popleft()
            for course in graph[pre_course]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)
                    
        print(in_degree)
                    
        return all(in_degree[course] == 0 for course in range(numCourses))
        
    
s = Solution()
# print(s.canFinish(3, [[1,0]]))
# print(s.canFinish(2, [[1,0],[0,1]]))
print(s.canFinish(4, [[1,0],[2,1],[3,2]]))

"""
[
    [1,0],
    [2,1],
    [3,2]
]


0: [1]
1: [2]
2: [3]
"""
