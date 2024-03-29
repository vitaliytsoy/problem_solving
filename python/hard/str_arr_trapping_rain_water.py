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
    
    
    # ---   
    
    def find_highest(self, arr, i):
        l_max, r_max = 0, 0
        
        for i in range(0, i):
            if arr[i] > l_max:
                l_max = arr[i]
                
                
        for i in range(i + 1, len(arr)):
            if arr[i] > r_max:
                r_max = arr[i]
            
        return (l_max, r_max)

    def trap(self, height: List[int]) -> int:
        trapped = 0
        
        for i in range(1, len(height) - 1):
            h = height[i]
            left, right = self.find_highest(height, i)
            
            if h >= left or h >= right:
                continue
            
            trapped += min(left, right) - h
        
        return trapped
    
    # ---
    
    def trap(self, height: List[int]) -> int:
        trapped = 0
        max_height = height[0]
        l_max_arr = [0] * len(height) 
        r_max_arr = [0] * len(height) 
        
        for i in range(1, len(height) - 1):
            l_max_arr[i] = max_height
            
            if height[i] > max_height:
                max_height = height[i]
                
        max_height = height[-1]
        
        for i in range(len(height) - 1, -1, -1):
            r_max_arr[i] = max_height
            
            if height[i] > max_height:
                max_height = height[i]

        for i in range(1, len(height) - 1):
            h = height[i]
            l_max = l_max_arr[i]
            r_max = r_max_arr[i]
            
            if h >= l_max or h >= r_max:
                continue
            
            trapped += min(l_max, r_max) - h
        
        return trapped
      
    
    
s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(s.trap([4,2,0,3,2,5])) # 9
