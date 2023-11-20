"""
Given an integer array nums, return the length of the longest strictly increasing 
subsequence.

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""
from typing import List

class Solution:
    def find_LIS(self, nums, i, lis):  
        max_lis = lis      
        
        for j in range(i, len(nums)):
            num = nums[j]
            
            if (num > nums[i]):
                max_lis = max(max_lis, self.find_LIS(nums, j, lis + 1))
                
        return max_lis
        
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums)):
            dp[i] = self.find_LIS(nums, i, 1)
            
        return max(dp)
    
s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18])) # 4
print(s.lengthOfLIS([0,1,0,3,2,3])) # 4
print(s.lengthOfLIS([7,7,7,7,7,7,7])) # 4
