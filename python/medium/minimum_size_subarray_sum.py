"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""
from typing import List
import sys

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 0
        min_len = sys.maxsize
        s = nums[0]
        
        while start <= end or end + 1 < len(nums):
            if (s >= target and end - start < min_len):
                min_len = end - start
                    
            if (s < target and end + 1 <= len(nums) - 1):
                end += 1
                s += nums[end]
            else: 
                s -= nums[start]
                start += 1
                
        return min_len + 1 if min_len + 1 < sys.maxsize else 0
    
    
s = Solution()

print(s.minSubArrayLen(7, [2,3,1,2,4,3])) # 2
print(s.minSubArrayLen(4, [1,4,4])) # 1
print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1])) # 0
print(s.minSubArrayLen(6, [10,2,3])) # 1