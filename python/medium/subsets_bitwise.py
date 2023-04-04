"""
Given an integer array nums of unique elements, return all possible 
subsets(the power set).

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
        n = len(nums)
        result = []

        for i in range(2**n):
            subset = []
            
            for j in range(n):
                print(f"i {i} j {j} shift {1 << j} num {i & (1 << j)}")
                if i & (1 << j):
                    print(nums[j])
                    subset.append(nums[j])

            print(subset)
            result.append(subset)

        return result
    
    
s = Solution()
print(s.subsets([1,2,3,4]))
    
    