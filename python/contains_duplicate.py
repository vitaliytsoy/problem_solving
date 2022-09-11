"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)

        if len(unique) < len(nums):
            return True

        return False

    def contains_duplicate(self, nums: List[int]) -> bool:
        dict = {}

        for num in nums:
            if num in dict: 
                return True
            else:
                dict[num] = 1

        return False


solution = Solution()

print(solution.containsDuplicate([1,2,3,1]))
        