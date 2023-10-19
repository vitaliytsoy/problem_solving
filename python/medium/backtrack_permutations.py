"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]] 
"""
from typing import List

class Solution:
    def backtrack(self, nums, permutation, i, result):
        if (i >= len(permutation)):
            result.append(permutation.copy())
            
            return
            
        for num in nums:
            if num in permutation:
                continue
            
            permutation[i] = num
            
            self.backtrack(nums, permutation, i + 1, result)
            
        permutation[i] = None

    def permute(self, nums: List[int]) -> List[List[int]]:
        if (len(nums) == 0):
            return []
                
        result = []
        permutation = [None] * len(nums)
            
        self.backtrack(nums, permutation, 0, result)

        return result
    
s = Solution()

print(s.permute([0,1])) # [[0, 1], [1, 0]]
print(s.permute([1,2,3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(s.permute([1])) # [[1]]

