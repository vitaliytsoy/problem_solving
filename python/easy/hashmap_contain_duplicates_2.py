"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if j - i > k:
                    break;
            
                if nums[i] == nums[j] and j - i <= k:
                    return True
                
        return False
    
    # ---
    
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        
        for i in range(len(nums)):
            num = nums[i]
            
            if num in mp:
                mp[num].append(i)
                continue
            
            mp[num] = [i]
            
        print(mp)
            
        for indexes in mp.values():
            if len(indexes) <= 1:
                continue
            
            for i in range(len(indexes)):
                # print(indexes, i, i + 1)
                # print(indexes[i + 1], indexes[i])
                if i + 1 < len(indexes) and indexes[i + 1] - indexes[i] <= k:
                    return True
   
        return False
    
    
s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1], 3)) # True
print(s.containsNearbyDuplicate([1,0,1,1], 1)) # True
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2)) # False