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
    
    
s = Solution()
print(s.jump([2,3,1,1,4])) # 2
print(s.jump([2,3,0,1,4])) # 2
            