"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
"""
from typing import List
import sys

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_sum_min = 0
        curr_sum_max = 0
        total_sum = 0
        min_sum = sys.maxsize
        max_sum = -sys.maxsize
        
        for num in nums:
            curr_sum_min += num
            curr_sum_max += num
            total_sum += num
            
            if curr_sum_min < min_sum:
                min_sum = curr_sum_min
                
            if curr_sum_max > max_sum:
                max_sum = curr_sum_max
                
            if curr_sum_min > 0:
                curr_sum_min = 0
                
            if curr_sum_max < 0:
                curr_sum_max = 0
        
        return max_sum if total_sum == min_sum else max(max_sum, total_sum - min_sum)
    
    
s = Solution()
print(s.maxSubarraySumCircular([1,-2,3,-2])) # 3
print(s.maxSubarraySumCircular([5,-3,5])) # 10
print(s.maxSubarraySumCircular([-3,-2,-3])) # -2
    