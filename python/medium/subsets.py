"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return nums
        
        if len(nums) == 1:
            return [[], [nums[0]]]
        
        result = []
        
        self.make_subsets(0, [], nums, result)
    
        return result
    
    def make_subsets(self, index: int, subset: List[int], nums: List[int], acc: List[List[int]]) -> List[List[int]]:
        if index >= len(nums):
            return
        
        if len(acc) == 0:
            acc.append([])
            
        self.make_subsets(index + 1, subset.copy(), nums, acc)
        
        subset.append(nums[index])
        acc.append(subset.copy())
        self.make_subsets(index + 1, subset.copy(), nums, acc)
    
    
s = Solution()
print(s.subsets([1,2,3,4]))
