"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""
from typing import List

class Solution:
    def is_trapped(self, arr, i):
        prev, post = i - 1, i + 1
        
        while prev >= 0:
            if arr[prev] >= 1:
                break
            
            prev -= 1
            
        while post < len(arr):
            if arr[post] >= 1:
                break
            
            post += 1
            
            
        return prev >= 0 and post < len(arr)
    
    def trap(self, height: List[int]) -> int:
        trapped = 0
        
        while sum(height) > 0:
            for i in range(1, len(height) - 1):
                if height[i] == 0 and self.is_trapped(height, i):
                    trapped += 1
                    
            for i in range(0, len(height)):
                if height[i] >= 1:
                    height[i] -= 1
    
        return trapped            
    
    
s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(s.trap([4,2,0,3,2,5])) # 9
