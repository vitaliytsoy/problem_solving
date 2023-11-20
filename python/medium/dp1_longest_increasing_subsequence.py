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
    
    
    # ---
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [(-1, -1)] * len(nums)
        dp[0] = (1, nums[0])

        for i in range(1, len(nums)):
            num = nums[i]
            lis = 1
            
            for j in range(i):
                lis_count, lis_num = dp[j]
                
                if (num <= lis_num):
                    continue
                
                lis = max(lis, lis_count + 1)
                
            dp[i] = (lis, num)
            
        return max(dp)[0]
    
s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18])) # 4
print(s.lengthOfLIS([0,1,0,3,2,3])) # 4
print(s.lengthOfLIS([7,7,7,7,7,7,7])) # 1
