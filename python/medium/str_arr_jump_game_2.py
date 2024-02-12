"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
"""
from typing import List
from collections import deque
import sys

class Solution:
    def jump(self, nums: List[int]) -> int:
        stack = deque([(0, 0)])
        min_count = sys.maxsize
        
        while stack:
            counter, pointer = stack.pop()
            
            if pointer >= len(nums):
                continue
            
            if pointer == len(nums) - 1:
                min_count = min(min_count, counter)
                
                continue
            
            distance = nums[pointer]
            
            for i in range(1, distance + 1):
                stack.append((counter + 1, pointer + i))
                
        return min_count
    
    # ---
    
    def jump(self, nums: List[int]) -> int:
        min_jump_reach = [sys.maxsize] * len(nums)
        min_jump_reach[0] = 0
        
        for i in range(len(nums)):
            distance = nums[i]
            
            for j in range(1, distance + 1):
                if i + j >= len(nums):
                    break
                
                if min_jump_reach[i + j] != sys.maxsize:
                    continue
                
                min_jump_reach[i + j] = min(min_jump_reach[i] + 1, min_jump_reach[i + j])
                
        return min_jump_reach[-1]
    
    
    # --- Greedy
    
    def jump(self, nums: List[int]) -> int:
        max_reach = 0
        last_p = 0
        counter = 0
        
        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])
            
            if i == last_p:
                counter += 1
                last_p = max_reach
        
        return counter
                
    
s = Solution()
print(s.jump([2,3,1,1,4])) # 2
print(s.jump([2,3,0,1,4])) # 2
            