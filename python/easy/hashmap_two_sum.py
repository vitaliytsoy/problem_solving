"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = 1
        
        while start < len(nums) - 1:
            while end < len(nums):
                if nums[start] + nums[end] == target:
                    return [start, end]
            
                end += 1
            
            start += 1
            end = start + 1
            
        return [start, end]
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}
        
        for i in range(len(nums)):
            num = nums[i]
            
            if num in mapper:
                return [mapper[num], i]
            
            mapper[target - num] = i
            
        return [-1, -1]
    
    
s = Solution()
print(s.twoSum([2,7,11,15], 9)) # [0, 1]
print(s.twoSum([3,2,4], 6)) # [1, 2]
print(s.twoSum([3,3], 6)) # [0, 1]
print(s.twoSum([0,4,3,0], 0)) # [0, 3]