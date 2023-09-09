"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Do not return anything, modify nums in-place instead.

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Do not return anything, modify nums in-place instead.

"""
from typing import List
import math

class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start +=1
            end -= 1

    def rotate_fast(self, nums: List[int], k: int) -> None:
        if (k == len(nums)):
            return None
        
        new_k = k if k < len(nums) else k - ((k // len(nums)) * len(nums))
    
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, new_k - 1)
        self.reverse(nums, new_k, len(nums) - 1)

    def rotate(self, nums: List[int], k: int) -> None:
        if (k == len(nums) or k == 0):
            return None
        
        new_k = k if k < len(nums) else k - ((k // len(nums)) * len(nums))
        
        for i in range(len(nums) - 1, new_k - 1, -1):            
            for j in range(1, new_k + 1):
                nums[i], nums[i - j] = nums[i - j], nums[i]
                
        
s = Solution()
s.rotate_fast([1,2,3,4,5,6,7], 3) # [5,6,7,1,2,3,4]
s.rotate_fast([-1,-100,3,99], 2) # [3,99,-1,-100]
s.rotate_fast([1,2,3], 0) # [1,2,3]