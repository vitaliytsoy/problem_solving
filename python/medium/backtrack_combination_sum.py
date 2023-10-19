"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1
Output: []
"""
from typing import List

class Solution:
    def backtrack(self, candidates, result, target, combination, curr_sum):
        if curr_sum > target:
            return
        
        if curr_sum == target:
            result.append(combination.copy())
            
            return
            
        for num in candidates:
            if  num > target - curr_sum :
                continue
            
            if len(combination) > 0 and num < combination[-1]:
                continue

            combination.append(num)
                
            self.backtrack(candidates, result, target, combination,  curr_sum + num)
            
            combination.pop()
            
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        candidates.sort()
        
        self.backtrack(candidates, result, target, [], 0)
        
        return result

s = Solution()
print(s.combinationSum([2,3,6,7], 7)) # [[2,2,3],[7]]
print(s.combinationSum([2,3,5], 8)) # [[2,2,2,2],[2,3,3],[3,5]]
print(s.combinationSum([2], 1)) # []
