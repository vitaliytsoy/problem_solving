"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""
from typing import List


class Solution:
    def find_max_sum(self, nums: List, n: int) -> int:
        if n < 0:
            return 0

        return max(self.find_max_sum(nums, n - 2) + nums[n], self.find_max_sum(nums, n - 1))

    def rob(self, nums: List[int]) -> int:
        return self.find_max_sum(nums, len(nums) - 1)
    
    
    # ---
    
    cache = {}
    
    def find_max_sum(self, nums: List, n: int) -> int:
        if n < 0:
            return 0
        
        if n in self.cache:
            return self.cache[n]
        
        self.cache[n] = max(self.find_max_sum(nums, n - 2) + nums[n], self.find_max_sum(nums, n - 1))

        return self.cache[n]
    
    def rob(self, nums: List[int]) -> int:
        self.cache = {}
        
        return self.find_max_sum(nums, len(nums) - 1)
    
    # ---
    
    def find_max_sum(self, nums: List, n: int) -> int:
        if n < 0:
            return 0
        
        if n in self.cache:
            return self.cache[n]
        
        self.cache[n] = max(self.find_max_sum(nums, n - 2) + nums[n], self.find_max_sum(nums, n - 1))

        return self.cache[n]
    
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        
        for i in range(len(nums)):
            cache[i] = max(nums[i])
            
            

        
        return 
    
    
    
    
s = Solution()
print(s.rob([1,2,3,1])) # 4
print(s.rob([2,7,9,3,1])) # 12
