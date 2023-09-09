""" 
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
from typing import List
from collections import defaultdict

class Solution:
    # Boyer–Moore majority vote algorithm
    def majorityElemen_boyer_moore(self, nums: List[int]) -> int:
        major = nums[0]
        count = 1
        
        for i in range(1, len(nums)):
            if (count == 0):
                major = nums[i]
                count += 1
                continue
            
            if (major != nums[i]):
                count -= 1
                continue
            
            if (major == nums[i]):
                count += 1
                continue
            
        return major
    
    def majorityElement(self, nums: List[int]) -> int:
        major = '#'
        entries = defaultdict(lambda: 0)
        
        for n in nums:
            if (n in entries): 
                entries[n] += 1
            else:
                entries[n] = 1
                
            if (entries[n] > entries[major]):
                major = n
                
        return major
                


    
s = Solution()
# print(s.majorityElement([3,2,3]))
# print(s.majorityElement([3,3,4]))
print(s.majorityElemen_boyer_moore([1,3,1,1,4,1,1,5,1,1,6,2,2]))

