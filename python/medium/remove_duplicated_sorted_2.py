"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores)
"""
from typing import List
import sys

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dupes = 0
        i = 0
        
        while i < len(nums) - 1:
            if (nums[i] == nums[i + 1]):
                j = i + 1 
                
                while ((j + 1) < len(nums) and nums[i] == nums[j + 1]):
                    j += 1
                    
                count = j - i + 1
                    
                if (count > 2):
                    count -= 2
                    dupes += count
                
                    while count > 0:
                        count -= 1
                        nums[j - count] = sys.maxsize
                        
                    i = j
                    
            i += 1
                    
        nums.sort()
                    
        return len(nums) - dupes
                    
                
                        
s = Solution()
# s.removeDuplicates([0,0,1,1,1,1,2,3,3])
# s.removeDuplicates([1,1,1,2,2,3])
s.removeDuplicates([1,1,1,2,2,2,3,3])
# s.removeDuplicates([0,0,0,0,0])
                
            

    
    
    