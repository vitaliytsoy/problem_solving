"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        x_new, y_new = newInterval
        
        for interval in intervals:
            x_cur, y_cur = interval
            
            if (y_cur < x_new): # 7 < 3
                left.append(interval)
            elif(x_cur > y_new): # 6 > 8
                right.append(interval)
            else:
                x_new = min(x_new, x_cur)
                y_new = max(y_new, y_cur)
                
        return left + [[x_new, y_new]] + right

    
    def merge(self, range_a, range_b):
        x_a, y_a = range_a
        x_b, y_b = range_b
        
        return [min(x_a, x_b), max(y_a, y_b)]
    
    def is_intersecting(self, range_a, range_b):
        x_a, y_a = range_a
        x_b, y_b = range_b

        return (x_a <= x_b and y_a >= y_b) \
            or (x_a <= x_b and x_b <= y_a and y_a < y_b) \
            or (x_a > x_b and y_a >= y_b and y_b >= x_a) \
            or (x_a > x_b and y_a < y_b)
        
    
    def insert_own(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        p_current, p_next = 0, 1
        x_new, y_new = newInterval
        
        if (len(intervals) == 0):
            intervals.append(newInterval)

            return intervals
        
        while p_current < len(intervals):
            x_cur, y_cur = intervals[p_current]
            is_intercept_current = self.is_intersecting(intervals[p_current], newInterval)
            
            if (is_intercept_current):
                # handle range merge
                merged = self.merge(intervals[p_current], newInterval)
                
                while (p_next < len(intervals) and self.is_intersecting(merged, intervals[p_next])):
                    merged = self.merge(merged, intervals[p_next])
                    intervals.pop(p_next)
                    
                intervals[p_current] = merged
                break
            elif (p_current == 0 and x_new < x_cur):
                # insert to start
                intervals.insert(0, newInterval)
                break
            elif (p_current == len(intervals) - 1 and x_new > x_cur):
                # insert to end
                intervals.append(newInterval)
                break
            
            x_next, _ = intervals[p_next]
            
            if (x_new > y_cur and y_new < x_next):
                # insert in between
                intervals.insert(p_next, newInterval)
                pass
            
            p_current += 1
            p_next += 1        
                
        return intervals
        
s = Solution()

print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) # [[1,2],[3,10],[12,16]]
# print(s.insert([[1,3],[6,9]], [2,5])) # [[1,5],[6,9]]
# print(s.insert([[1,3],[6,7]], [4,5])) #  [[1, 3], [4, 5], [6, 7]]
# print(s.insert([[3,4],[6,7]], [1,2])) #  [[1, 2], [3, 4], [6, 7]]
# print(s.insert([[3,4],[6,7]], [8,9])) #  [[3, 4], [6, 7], [8, 9]]
            
# [4, 8], [3, 6] inside
# [4, 8], [5, 9] right-out
# [4, 8], [3, 8] left-out
# [4, 8], [3, 9] left-right-out

