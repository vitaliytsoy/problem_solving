"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""
from typing import List

class Solution:    
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            middle = (end + start) // 2
            
            if target == nums[middle]:
                return middle
            
            if target > nums[middle]:
                start = middle + 1
            elif target < nums[middle]:
                end = middle - 1   
        
        return max(start, end) 
        

s = Solution()
print(s.searchInsert([1,3,5,6], 5)) # 2
print(s.searchInsert([1,3,5,6], 2)) # 1
print(s.searchInsert([1,3,5,6], 7)) # 4
print(s.searchInsert([1,3,5,6], 0)) # 0
