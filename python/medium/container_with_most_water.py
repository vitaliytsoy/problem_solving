"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        area = 0
        
        while start < end:
            new_area = (end - start) * min(height[start], height[end])
            
            if (area < new_area):
                area = new_area
                
            if (height[start] > height[end]):
                end -= 1
                
            else:
                start += 1 
                
        return area
    
    
s= Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(s.maxArea([1,1])) # 1
