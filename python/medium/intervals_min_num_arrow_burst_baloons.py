"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
"""
from typing import List

class Solution:
    def is_intersecting(self, left, right):
        return (right[1] <= left[1] and right[1] >= left[0]) \
            or (left[1] >= right[0] and left[1] <= right[1])
            
    def merge_intervals(self, left: List[int], right: List[int]) -> bool:
        return [min(left[0], right[0]), max(left[1], right[1])]
    
    
    def find_max_intersection(self, points, intersection, start_at):
        for i in range(start_at, len(points)):
            if self.is_intersecting(points[0], points[i]):
                copy = intersection.copy()
                
                copy.append(i)
                self.find_max_intersection(points, copy)
            
        

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return len(points)
        
        outside = set([])
        
        for i in range(1, len(points)):
            if self.is_intersecting(points[0], points[i]):
                continue
            
            outside.add(i)
            
        return 1 + self.findMinArrowShots([points[i] for i in outside])
            
    
s = Solution()
print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])) # 2 
print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])) # 4
print(s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])) # 2
print(s.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))