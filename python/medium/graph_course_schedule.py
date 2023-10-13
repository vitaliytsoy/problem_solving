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
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}
        prereq_count = [0] * numCourses
        
        for prereq in prerequisites:
            course, requirement = prereq
            
            if requirement not in courses:
                courses[requirement] = []
                
            courses[requirement].append(course)
            prereq_count[course] += 1
            
        queue = deque()
        
        for i in range(numCourses):
            if prereq_count[i] == 0:
                queue.append(i)

        while queue:
            prereq = queue.popleft()
            
            if prereq not in courses:
                continue
            
            for course in courses[prereq]:
                prereq_count[course] -= 1
                
                if prereq_count[course] == 0:
                    queue.append(course)
            
        return sum(prereq_count) == 0
        
        
s = Solution()
print(s.canFinish(2, [[1,0]])) # True
print(s.canFinish(2, [[1,0],[0,1]])) # False