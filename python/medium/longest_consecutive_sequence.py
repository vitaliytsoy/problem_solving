"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""
from typing import List 
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        numbers = defaultdict(lambda : 0)
        
        for num in nums: 
            if (num in numbers and numbers[num] != 0):
                continue
            
            left = numbers[num - 1] 
            right = numbers[num + 1]
            numbers[num] = left + right + 1
            numbers[num - left] = numbers[num]
            numbers[num + right] = numbers[num]
            result = max(result, numbers[num])            

        return result
    
    def longestConsecutive_set(self, nums: List[int]) -> int:
        set_nums = set(nums)
        result = 0
        
        for num in nums: 
            if num - 1 not in set_nums:
                maximum = num
                
                while maximum in set_nums:
                    maximum += 1
                    
                result = max(maximum - num, result) 
                
        return result


    def longestConsecutive_nlogn(self, nums: List[int]) -> int:
        start, end = 0, 1
        longest_sequence = 0
        
        nums = sorted(list(set(nums)))
        
        if (len(nums) <= 1):
            return len(nums)
        
        while end < len(nums):
            if (nums[end - 1] != nums[end] - 1):
                longest_sequence = max(end - start, longest_sequence)
                start = end 
                end += 1
                continue;
                
            end += 1
                
        return max(end - start, longest_sequence)
    


s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2])) # 4
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9
print(s.longestConsecutive([0])) # 1
print(s.longestConsecutive([1,2,0,1])) # 3

# 100,4,200,1,3,2