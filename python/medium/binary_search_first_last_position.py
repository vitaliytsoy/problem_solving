"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) - 1
        
        while start <= end:
            middle = (start + end) // 2
            middle_num = nums[middle]
            
            if middle_num == target:
                start, end = middle, middle
                
                while start > 0 and nums[start - 1] == target:
                    start -= 1
                    
                while end < len(nums) - 1 and nums[end + 1] == target:
                    end += 1
                    
                return [start, end]

            if target > middle_num: 
                start = middle + 1
            else:
                end = middle - 1
        
        return [-1, -1]

    
s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8)) # [3, 4]
print(s.searchRange([5,7,7,8,8,10], 6)) # [-1, -1]
print(s.searchRange([], 0)) # [-1, -1]
print(s.searchRange([1], 1)) # [0, 0]
