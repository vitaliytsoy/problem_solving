"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        intersections = []
        p1, p2 = 0, 0
        
        while p1 < len(nums1) and p2 < len(nums2):
            v1, v2 = nums1[p1], nums2[p2]
            
            if v1 == v2:
                intersections.append(v1)
                p1 += 1
                p2 += 1
                continue
            
            if v1 < v2: 
                p1 += 1
                continue
                
            if v1 > v2: 
                p2 += 1
                continue
            
        return intersections
    
    def make_array_dict(self, array: List[int]):
        array_dict = {}
        
        for num in array:
            if num in array_dict:
                array_dict[num] += 1
                continue
            
            array_dict[num] = 1
            
        return array_dict
            
    def intersect_dict(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1_dict = self.make_array_dict(nums1)
        n2_dict = self.make_array_dict(nums2)
        fill_dict = {}
        intersection = []
        
        
        for key, value in n1_dict.items():
            if (key in n2_dict):
                fill_dict[key] = min(value, n2_dict[key])
                
                
        for key, value in fill_dict.items():
            for n in range(value):
                intersection.append(key)
                
        return intersection
            
            
    
s = Solution()
# s.intersect([1,2,2,1], [2,2])
# s.intersect([4,9,5], [9,4,9,8,4])
# s.intersect_dict([1,2,2,1], [2,2])
s.intersect_dict([4,9,5], [9,4,9,8,4])