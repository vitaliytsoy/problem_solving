
"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b    

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"


"""
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) <= 1:
            return [str(num) for num in nums]
        
        start, end = 0, 0
        result = []
        
        for index in range(len(nums)):
            if index == 0:
                continue
            
            if nums[index] == nums[index - 1] + 1:
                end += 1
                continue
            
            result.append(str(nums[start]) if start == end else f"{nums[start]}->{nums[end]}")
            start = index
            end = index
            
        result.append(str(nums[start]) if start == end else f"{nums[start]}->{nums[end]}")
        
        return result

        
        
s = Solution()
s.summaryRanges([0,2,3,4,6,8,9])
s.summaryRanges([0,1,2,4,5,7])
s.summaryRanges([-1])