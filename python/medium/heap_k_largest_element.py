"""
215. Kth Largest Element in an Array
Medium
16.2K
794
Companies
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?


Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""
from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        random_index = random.randint(0, len(nums) - 1)
        random_num = nums[random_index]
        left, right, middle = [], [] ,[]
        
        for num in nums:
            if num > random_num:
                left.append(num)
                continue
            if num < random_num:
                right.append(num)
                continue
            middle.append(num)
            
        left_size, middle_size = len(left), len(middle)
        
        if left_size == k - 1 :
            return middle[0]
        
        if left_size >= k:
            return self.findKthLargest(left, k)
        
        if middle_size >= k - left_size:
            return middle[0]
        
        return self.findKthLargest(right, k - left_size - middle_size)

    
s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 2)) # 5
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4)) # 4
