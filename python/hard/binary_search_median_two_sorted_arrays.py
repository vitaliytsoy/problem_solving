"""
Median of Two Sorted Arrays
Hard
Topics
Companies
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
from typing import List
from collections import deque

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        merged = []
        is_specific = True if total_length % 2 != 0 else False
        n1 = deque(nums1)
        n2 = deque(nums2)
        
        for _ in range((total_length // 2) + 1):
            if n1 and n2:
                if n1[0] < n2[0]:
                    merged.append(n1.popleft())
                else: 
                    merged.append(n2.popleft())
                
                continue
            
            if not n1:
                merged.append(n2.popleft())
                continue
            
            if not n2:
                merged.append(n1.popleft())
                continue

        return merged[-1] if is_specific else (merged[-1] + merged[-2]) / 2
    
    
s = Solution()
print(s.findMedianSortedArrays([1], [2])) # 1.5
print(s.findMedianSortedArrays([1,3], [2])) # 2
print(s.findMedianSortedArrays([1,2], [3,4])) # 2.5

# 1 2 3 4 5 6 7 
# 7 // 2 = 3

# 1 2 3 4 5 6
# 6 // 2 = 3