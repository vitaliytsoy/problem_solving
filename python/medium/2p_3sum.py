"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.


Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.


Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

"""

from typing import List

class Solution:
    # Time Limit
    
    def find_three_sum(self, nums, i, j, k, result, visited):
        if i >= len(nums) or j >= len(nums) or k >= len(nums):
            return result
        
        if j >= k or i >= j:
            return result
        
        if i in visited:
            self.find_three_sum(nums, i + 1, j, k, result, visited)
            return result
            
        if j in visited:
            self.find_three_sum(nums, i, j + 1, k, result, visited)
            return result
            
        if k in visited:
            self.find_three_sum(nums, i, j, k + 1, result, visited)
            return result
        
        if (nums[i] + nums[j] + nums[k] == 0):
            visited.add(i)
            visited.add(j)
            visited.add(k)
            result.append([nums[i], nums[j], nums[k]])
            
        self.find_three_sum(nums, i + 1, j, k, result, visited)
        self.find_three_sum(nums, i, j + 1, k, result, visited)
        self.find_three_sum(nums, i, j, k + 1, result, visited)
        
        return result
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.find_three_sum(nums, 0, 1, 2, [], set())
    
    
    # ---
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        negative, zero, positive = [], [], []
        result = set()
        
        nums.sort()
        
        for num in nums:
            if num < 0:
                negative.append(num)
                continue
                
            if num > 0:
                positive.append(num)
                continue
            
            zero.append(num)
            
        n_unique, p_unique = set(negative), set(positive)

        if len(zero) >= 3:
            result.add((0,0,0))
            
        if (len(positive) == 0 or len(negative) == 0):
            return result
            
        if len(zero) >= 1:
            for num in n_unique:
                if abs(num) in p_unique:
                    result.add((0, num, abs(num)))
                    
                    
        p1, p2 = 0, 1
        
        if len(negative) >= 2:
            while p1 < len(negative) - 1:
                while p2 < len(negative):
                    absolute = abs(negative[p1] + negative[p2])
                    
                    if absolute in p_unique:
                        result.add((negative[p1], negative[p2], absolute))
                    
                    p2 += 1
                    
                p1 += 1
                p2 = p1 + 1
                
        
        p1, p2 = 0, 1  
                
        if len(positive) >= 2:
            while p1 < len(positive) - 1:
                while p2 < len(positive):
                    absolute = positive[p1] + positive[p2]
                    
                    if -absolute in n_unique:
                        result.add((-absolute, positive[p1], positive[p2], ))
                    
                    p2 += 1
                    
                p1 += 1
                p2 = p1 + 1
                
        return result
    
    
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,1,1]))
print(s.threeSum([0,0,0]))
