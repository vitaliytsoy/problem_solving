"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            mid_num = nums[mid]
            
            if mid_num == target:
                return mid
            
            if mid_num > nums[end] or mid_num < nums[start]: 
                # pivoted
                if mid_num > nums[end]:
                    if target >= nums[start] and target <= mid_num:
                        end = mid
                    else:
                        start = mid + 1   
                else:
                    if target <= nums[end] and target >= mid_num:
                        start = mid
                    else:
                        end = mid - 1
            else:
                # not pivoted
                if mid_num < target:
                    start = mid + 1
                else:
                    end = mid - 1                    
            
        return -1
        
        
s = Solution()
print(s.search([4,5,6,7,0,1,2], 0)) # 4
print(s.search([4,5,6,7,0,1,2], 3)) # -1
print(s.search([1], 0)) # -1
print(s.search([3,1], 1)) # 1
print(s.search([5,1,3], 5)) # 0
print(s.search([4,5,6,7,8,1,2,3], 8)) # 4
