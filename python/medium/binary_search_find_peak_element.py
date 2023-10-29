"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0 
        end = len(nums) - 1
        
        while start < end:
            mid = (start + end) // 2
            mid_num = nums[mid]
            
            if mid_num < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid
                
        return start
    
    def findPeakElement1(self, nums: List[int]) -> int:
        start = 0 
        end = len(nums) - 1
        
        if (len(nums) == 1):
            return 0
        
        if(nums[0] > nums[1]): 
            return 0
        
        if(nums[len(nums) - 1] > nums[len(nums) - 2]):
            return len(nums) - 1;
        
        while start <= end:
            mid = (start + end) // 2
            num = nums[mid]
            
            if num > nums[mid + 1] and num > nums[mid - 1]:
                return mid
            
            if num < nums[mid - 1]:
                end = mid - 1
                continue
            
            if num < nums[mid + 1]:
                start = mid + 1
                continue
    


s = Solution()
print(s.findPeakElement([1,2,3,1])) # 2
print(s.findPeakElement([1,2,1,3,5,6,4])) # 5
print(s.findPeakElement([1])) # 0
