"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0

        for index in range(len(nums)):
            num = nums[index]


            if (num != 0):
                nums[pointer] = num
                pointer += 1

        while pointer < len(nums):
            nums[pointer] = 0
            pointer += 1
            

        print(nums)
        




s = Solution()
s.moveZeroes([1,0,3,4,0,12, 3, 5])



