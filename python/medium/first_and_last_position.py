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
    def find_lower_bound(self, nums: List[int], target: int):
        start, end = 0, len(nums) - 1
        
        while start <= end:
            middle = (start + end) // 2
            num = nums[middle]
            
            if (start == end):
                return start if nums[start] == target else -1
            
            if (num < target): 
                start = middle + 1
                continue
                
            if (num > target):
                end = middle - 1
                continue
                
            if (middle == 0):
                return middle
                                 
            if (nums[middle - 1] == target):
                end = middle - 1
                continue
            
            return middle
            
        return -1
                
                
    def find_higher_bound(self, nums: List[int], target: int):
        start, end = 0, len(nums) - 1
        
        while start <= end:
            middle = (start + end) // 2
            num = nums[middle]
            
            if (start == end):
                return start if nums[start] == target else -1
            
            if (num < target): 
                if start == middle and end - start == 1:
                    start += 1 
                    continue
                    
                start = middle + 1
                continue
                
            if (num > target):
                if end == middle and end - start == 1:
                    end -= 1 
                    continue

                end = middle - 1
                continue
                
            if (middle == len(nums) - 1):
                return middle
                                 
            if (nums[middle + 1] == target):
                start = middle + 1
                continue
            
            return middle
            
        return -1
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.find_lower_bound(nums, target)
        
        if (start == -1): return [-1, -1]
        
        end = self.find_higher_bound(nums, target)
        
        return [start, end]
        
    
    
s= Solution()
print(s.searchRange([8,8,8,8,8,8], 8))
print(s.searchRange([5,7,7,8,8,10], 6))
