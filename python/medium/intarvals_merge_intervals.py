"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""
from typing import List


# [1, 3] [2, 4]
# [1, 3] [0, 4]
# [1, 4] [2, 3]
# [1, 3] [0, 2]
class Solution:
    def is_interlacing(self, left: List[int], right: List[int]) -> bool:
        return right[1] <= left[1] and right[1] >= left[0] \
            or right[0] <= left[1] and right[1] >= left[1]
    
    def merge_intervals(self, left: List[int], right: List[int]) -> bool:
        return [min(left[0], right[0]), max(left[1], right[1])]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pointer = 1
        result = []
        
        intervals.sort()
        
        while pointer < len(intervals):
            current = intervals[pointer]
            prev = intervals[pointer - 1]
            
            if (self.is_interlacing(current, prev)):
                intervals[pointer] = self.merge_intervals(current, prev)
            else:
                result.append(prev)

            pointer += 1
            
        result.append(intervals[-1])
            
        return result
    
    
s = Solution()
# print(s.merge([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
# print(s.merge([[1,4],[4,5]])) # [[1,4],[4,5]]
# print(s.merge([[1,5],[6,7]])) # [[1,5],[6,7]]
print(s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]])) # [[1,10]]