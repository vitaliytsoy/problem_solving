"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation. 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        count = 1
               
        for i in range(1, len(nums)):
            answer[i] = count * nums[i - 1]
            count *= nums[i - 1]
            
            
        count = 1
            
        for i in range(len(nums) - 2, -1, -1):
            answer[i] *= count * nums[i + 1]
            count *= nums[i + 1]
        
        return answer
            
s = Solution()
print(s.productExceptSelf([1,2,3,4])) # [24,12,8,6]
print(s.productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]
